from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Course(models.Model):
    _name = "course.course"
    _inherit = "mail.thread"
    _description = "Course name"

    name = fields.Char(
        string='Course name',
        required=True)
    course_field_of_study = fields.Text(
        string="Field of study",
        required=True)
    course_teacher_name = fields.Many2one(
        "course.teacher",
        string="Teacher of this course",
        required=False)
    course_semester = fields.Selection(
        [('First semester', '1'),
         ('Second semester', '2'),
         ('Third semester', '3'),
         ('Fourth semester', '4'),
         ('Fifth semester', '5'),
         ('Sixth semester', '6'),
         ('Seventh semester', '7'),
         ('Eight semester', '8')],
        string="Semester",
        required=True)
    state = fields.Selection(
        [('draft', 'Draft'),
         ('open', 'Open'),
         ('finished', 'Finished')],
        string="Status",
        default='draft',
        readonly=True,
        required=True)
    course_start_date = fields.Date(
        string='Beginning date',
        required=True)
    course_end_date = fields.Date(
        string='End date',
        required=True)
    course_description = fields.Text(
        string='Description',
        translate=True)
    number_students_in_course = fields.Integer(
        string="Number of students")
    course_file = fields.Many2many(
        'ir.attachment',
        'class_ir_attachments_rel',
        'class_id',
        'attachment_id',
        string="Course material",
        required=False)
    student_grades = fields.One2many(
        'course.grades',
        'course',
        string="Grades",
        required=False)
    students_in_course = fields.Many2many(
        'course.student',
        string="Students in the course",
        required=False)

    @api.constrains("students_in_course")
    def number_of_students(self):
        for record in self:
            record.number_students_in_course = len(record.students_in_course)

            student_grades = record.env["course.grades"].search([('course', '=', record.id)])

            for i in range(0, len(student_grades)):
                flag = False
                for j in range(0, len(record.students_in_course)):
                    if student_grades[i].student.id == record.students_in_course[j].id:
                        flag = True
                        break

                if not flag:
                    student_grades[i].unlink()

            for i in range(0, len(record.students_in_course)):
                obj = record.env["course.grades"].search([
                    ('course', '=', record.id),
                    ('student', '=', record.students_in_course[i].id)
                ])

                if not obj:
                    record.env["course.grades"].create({
                        'course': record.id,
                        'student': record.students_in_course[i].id
                    })

    def insert_grades(self):
        for record in self:
            form_name = ""
            if record.state == "open":
                form_name = "Insert Grades"
            elif record.state == "finished":
                form_name = "View Grades"
            view_id = record.env.ref('courses.insert_grades_form').id
            context = record._context.copy()
            return {
                'name': form_name,
                'view_type': 'form',
                'view_mode': 'tree',
                'views': [(view_id, 'form')],
                'res_model': 'course.course',
                'view_id': view_id,
                'type': 'ir.actions.act_window',
                'res_id': record.id,
                'target': 'new',
                'context': context,
            }

    def copy_course(self, default=None):

        for record in self:

            if record.state == "finished":
                default = dict(default or {})
                default.update({
                    'students_in_course': None,
                    'student_grades': None,
                    'state': 'draft',
                    'number_students_in_course': None,
                })
                copy = super(Course, record).copy(default)
                view_id = record.env.ref('courses.course_view_form').id

                return {
                    'name': 'form_name',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'course.course',
                    'view_id': view_id,
                    'type': 'ir.actions.act_window',
                    'res_id': copy.id,
                    'target': 'current'
                }

            else:
                raise ValidationError(_("The state has to be finished in order to make a copy of the course."))

    def action_draft(self):
        for record in self:
            if record.state == "open" or record.state == "finished":
                record.state = "draft"
            else:
                raise ValidationError(_(
                    "%s course has to be in open state in order to change the state to Draft." % record.name))

    def action_open(self):
        for record in self:
            record.state = "open"

    def action_finished(self):
        for record in self:
            if record.state != "open":
                raise ValidationError(_("The action has to be in open state to change the state to finish."))
            student_grades = record.env["course.grades"].search([('course', '=', record.id)])
            assigned_grades = 0
            for i in range(0, len(student_grades)):
                if student_grades[i].grade:
                    assigned_grades += 1
            if record.state == "open" and len(student_grades) == assigned_grades:
                record.state = "finished"
            else:
                raise ValidationError(_("You have not assigned a grade for every student."))

    @api.constrains('name')
    def check_name(self):
        for record in self:
            duplicate = self.env['course.course'].search([('name', '=', record.name), ('id', '!=', record.id)])
            if duplicate:
                raise ValidationError(_("%s course already exists." % record.name))

    @api.constrains('course_start_date', 'course_end_date')
    def check_date(self):
        for record in self:
            if (record.course_end_date - record.course_start_date).total_seconds() < 0:
                raise ValidationError(_("The end date of %s course cannot be before the start date." % record.name))

    def print_report(self):
        return self.env.ref('courses.report_course_card').report_action(self)
