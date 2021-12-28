from odoo import api, fields, models
from datetime import datetime
from odoo.exceptions import ValidationError


class CourseStudent(models.Model):
    _name = "course.student"
    _description = "Student in the course"

    name = fields.Char(
        string='Name',
        required=True)
    student_surname = fields.Char(
        string='Surname',
        required=True)
    student_email = fields.Char(
        string='Email',
        required=True)
    student_birth_date = fields.Date(
        string='Date of birth',
        required=True)
    student_field_of_study = fields.Text(
        string="Field of study",
        required=True)
    student_enrolled_year = fields.Selection(
        [(str(year), str(year))
         for year in range(datetime.now().year - 20, datetime.now().year + 1)],
        string="Enrolled year",
        required=True)
    student_index_number = fields.Char(
        string="Index number",
        default="/",
        readonly=True)
    student_grades = fields.One2many(
        'course.grades',
        'student',
        string="Grades",
        required=False,
        readonly=True)
    course = fields.Many2many(
        'course.course',
        string='Courses'
    )
    student_access = fields.Many2one(
        'res.partner',
        string='Student access'
    )

    @api.constrains('student_enrolled_year', 'student_index_number')
    def _check_change_enrolled_year(self):
        for record in self:
            if record.student_index_number == '/':
                record.student_index_number = str(record.id) + "/" + record.student_enrolled_year
            else:
                index_number = record.student_index_number
                enrollment_year = record.student_enrolled_year
                if index_number.split('/')[1] != enrollment_year:
                    record.student_index_number = str(index_number.split('/')[0]) + '/' + enrollment_year

    @api.constrains('student_email')
    def check_student_email(self):
        for record in self:
            duplicate = self.env['course.student'].search([
                ('student_email', '=', record.student_email), ('id', '!=', record.id)])
            if duplicate:
                raise ValidationError(("%s : This email already exists." % record.student_email))

    def print_report(self):
        return self.env.ref('courses.report_student_card').report_action(self)
