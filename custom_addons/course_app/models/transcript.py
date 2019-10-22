from odoo import fields, models

class Transcript(models.Model):
    _name = 'transcript.student'
    _description = 'Transcript'


    #Relationships
    #result_transcript_id = fields.One2many('result.module','transcript_result_id', string='Result')
    #module_transcript_id = fields.One2many('module.program', 'transcript_module_id',string='Module')
    student_transcript_id  = fields.Many2one('student.user', string='Student')
