# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _




class CustomLead2OpportunityPartner(models.TransientModel):
    _inherit = 'crm.lead2opportunity.partner'



    name = fields.Selection([
        ('convert', 'Convert to opportunity'),
        ('merge', 'Merge with existing opportunities')
    ], 'Conversion Action', readonly=True, store=True, default="convert")
    action = fields.Selection([
        ('create', 'Create a new customer'),
        ('exist', 'Link to an existing customer'),
        ('nothing', 'Do not link to a customer')
    ], string='Related Customer', readonly=True, store=True, default="nothing")

    user_id = fields.Many2one(
        'res.users', 'Salesperson',
        readonly=True, store=True, compute_sudo=False)
    team_id = fields.Many2one(
        'crm.team', 'Sales Team',
         readonly=True, store=True, compute_sudo=False)


