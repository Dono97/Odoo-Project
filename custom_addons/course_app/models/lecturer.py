from odoo import fields, models

class Lecturer(models.Model):
    _name = 'lecturer.user'
    _description = 'Lecturer'
    first_name = fields.Char('First Name', required=True)
    last_name = fields.Char('Last Name', required=True)
    staff_number = fields.Char('Staff Number', required=True)
    office_number = fields.Char('Office Number', required=True)

#Relationships
    module_lecturer_id = fields.One2many('module.program', 'lecturer_module_id', string='Module')
#hello world
