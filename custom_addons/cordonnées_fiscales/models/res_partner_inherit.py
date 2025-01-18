from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"


    ai = fields.Char(string="Article d'Imposition",tracking=True,)

    rc = fields.Char(string="Registre de Commerce",tracking=True,)

    nif = fields.Char(string="NIF",tracking=True,)

    nis = fields.Char(string="NIS",tracking=True,)




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
