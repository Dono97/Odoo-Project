from odoo import fields, models, api
from random import randint           #import 'random' module / generates random 5 digit number

class Lecturer(models.Model):
    _name = 'lecturer.user'
    _description = 'Lecturer'
    first_name = fields.Char('First Name', required=True)
    last_name = fields.Char('Last Name', required=True)
    office_number = fields.Char('Office Number', required=True)
    staff_number = fields.Char('Staff Number', compute='compute_staff_num', store=True)
    image = fields.Binary('Cover')
    name = fields.Char('Name', compute='computer_name')


#Relationships
    module_lecturer_id = fields.One2many('module.program', 'lecturer_module_id', string='Module')

    @api.depends('staff_number')
    def computer_name(self):
        for rec in self:
            rec.name = rec.staff_number

    @api.multi
    def five_digits(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint (range_start, range_end)

    @api.depends('first_name')
    def compute_staff_num(self):
        range_1 = ['A', 'B', 'C', 'D', 'E']
        range_2 = ['F', 'G', 'H', 'I', 'J']
        range_3 = ['K', 'L', 'M', 'N', 'O']
        range_4 = ['P', 'Q', 'R', 'S', 'T']
        set_1 = '100'
        set_2 = '111'
        set_3 = '122'
        set_4 = '133'
        set_5 = '144'
        for rec in self:
            test = str(rec.first_name)
            if test[0] in range_1[0:4]:
                staff_number = set_1 + str(self.five_digits(5))
            elif test[0] in range_2[0:4]:
                staff_number = set_2 + str(self.five_digits(5))
            elif test[0] in range_3[0:4]:
                staff_number = set_3 + str(self.five_digits(5))
            elif test[0] in range_4[0:4]:
                staff_number = set_4 + str(self.five_digits(5))
            else:
                staff_number = set_5 + str(self.five_digits(5))

            rec.staff_number = staff_number
            return rec.staff_number



    @api.multi
    def add_lecturer(self):
        new_user = self.env['res.users'].create({
            'name':self.first_name,
            'login':self.first_name,
            'new_password':self.staff_number,
        })
        lecturer_group_security = self.env['res.groups'].search([('name', '=', 'Lecturer')])
        new_user.groups_id = lecturer_group_security
