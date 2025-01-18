# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = "res.partner"
    _description = "Res Partner Sequences"

    # @api.model
    # def create(self, vals):
    #     vals['ref'] = self.env['ir.sequence'].next_by_code('res.partner') or '/'
    #     return super(ResPartner, self).create(vals)

    is_patient = fields.Boolean(string="Is Patient", default=False, help="Indicates whether the partner is a patient."
                                ,store=True)

    telecomercial = fields.Many2one(
        'res.users', string='Télécommercial',
        readonly=False, store=True,
        help='The second internal user in charge of this contact.')

    ref = fields.Char(string="Reference", compute="_compute_ref", store=True, readonly=False)
    sequence_id = fields.Char(string="Sequence", readonly=True,
                              default=lambda self: self.env['ir.sequence'].next_by_code('res.partner'))

    hospital_id = fields.Many2one(
        'utm.campaign', string='Hopital',
        readonly=False, store=True,
        help='Hopital du patient.')

    securite_id = fields.Many2one(
        'utm.source', string='Sécurité sociale',
        readonly=False, store=True,
        help='Sécurité sociale du patient.')

    date_of_birth = fields.Date(string='Date de naissance',
                                help='Date of birth of the patient')


# Créer une séquence pour le patient
    @api.depends('telecomercial')
    def _compute_ref(self):
        for record in self:
            telecomercial = record.telecomercial
            telecomercial_prefix = telecomercial.name[:3].upper() if telecomercial and telecomercial.name else ''
            record.ref = f"{telecomercial_prefix}/{record.sequence_id}"

    @api.model
    def create(self, vals):
        # Generate the sequence only on creation
        if not vals.get('sequence_id'):
            vals['sequence_id'] = self.env['ir.sequence'].next_by_code('res.partner') or '/'
        return super(ResPartner, self).create(vals)

    # @api.model
    # def create(self, vals):
    #     # Check for duplicate phone numbers
    #     if vals.get('phone'):
    #         existing_partner = self.search([('phone', '=', vals['phone'])], limit=1)
    #         if existing_partner:
    #             raise ValidationError(
    #                 f"Un partenaire avec le même numéro {vals['phone']} existe déja: {existing_partner.ref}."
    #             )
    #
    #     # Generate the sequence only on creation
    #     if not vals.get('sequence_id'):
    #         vals['sequence_id'] = self.env['ir.sequence'].next_by_code('res.partner') or '/'
    #
    #     return super(ResPartner, self).create(vals)

