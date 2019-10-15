# -*- coding: utf-8 -*-
from odoo import http

# class ./admin(http.Controller):
#     @http.route('/./admin/./admin/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./admin/./admin/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('./admin.listing', {
#             'root': '/./admin/./admin',
#             'objects': http.request.env['./admin../admin'].search([]),
#         })

#     @http.route('/./admin/./admin/objects/<model("./admin../admin"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./admin.object', {
#             'object': obj
#         })