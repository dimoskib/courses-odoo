# -*- coding: utf-8 -*-
{
    'name': 'Courses',
    'version': '1.1',
    'summary': 'Student Courses',
    'sequence': 10,
    'description': """Courses taken by the students.""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com/app/courses',
    'images': [],
    'depends': [
        'base',
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/course.xml',
        'views/teacher.xml',
        'views/student.xml',
        'views/grades.xml',
        # 'views/courses_chatter.xml',

        'report/report.xml',
        'report/course_card.xml',
        'report/student_card.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
