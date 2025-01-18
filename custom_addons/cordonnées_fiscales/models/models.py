# -*- coding: utf-8 -*-

from odoo import models, fields, api
from num2words import num2words
from decimal import Decimal, getcontext, ROUND_HALF_UP


class AccountMouveInherit(models.Model):
    _inherit = 'account.move'

    total_en_lettres = fields.Char(string="Total en lettres", compute='_compute_total_en_lettres', store=True,
                                   readonly=True)

    @api.depends('amount_total', 'payment_reference')
    def _compute_total_en_lettres(self):
        for record in self:
            if record.amount_total:
                partie_entiere = int(record.amount_total)
                diff = Decimal(record.amount_total - partie_entiere)
                diff = diff.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                partie_decimale = int((diff) * 100)

                montant_en_mots = num2words(partie_entiere, lang='fr')
                montant_en_mots = montant_en_mots + " dinars"

                if partie_decimale > 0:
                    montant_en_mots += " et {} centimes".format(
                        num2words(partie_decimale, lang='fr'))

                record.total_en_lettres = montant_en_mots
            else:
                record.total_en_lettres = ""
