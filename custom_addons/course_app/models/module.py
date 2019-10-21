# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import Warning

class Module(models.Model):
    _name = 'module.program'
    _description = 'Module'
    name = fields.Char('Module name', required=True)
    year = fields.Char('Module year', required=True)
    code = fields.Char('Module code', compute='compute_module_code')

    #Relationships
    program_module_id = fields.Many2one('program.course', string='Program')
    result_module_id = fields.One2many('result.module','module_result_id', string='Result')
    lecturer_module_id = fields.Many2one('lecturer.user', string='Lecturer')
    transcript_module_id = fields.Many2one('transcript.student',string='Transcript')


    #@api.multi
    #def compute_module_code(self):
    #    self.ensure_one()
    #    self.code = self.name[:3] + self.year + "0"
    #    while self.code in self:
    #        self.code = self.name[:3] + self.year + str(int(self.code[-1])+1)
    #    return self.code.upper()


    @api.depends('name')
    def compute_module_code(self):
       for rec in self:

          nametest = str(rec.name)
          namevar = nametest[:3]
          codevar = str(rec.id)
          code = namevar.upper() + codevar

          rec.code = code
