# -*- coding: utf-8 -*-
from odoo import models, fields, _


class HistoriqueAppels(models.Model):
    _name = 'crm.call.history'
    _description = 'CRM Call History'
    _order = "date_call desc"

    partner_id = fields.Many2one(
        "res.partner",
        string="Client",
        related="crm_id.partner_id",
        required=True
    )
    crm_id = fields.Many2one(
        "crm.lead",
        string="Tracking",
        required=True
    )
    partner_code_id = fields.Char(
        string="Code patient",
        related="partner_id.ref",
        readonly=True
    )
    date_call = fields.Date(
        string="Date du call",default=fields.Date.today
    )
    date_recup = fields.Date(
        string="Date de récuperation"
    )
    commentaire = fields.Text(
        string="Commentaire"
    )
    product_id = fields.Many2one(
        "product.product",
        string="Produit récupéré"
    )
    product_qty = fields.Float(
        string="Quantité récupérée"
    )
    pharmacie_id = fields.Many2one(
        "res.partner",
        string="Pharmacie",
        domain=[('is_company', '=', True)]
    )









