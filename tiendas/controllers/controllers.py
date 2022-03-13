# -*- coding: utf-8 -*-
# from odoo import http


# class Tiendas(http.Controller):
#     @http.route('/tiendas/tiendas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tiendas/tiendas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tiendas.listing', {
#             'root': '/tiendas/tiendas',
#             'objects': http.request.env['tiendas.tiendas'].search([]),
#         })

#     @http.route('/tiendas/tiendas/objects/<model("tiendas.tiendas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tiendas.object', {
#             'object': obj
#         })
