# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Program(models.Model):
    _name = 'program.course'
    _description = 'Program'
    name = fields.Char('Program name', required=True)
    code = fields.Char('Program code', required=True)
    _sql_constraints = [('code', 'UNIQUE (code)', 'Program code already exists!')]

    #Relationships
    student_program_id = fields.One2many('student.user', 'program_student_id', string='Student')
    module_program_id = fields.One2many('module.program','program_module_id', string='Module')
