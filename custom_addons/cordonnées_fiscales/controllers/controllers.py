# -*- coding: utf-8 -*-
# from odoo import http


# class Hci(http.Controller):
#     @http.route('/hci/hci', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hci/hci/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hci.listing', {
#             'root': '/hci/hci',
#             'objects': http.request.env['hci.hci'].search([]),
#         })

#     @http.route('/hci/hci/objects/<model("hci.hci"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hci.object', {
#             'object': obj
#         })
