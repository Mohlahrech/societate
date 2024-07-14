from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    id_nat = fields.Char(string="Numéro d'Identité Nationale",related="partner_id.id_nat")
    company_type = fields.Selection(string='Company Type',
                                    related='partner_id.company_type',
                                    selection=[('person', 'Individual'), ('company', 'Company')])


    @api.depends('partner_id')
    @api.onchange('partner_id')
    def update_id_nat(self):
        for rec in self:
            if rec.partner_id:
                rec.id_nat = rec.partner_id.id_nat

    # @api.constrains('id_nat')
    # def check_id_nat(self):
    #     for rec in self:
    #         if rec.id_nat:
    #             if len(rec.id_nat) != 18:
    #                 raise ValidationError(_('NIN doit être une suite de 18 caractères '))
    @api.depends('id_nat')
    @api.onchange('id_nat')
    def update_client(self):
        for rec in self:
            if rec.id_nat:
                client = rec.env['res.partner'].sudo().search([('id_nat', '=', rec.id_nat)],limit=1)
                if client:
                    rec.partner_id = client
                else:
                    raise ValidationError(_('Cet NIN n\'existe pas veuillez le creer s\'il vous plait'))


    @api.depends('partner_id')
    @api.onchange('partner_id')
    def update_id_nat(self):
        for rec in self:
            if rec.partner_id:
                rec.id_nat = rec.partner_id.id_nat
class ResPartner(models.Model):
    _inherit = "res.partner"

    entity = fields.Selection(string='Entité juridique', selection=[('private', 'Privé'), ('public', 'Publique')],
                              default='private')

    birth_date = fields.Date(string=u"Date de naissance", tracking=True,)
    id_nat = fields.Char(string="Numéro d'Identité Nationale ", required=True, tracking=True,)
    id_nat_import = fields.Binary(string="Joindre la piece d'identité")
    ai = fields.Char(string="Article d'Imposition",tracking=True,)
    ai_import = fields.Binary(string="Joindre l'AI")
    rc = fields.Char(string="Registre de Commerce",tracking=True,)
    rc_import = fields.Binary(string="Joindre le registre de Commerce")
    nif = fields.Char(string="NIF",tracking=True,)
    nif_import = fields.Binary(string="Joindre le NIF")
    nis = fields.Char(string="NIS",tracking=True,)
    nis_import = fields.Binary(string="Joindre le NIS")
    readonly_partner = fields.Boolean(default=False)

    _sql_constraints = [('id_nat',
                         'UNIQUE (id_nat)',
                         'ID number already exists'), ]

    # Removing constraint from leasing
    _sql_constraints = [('rc',
                         'Check(1=1)',
                         'RC Number already exists'), ]

    _sql_constraints = [('nif',
                         'Check(1=1)',
                         'NIF Number already exists'), ]

    _sql_constraints = [('ai',
                         'Check(1=1)',
                         'AI number already exists'), ]

    _sql_constraints = [('nis',
                         'Check(1=1)',
                         'NIS number already exists'), ]


    @api.onchange('id_nat')
    def check_id_nat_unicity(self):
        for rec in self:
            if rec.id_nat:
                same_id_nat = self.env['res.partner'].search([
                    ('id_nat', '=', rec.id_nat)])
                if len(rec.id_nat) != 18:
                    raise ValidationError(_('NIN doit être une suite de 18 caractères '))
                if same_id_nat:
                    raise ValidationError(_("Ce Numéro d'Identité Nationale exsite deja"))

    # @api.onchange('rc')
    # def check_rc(self):
    #     for rec in self:
    #         if rec.rc:
    #             same_rc = self.env['res.partner'].search([
    #                 ('rc', '=', rec.rc)])
    #             if same_rc:
    #                 raise ValidationError(_("Ce Registre de Commerce exsite deja"))
    #
    # @api.onchange('nif')
    # def check_nif(self):
    #     for rec in self:
    #         if rec.nif:
    #             same_nif = self.env['res.partner'].search([
    #                 ('nif', '=', rec.nif)])
    #             if same_nif:
    #                 raise ValidationError(_("Le Numero d'identification fiscale que vous avez introduit exsite deja"))
    #
    # @api.onchange('nis')
    # def check_rec(self):
    #     for rec in self:
    #         if rec.nis:
    #             same_nis = self.env['res.partner'].search([
    #                 ('nis', '=', rec.nis)])
    #             if same_nis:
    #                 raise ValidationError(_("Ce Numero d'identification à la Sécurité Sociale exsite deja"))
