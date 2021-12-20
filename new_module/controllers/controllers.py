# -*- coding: utf-8 -*-
import base64
from odoo import http


# from werkzeug.utils import redirect
#
# DEFAULT_IMAGE = '/new_module/static/src/img/material-background.png'
#


class AllCourses(http.Controller):

    @http.route('/my/courses', type='http', auth='public', website=True)
    def show_custom_page(self, **kw):
        courses = http.request.env['course.course'].search([])
        values = {
            'courses': courses,
        }
        return http.request.render('new_module.courses_page', values)


class AllTeachers(http.Controller):

    @http.route('/my/teachers', type='http', auth='public', website=True)
    def show_custom_page(self, **kw):
        teachers = http.request.env['course.teacher'].search([])
        values = {
            'teachers': teachers,
        }
        return http.request.render('new_module.teachers_page', values)


class AllStudents(http.Controller):

    @http.route('/my/students', type='http', auth='public', website=True)
    def show_custom_page(self, **kw):
        students = http.request.env['course.student'].search([])
        values = {
            'students': students,
        }
        return http.request.render('new_module.students_page', values)

#     @route(['/dashboard'], type='http', auth='user', website=False)
#     def dashboard(self, **post):
#         user = request.env.user
#         company = user.company_id
#         if company.dashboard_background:
#             image = base64.b64decode(company.dashboard_background)
#         else:
#             return redirect(DEFAULT_IMAGE)
#
#         return request.make_response(
#             image, [('Content-Type', 'image')])
