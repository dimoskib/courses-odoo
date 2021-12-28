# -*- coding: utf-8 -*-
import base64
from odoo import http
from odoo.http import request


# from werkzeug.utils import redirect
#
# DEFAULT_IMAGE = '/new_module/static/src/img/material-background.png'
#


class AllCourses(http.Controller):

    @http.route('/my/courses', type='http', auth='public', website=True)
    def show_custom_page(self):
        courses = http.request.env['course.course'].search([])
        values = {
            'courses': courses,
        }
        return http.request.render('new_module.portal_all_courses', values)

    @http.route('/my/my_courses', type='http', auth='public', website=True)
    def show_my_courses(self):
        users_email = request.env.user.email
        student_id = http.request.env['course.student'].search([('student_email', '=', users_email)]).id
        # students_in_course = http.request.env['course.course'].search([('students_in_course', '=', student_id)])
        courses = http.request.env['course.course'].search([('students_in_course', '=', student_id)])
        values = {
            'courses': courses,
        }
        return http.request.render('new_module.portal_my_courses', values)

        # html_result = '<html><body><ul>'
        # for course in courses:
        #     if student_id in course.students_in_course.ids:
        #         html_result += "<li> <b>%s</b> </li>" % course.name
        #     else:
        #         html_result += "<li> %s </li>" % course.name
        # html_result += '</ul></body></html>'
        # return html_result


class AllTeachers(http.Controller):

    @http.route('/my/teachers', type='http', auth='public', website=True)
    def show_custom_page(self, **kw):
        teachers = http.request.env['course.teacher'].search([])
        values = {
            'teachers': teachers,
        }
        return http.request.render('new_module.portal_all_teachers', values)


class AllStudents(http.Controller):

    @http.route('/my/students', type='http', auth='public', website=True)
    def show_custom_page(self, **kw):
        students = http.request.env['course.student'].search([])
        values = {
            'students': students,
        }
        return http.request.render('new_module.portal_all_students', values)

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
