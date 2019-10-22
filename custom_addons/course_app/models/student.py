# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import Warning
from random import randint                      #import 'random' module / generates random 5 digit number

class Student(models.Model) :
    _name = 'student.user'
    _description = 'Student'
    student_number = fields.Char('Student Number', compute='compute_stu_num', store=True)
    first_name = fields.Char('First Name', required=True)
    last_name = fields.Char('Last Name', required=True)
    image = fields.Binary('Cover')
    name = fields.Char('Name', compute='computer_name')

    #Relationships
    program_student_id = fields.Many2one('program.course', string='Program')
    result_student_id = fields.One2many('result.module', 'student_result_id', string='Result')
    transcript_student_id = fields. Many2one('transcript.student', compute='compute_transcript', inverse='transcript_inverse')
    transcript_student_ids = fields.One2many('transcript.student', 'student_transcript_id')

    @api.depends('student_number')
    def computer_name(self):
        for rec in self:
            rec.name = rec.student_number


    @api.multi
    def five_digits(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint (range_start, range_end)

    @api.depends('first_name')
    def compute_stu_num(self):
        range_1 = ['A', 'B', 'C', 'D', 'E']
        range_2 = ['F', 'G', 'H', 'I', 'J']
        range_3 = ['K', 'L', 'M', 'N', 'O']
        range_4 = ['P', 'Q', 'R', 'S', 'T']
        set_1 = '200'
        set_2 = '211'
        set_3 = '222'
        set_4 = '233'
        set_5 = '244'
        for rec in self:
            test = str(rec.first_name)
            if test[0] in range_1[0:4]:
                student_number = set_1 + str(self.five_digits(5))
            elif test[0] in range_2[0:4]:
                student_number = set_2 + str(self.five_digits(5))
            elif test[0] in range_3[0:4]:
                student_number = set_3 + str(self.five_digits(5))
            elif test[0] in range_4[0:4]:
                student_number = set_4 + str(self.five_digits(5))
            else:
                student_number = set_5 + str(self.five_digits(5))

            rec.student_number = student_number

    @api.one
    @api.depends('transcript_student_ids')
    def compute_transcript(self):
        if len(self.transcript_student_ids) > 0:
            self.transcript_student_id = self.transcript_student_ids[0]

    @api.one
    def transcript_inverse(self):
        if len(self.transcript_student_ids) > 0:
            # delete previous reference
            asset = self.env['transcript.student'].browse(self.transcript_student_ids[0].id)
            asset.student_transcript_id = False
        # set new reference
        self.transcript_student_id.student_transcript_id = self
