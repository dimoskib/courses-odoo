from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Grades(models.Model):
    _name = 'course.grades'
    _description = 'Grades'

    course = fields.Many2one(
        'course.course',
        string="Course",
        required=False,
        readonly=True)
    student = fields.Many2one(
        'course.student',
        string="Student",
        required=False,
        readonly=True)
    grade = fields.Selection([
        ("5", "5"), ("6", "6"),
        ("7", "7"), ("8", "8"),
        ("9", "9"), ("10", "10")],
        string="Grade",
        required=False)

    @api.constrains('student', 'course')
    def check_grade(self):
        for record in self:
            duplicate = self.env['course.grades'].search([
                ('student', '=', record.student.id),
                ('course', '=', record.course.id),
                ('id', '!=', record.id)])
            if duplicate:
                raise ValidationError('Student already have a grade')
