from odoo import models, fields

class Session(models.Model):

	_name = 'training.center.session'
	_description = 'Master Session' 

	code = fields.Char('Class code', size=20, required=True)
	desc = fields.Text('Description')
	capacity = fields.Integer('capacity', required=True)
	date = fields.Date('Date', required=True)
	start_time = fields.Float('Start Time', required=True)
	duration = fields.Integer('duration', required=True)

	