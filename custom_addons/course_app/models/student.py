# -*- coding: utf-8 -*-
from odoo import fields, models

class Student(models.Model) :
    _name = 'student.user'
    _description = 'Student'
    student_number = fields.Char('Student Number', compute='_compute_stu_num',required=True)
    first_name = fields.Char('First Name', required=True)
    last_name = fields.Char('Last Name', required=True)

    #Relationships
    program_student_id = fields.Many2many('program.course', string='Program')
    result_student_id = fields.One2many('result.module', 'student_result_id', string='Result')

    #@api.multi
    #def _compute_stu_num(self):
        #pass
