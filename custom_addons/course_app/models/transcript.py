from odoo import fields, models, api

class Transcript(models.Model):
    _name = 'transcript.student'
    _description = 'Transcript'


    #Relationships
    #result_transcript_id = fields.One2many('result.module','transcript_result_id', string='Result')
    #module_transcript_id = fields.One2many('module.program', 'transcript_module_id',string='Module')
    student_transcript_id  = fields.Many2one('student.user', string='Student')

    #Function that displays a students transcript 
    @api.multi
    def open_student_transcript(self):
        for rec in self:
            print(rec.student_transcript_id.id)
            student = self.env['student.user'].search([('id','=',rec.student_transcript_id.id)])
            return {
                'name': ('View transcript'),
                'domain': [('student_result_id', '=', student.id)],
                'view_type': 'form',
                'res_model': 'result.module',
                'view_id': False,
                'view_mode': 'tree,form',
                'type': 'ir.actions.act_window',
                }
