from odoo import models, fields

class Course(models.Model):

	_name = 'training.center.course'
	_description = 'Master course'

	name = fields.Char('Course Name', size=40, required=True)
	code = fields.Char('Code', size=10, required=True)
	course_desc = fields.Text('Description')
	syllabus_ids = fields.One2many('training.center.syllabus', 'course_id', 'Syllabuses')

	_sql_constraints = [
		('unique_code','UNIQUE(code)','Course code must be unique.'),
	]

