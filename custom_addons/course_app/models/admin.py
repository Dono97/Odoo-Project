# -*- coding: utf-8 -*-
from odoo import fields, models

class Admin(models.Model) :
    _name = 'admin.user'
    _description = 'Admin'
    first_name = fields.Char('First Name', required=True)
    last_name = fields.Char('Last Name', required=True)
    staff_number = fields.Char('Staff Number', required=True)
    office_number = fields.Char('Office Number', required=True)
