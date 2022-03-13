# -*- coding: utf-8 -*-
# from odoo import http


# class ProyectoOdooM(http.Controller):
#     @http.route('/proyecto_odoo_m/proyecto_odoo_m/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyecto_odoo_m/proyecto_odoo_m/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyecto_odoo_m.listing', {
#             'root': '/proyecto_odoo_m/proyecto_odoo_m',
#             'objects': http.request.env['proyecto_odoo_m.proyecto_odoo_m'].search([]),
#         })

#     @http.route('/proyecto_odoo_m/proyecto_odoo_m/objects/<model("proyecto_odoo_m.proyecto_odoo_m"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyecto_odoo_m.object', {
#             'object': obj
#         })
