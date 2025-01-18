# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models



class CustomHosipital(models.Model):
        _inherit = 'utm.campaign'

        wilaya = fields.Many2one(
            'res.country.state',
            string="Wilaya de l'Hopital",
            domain="[('country_id.name', '=', 'Algérie')]",
            help='Wilaya de l"Hopital'
        )

        partner_ids = fields.One2many(
            'res.partner',  # Related model
            'hospital_id',  # Field in `res.partner` that links to `utm.campaign`
            string='Linked Partners',
            help='List of partners linked to this hospital.'
        )


