# -*- coding: utf-8 -*-
# from odoo import http


# class FactureFiscale(http.Controller):
#     @http.route('/facture_fiscale/facture_fiscale', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/facture_fiscale/facture_fiscale/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('facture_fiscale.listing', {
#             'root': '/facture_fiscale/facture_fiscale',
#             'objects': http.request.env['facture_fiscale.facture_fiscale'].search([]),
#         })

#     @http.route('/facture_fiscale/facture_fiscale/objects/<model("facture_fiscale.facture_fiscale"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('facture_fiscale.object', {
#             'object': obj
#         })
