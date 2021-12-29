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
        courses = http.request.env['course.course'].search([('students_in_course', '=', student_id)])
        values = {
            'courses': courses,
        }
        return http.request.render('new_module.portal_my_courses', values)


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

    @http.route('/my/my_students', type='http', auth='public', website=True)
    def show_custom_page(self, **kw):
        users_email = request.env.user.email
        teacher_id = http.request.env['course.teacher'].search([('teacher_email', '=', users_email)]).id
        my_courses = http.request.env['course.course'].search([('course_teacher_name', '=', teacher_id)])
        students = http.request.env['course.student'].search([])
        values = {
            'students': students,
        }
        return http.request.render('new_module.portal_my_students', values)

