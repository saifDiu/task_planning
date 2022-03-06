from odoo import models, fields, api,_


class TaskPlanning(models.Model):
    _name = 'task.planning'
    _rec_name = 'task_name'

    task_name = fields.Char(string="Task Name", required=True)
    assigned_person = fields.Many2one('res.users',string="Assigned To",required=True)

    start_time = fields.Datetime(string="Start Date/Time")
    end_date_time = fields.Datetime(string="End Date/Time")

    upload_picture = fields.Many2many('ir.attachment',string="Task Files")

    task_state = fields.Selection([
        ('draft','Draft'),
        ('assigned','Assigned'),
        ('done','Done')
    ],default='draft',string="State")

    task_details = fields.One2many('task.planning.line','task_id')

    def assigned_task(self):
        self.task_state = 'assigned'

    def mark_as_done(self):
        self.task_state = 'done'


class TaskPlanningDetails(models.Model):
    _name = 'task.planning.line'

    task_id = fields.Many2one('task.planning')

    task_name = fields.Char(string="Name")
    task_details = fields.Char(string="Details")

