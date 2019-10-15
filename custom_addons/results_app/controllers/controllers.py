# -*- coding: utf-8 -*-
from odoo import http

# class ./academicStaff(http.Controller):
#     @http.route('/./academic_staff/./academic_staff/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./academic_staff/./academic_staff/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('./academic_staff.listing', {
#             'root': '/./academic_staff/./academic_staff',
#             'objects': http.request.env['./academic_staff../academic_staff'].search([]),
#         })

#     @http.route('/./academic_staff/./academic_staff/objects/<model("./academic_staff../academic_staff"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./academic_staff.object', {
#             'object': obj
#         })