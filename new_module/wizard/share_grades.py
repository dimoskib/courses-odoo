from odoo import models, fields, api


class ShareGradesWizard(models.TransientModel):
    _name = 'share.grades.wizard'
    _description = "Share student's grades"

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
    grade = fields.Many2one(
        'course.grades',
        string="Grade",
        required=False,
        readonly=True)
    description = fields.Text(
        string="Description", )

    def send_sms(self):
        print("The SMS was shared")
