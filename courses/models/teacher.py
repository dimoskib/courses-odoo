from odoo import api, fields, models


class CourseTeacher(models.Model):
    _name = "course.teacher"
    _description = "Teacher of the course"

    name = fields.Char(
        string='Teachers name',
        required=True)
    teacher_surname = fields.Char(
        string='Teachers surname',
        required=True)
    teacher_email = fields.Char(
        string='Teachers email',
        required=True)
    teacher_courses = fields.One2many(
        'course.course',
        'course_teacher_name',
        string="Courses",
        required=False,
        readonly=True)
