from odoo import api, fields, models, _


class ResCompany(models.Model):
    _inherit = "res.company"

    rc = fields.Char(string="Registre de Commerce", required=False, tracking=True,)
    nif = fields.Char(string="NIF", required=False, tracking=True,)
    ai = fields.Char(string="Article d'Imposition", required=False, tracking=True,)
    nis = fields.Char(string="NIS", required=False, tracking=True,)
