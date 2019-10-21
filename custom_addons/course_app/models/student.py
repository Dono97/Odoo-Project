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
    transcript_student_id = fields. Many2one('transcript.student', compute='compute_transcript', inverse='transcript_inverse')
    transcript_student_ids = fields.One2many('transcript.student', 'student_transcript_id')


    @api.multi
    def compute_stu_num(self):
        for rec in self:
            rec.student_number = '100' + str(rec.id)

            student_number = rec.student_number

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
