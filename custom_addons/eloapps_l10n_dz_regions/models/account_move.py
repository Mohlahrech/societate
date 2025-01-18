from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = "account.move"

    partner_state = fields.Char(
        string="Wilaya",
        related="partner_id.state_id.name",
        store=True,
        readonly=True
    )

    telecomercial = fields.Char(
        string="Télé-commercial",
        related="partner_id.telecomercial.name",
        store=True,
        readonly=True
    )
