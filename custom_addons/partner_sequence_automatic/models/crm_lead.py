from odoo import models, fields, api
from odoo.exceptions import UserError


class CrmLead(models.Model):
    _inherit = "crm.lead"

    has_duplicate_phone = fields.Boolean(
        string="Has Duplicate Phone", compute="_compute_has_duplicate_phone", store=False
    )

    patient_ref = fields.Char(
        string="Patient Reference",
        related="partner_id.ref",
        store=True,
        readonly=False, placeholder="Ce patient n'existe pas.")

    date_of_birth = fields.Date(string='Date de naissance',
                                help='Date of birth of the patient')

    date_of_accord = fields.Date(string='Date Accords Caisse',
                                help='Date of birth of the patient')



    wilaya_cnas = fields.Char(
        string="Wilaya Cnas",
        store=True,
        readonly=False)

    antene_caisse = fields.Char(
        string="Antenne caisse",
        store=True,
        readonly=False)

    pathologie = fields.Char(
        string="Pathologie",
        store=True,
        readonly=False)

    cause_pathologie = fields.Char(
        string="Cause de la pathologie",
        store=True,
        readonly=False)


    call_ids = fields.One2many("crm.call.history", "crm_id", string="Liste des apelles")





    # @api.depends('phone','mobile')
    # def _compute_has_duplicate_phone(self):
    #     for lead in self:
    #         if lead.phone:
    #             duplicate_partner = self.env['res.partner'].search_count([('phone', '=', lead.phone)
    #             ])
    #
    #         if lead.mobile:
    #             duplicate_partner2 = self.env['res.partner'].search_count([('mobile', '=', lead.mobile)
    #             ])
    #             lead.has_duplicate_phone = duplicate_partner > 0 or duplicate_partner2 > 0
    #         else:
    #             lead.has_duplicate_phone = False

    @api.depends('phone', 'mobile')
    def _compute_has_duplicate_phone(self):
        for lead in self:
            duplicate_partner = 0
            duplicate_partner2 = 0
            duplicate_partner3 = 0
            duplicate_partner4 = 0
            if lead.phone:
                duplicate_partner = self.env['res.partner'].search_count([('phone', '=', lead.phone)])
                duplicate_partner3 = self.env['res.partner'].search_count([('mobile', '=', lead.phone)])

            if lead.mobile:
                duplicate_partner2 = self.env['res.partner'].search_count([('mobile', '=', lead.mobile)])
                duplicate_partner4 = self.env['res.partner'].search_count([('phone', '=', lead.mobile)])

            lead.has_duplicate_phone = duplicate_partner > 0 or duplicate_partner2 > 0 or duplicate_partner3 > 0 or duplicate_partner4 > 0



    @api.depends('partner_id')
    def _compute_contact_name(self):
        # Override the method to do nothing
        pass

    @api.depends('partner_id.phone')
    def _compute_phone(self):
        # Override the method to do nothing
        pass

    def _inverse_phone(self):
        # Override the method to do nothing
        pass

    @api.depends('partner_id')
    def _compute_mobile(self):
        # Override the method to do nothing
        pass

    @api.depends('partner_id')
    def _compute_partner_address_values(self):
        # Override the method to do nothing
        pass




    def create_partner_from_lead(self):
        for lead in self:
            # Check if user_id is defined
            if not lead.user_id:
                raise UserError("Veuillez assigner un PFP avant de créer le patient.")

            if lead.has_duplicate_phone:
                raise UserError("Un client avec le même numéro de téléphone existe déjà.")

            # Collect the values to create the partner
            partner_values = {
                'is_patient': True,
                'name': lead.name,
                'street': lead.street,
                'street2': lead.street2,
                'city': lead.city,
                'state_id': lead.state_id.id if lead.state_id else False,
                'zip': lead.zip,
                'country_id': lead.country_id.id if lead.country_id else False,
                'function': lead.function,
                'phone': lead.phone,
                'mobile': lead.mobile,
                'email': lead.email_from,
                'telecomercial': lead.user_id.id,
                'hospital_id': lead.campaign_id.id,
                'date_of_birth': lead.date_of_birth,
                'securite_id': lead.source_id.id if lead.source_id else False,
            }

            # Create the partner record
            partner = self.env['res.partner'].create(partner_values)

            # Optionally, link the partner to the lead if needed
            lead.partner_id = partner

        return True



    # all this have been put here just to hide the damn create quotation button and better performance

    sale_amount_total = fields.Monetary(compute='_compute_sale_data', string="Sum of Orders",
                                        help="Untaxed Total of Confirmed Orders", currency_field='company_currency')
    quotation_count = fields.Integer(compute='_compute_sale_data', string="Number of Quotations")
    sale_order_count = fields.Integer(compute='_compute_sale_data', string="Number of Sale Orders")


    def action_sale_quotations_new(self):
        # Override the method to do nothing
        pass

    def action_view_sale_quotation(self):
        # Override the method to do nothing
        pass

    def action_view_sale_order(self):
        # Override the method to do nothing
        pass



    @api.onchange('stage_id')
    def _onchange_stage_id(self):
        if self.stage_id:
            return {
                'warning': {
                    'title': "Vous avez changé l'étape",
                    'message': f"Le patient: '{self.name}' a été changé vers '{self.stage_id.name}'.",
                }
            }