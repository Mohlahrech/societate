from odoo import models, fields, api, _
import logging  as log
from odoo.http import request


class AccountMove(models.Model):
    _inherit = 'account.move'

    
    payment_mode_supplier = fields.Many2one(
        'account.payment.mode',
        string="Mode de paiement",
        
    )

    payment_mode_supplier_type = fields.Selection(related='payment_mode_supplier.mode_type')


    amount_timbre_supplier = fields.Monetary(string="Droit de timbre", compute='_compute_amount_timbre_supplier', store=True)
    amount_with_timbre_supplier = fields.Monetary(string="Montant avec timbre", compute='_compute_amount_timbre_supplier', store=True)
    
    """Un champ boolean utilisé pour la visibilté d'autre champs en fonction de la valeur de champ  'Se basé sur' """
    #for_based_on_in_move = fields.Boolean(string="Pour le champ 'Se basé sur'",compute="compute_for_based_on")
    for_based_on_in_move = fields.Boolean(string="Pour le champ 'Se basé sur'",compute="compute_for_based_on")

    def compute_for_based_on(self):
        conf = self.env['res.config.settings'].sudo().search([], order='id desc', limit=1)
        if conf.based_on == "posted_invoices":
            self.for_based_on_in_move = True
        else:
            self.for_based_on_in_move = False

    @api.onchange('payment_mode_supplier', 'amount_timbre_supplier')
    def onchange_amount_timbre_supplier(self):
        if self.payment_mode_supplier.mode_type != "cash":
            self.amount_timbre_supplier = 0.0


    def _timbre_supplier(self, amount_total):
        timbre = 0.0
        if self.payment_mode_supplier_type and self.payment_mode_supplier.mode_type == "cash":
            company = self.env['res.company'].search([('id', 'in', self.get_current_company_value())], limit=1)
            company_id = company or self.company_id
            timbre = company_id._timbre(amount_total)
        return timbre

    @api.depends('amount_total', 'payment_mode_supplier', 'invoice_line_ids')
    def _compute_amount_timbre_supplier(self):
        for record in self:
            if record.move_type in ['in_invoice', 'in_refund']:
                if record.payment_mode_supplier.mode_type != 'cash':
                    record.amount_timbre_supplier = 0
                    record.amount_with_timbre_supplier = 0
                    record._recompute_timbre_supplier()
                else:
                    record.amount_timbre_supplier = record._timbre_supplier(record.amount_total)
                    record.amount_with_timbre_supplier = record.amount_total + record.amount_timbre_supplier if record.amount_timbre_supplier else 0.0
                    record._recompute_timbre_supplier()

    def get_current_company_value(self):
        cookies_cids = [int(r) for r in request.httprequest.cookies.get('cids').split(",")] \
            if request.httprequest.cookies.get('cids') \
            else [request.env.user.company_id.id]

        for company_id in cookies_cids:
            if company_id not in self.env.user.company_ids.ids:
                cookies_cids.remove(company_id)
        if not cookies_cids:
            cookies_cids = [self.env.company.id]
        if len(cookies_cids) == 1:
            cookies_cids.append(0)
        return cookies_cids

    def _recompute_timbre_supplier(self):
        self.ensure_one()
        company = self.env['res.company'].search([('id', 'in', self.get_current_company_value())], limit=1)
        company_id = company or self.company_id

        if company_id.based_on == 'posted_invoices':
            if self.move_type in ['in_invoice', 'in_refund']:
                if self.payment_mode_supplier and self.payment_mode_supplier.mode_type == 'cash':
                    in_draft_mode = self != self._origin
                    create_method = in_draft_mode and self.env['account.move.line'].new or self.env['account.move.line'].create
                    supplier_timbre = self.amount_timbre_supplier
                    account_timbre_id  = company_id.purchase_offset_account

                    timbre_line_vals = {
                        'name': 'Droit de timbre fournisseur',
                        'quantity': 1.0,
                        'account_id': account_timbre_id.id,
                        'move_id': self.id,
                        'debit':supplier_timbre,
                    }

                    existing_timbre_line = self.line_ids.filtered(lambda line: line.account_id == account_timbre_id)
                    timbre_line = create_method(timbre_line_vals) if not existing_timbre_line else existing_timbre_line

                    existing_lines = self.line_ids.filtered(lambda line: line.account_id != account_timbre_id)

                    curr_line = 'debit'

                    curr_amount = sum(existing_lines.mapped(curr_line))
                    timbre_line.update({
                        #curr_line: supplier_timbre,
                        curr_line: company_id._timbre(curr_amount),

                    })
                else:
                    # for line in self.line_ids:
                    #     if line.account_id == company_id.purchase_offset_account:
                    #         self.line_ids -= line
                    for line in self.line_ids.filtered(
                        lambda x: x.account_id == company_id.purchase_offset_account and x.move_id.state != 'posted'):
                        self.line_ids -= line
       
        
    
    # def _recompute_dynamic_lines(self, recompute_all_taxes=False, recompute_tax_base_amount=False):
    #
    #     for invoice in self:
    #         # verifier la/les taxe(s) avant calcule/recalcule du timbre
    #         for line in invoice.line_ids:
    #             if line.recompute_tax_line:
    #                 recompute_all_taxes = True
    #                 line.recompute_tax_line = False
    #             if recompute_all_taxes:
    #                 invoice._recompute_tax_lines()
    #             if recompute_tax_base_amount:
    #                 invoice._recompute_tax_lines(recompute_tax_base_amount=True)
    #
    #         if invoice.is_invoice(include_receipts=False):
    #             invoice._recompute_timbre_supplier()
    #
    #     return super(AccountMove, self)._recompute_dynamic_lines(recompute_all_taxes, recompute_tax_base_amount)
    
   
    
