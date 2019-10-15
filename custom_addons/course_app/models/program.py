# -*- coding: utf-8 -*-
from odoo import fields, models

class Program(models.Model):
    _name = 'program.course'
    _description = 'Program'
    name = fields.Char('Program name', required=True)
    code = fields.Char('Program code', required=True)
    short_code = fields.Char('Shortened form', required=True)

    #Relationships
    student_program_id = fields.Many2many('student.user', string='Student')
    module_program_id = fields.One2many('module.program','program_module_id', string='Module')
