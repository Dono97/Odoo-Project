# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import Warning

class Student(models.Model) :
    _name = 'student.user'
    _description = 'Student'
    # student_number = fields.Char('Student Number', compute='compute_stu_num', required=True)
    first_name = fields.Char('First Name', required=True)
    last_name = fields.Char('Last Name', required=True)


    #Relationships
    program_student_id = fields.Many2one('program.course', string='Program')
    result_student_id = fields.One2many('result.module', 'student_result_id', string='Result')

    @api.multi
    def compute_stu_num(self):
        self.ensure_one()
        self.student_number = '100'
