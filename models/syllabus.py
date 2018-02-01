from odoo import models, fields

class Syllabus(models.Model):

	_name = 'training.center.syllabus'
	_description = 'Master syllabus' 

	sequence = fields.Integer('Sequence', required=True)
	name = fields.Char('Title', size=40, required=True)
	duration = fields.Float('Duration', required=True)
	desc = fields.Text('Description', required=True)
	course_id = fields.Many2one('training.center.course', 'Course')
	