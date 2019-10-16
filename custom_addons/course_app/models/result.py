from odoo import fields, models

class Result(models.Model):
    _name = 'result.module'
    _description = 'Result'
    value = fields.Integer('Result Value', required=True)

    #Relationships
    # module_result_id = fields.Many2one('module.program', string='Module')
    student_result_id = fields.Many2one('student.user', string='Student')
    transcript_result_id = fields.Many2one('transcript.student', string='Transcript')
    
