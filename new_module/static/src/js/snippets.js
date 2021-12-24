odoo.define('course.dynamic.snippet', function (require) {
'use strict';
var publicWidget = require('web.public.widget');

publicWidget.registry.books = publicWidget.Widget.extend({
    selector: '.course_snippet',
    disabledInEditableMode: false,
    start: function () {
        var self = this;
        var rows = this.$el[0].dataset.numberOfCourses || '5';
        this.$el.find('td').parents('tr').remove();
        this._rpc({
            model: 'course.course',
            method: 'search_read',
            domain: [],
            fields: ['name', 'course_teacher_name', 'course_semester'],
            orderBy: [],
            limit: parseInt(rows)
            }).then(function (data) {
            _.each(data, function (course) {
                self.$el.append(
                    $('<tr />').append(
                        $('<td />').text(course.name),
                        $('<td />').text(course.course_teacher_name),
                        $('<td />').text(course.course_semester)
                    ));
            });
        });
    },
});
});