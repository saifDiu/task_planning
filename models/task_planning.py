from odoo import models, fields, api,_


class TaskPlanning(models.Model):
    _name = 'task.planning'
    _rec_name = 'task_name'

    task_name = fields.Char(string="Task Name", required=True)
    assigned_person = fields.Many2one('res.users',string="Assigned To",required=True)

    start_time = fields.Datetime(string="Start Date/Time")
    end_date_time = fields.Datetime(string="End Date/Time")

    initial_task_files = fields.Many2many('ir.attachment','initial_task_rel',string="Initial Files")

    upload_picture = fields.Many2many('ir.attachment','proof_task_files',string="Proof Files")

    task_state = fields.Selection([
        ('draft','Draft'),
        ('assigned','Assigned'),
        ('processing','Processing'),
        ('done','Done'),
    ],default='draft',string="State")

    task_details = fields.One2many('task.planning.line','task_id')

    def assigned_task(self):
        self.task_state = 'assigned'

    def mark_as_done(self):
        self.task_state = 'done'

    task_comments = fields.Text(string="Comments")

    def do_process(self):
        self.task_state = 'processing'


class TaskPlanningDetails(models.Model):
    _name = 'task.planning.line'

    task_id = fields.Many2one('task.planning')

    task_name = fields.Char(string="Name")
    task_details = fields.Char(string="Details")
    task_comment = fields.Text(string="Comment")
    task_location = fields.Char(string="Location")


