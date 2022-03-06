# -*- coding: utf-8 -*-
# from odoo import http


# class TaskPlanning(http.Controller):
#     @http.route('/task_planning/task_planning/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/task_planning/task_planning/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('task_planning.listing', {
#             'root': '/task_planning/task_planning',
#             'objects': http.request.env['task_planning.task_planning'].search([]),
#         })

#     @http.route('/task_planning/task_planning/objects/<model("task_planning.task_planning"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('task_planning.object', {
#             'object': obj
#         })
