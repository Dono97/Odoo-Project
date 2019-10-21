# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import Warning

class Student(models.Model) :
    _name = 'student.user'
    _description = 'Student'
    student_number = fields.Char('Student Number', compute='compute_stu_num')
    first_name = fields.Char('First Name', required=True)
    last_name = fields.Char('Last Name', required=True)


    #Relationships
    program_student_id = fields.Many2one('program.course', string='Program')
    result_student_id = fields.One2many('result.module', 'student_result_id', string='Result')

    @api.multi
    def compute_stu_num(self):
        for rec in self:
            rec.student_number = '100' + str(rec.id)

            student_number = rec.student_number
