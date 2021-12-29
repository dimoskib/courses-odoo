# -*- coding: utf-8 -*-
{
    'name': "Courses theme",
    'summary': """""",
    'description': """A theme for teachers in courses""",  # 'views/courses_chatter.xml',

    'author': "Bobo",
    'website': "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Theme/Creative',
    'version': '1.0',
    # any module necessary for this one to work correctly
    'depends': ['website'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/assets.xml',
        'views/layout.xml',
        'views/pages.xml',
        'views/snippets.xml',
        'views/options.xml',
        'views/sidebar.xml',
        'views/dynamic_snippet.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
