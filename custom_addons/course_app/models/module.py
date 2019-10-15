# -*- coding: utf-8 -*-
from odoo import fields, models

class Module(models.Model):
    _name = 'module.program'
    _description = 'Module'
    name = fields.Char('Module name', required=True)
    code = fields.Char('Module code', required=True)

    #Relationships
    program_module_id = fields.Many2one('program.course', string='Program')
    #result_module_id = fields.One2many('result.module', string='Result')
    lecturer_module_id = fields.Many2one('lecturer.user', string='Lecturer')
