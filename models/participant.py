from odoo import models, fields

class Participant(models.Model):

	_name = 'training.center.participant'
	_description = 'Master participant'

	name = fields.Char('Participant Name', size=40, required=True)
	address = fields.Char('Address', size=40, required=True)
	phone = fields.Char('Phone Number', size=30, required=True)
	email = fields.Char('Email', size=50, required=True)
	birth_date = fields.Date('Birth Date', required=True)

	_sql_constraints = [
		('unique_code','UNIQUE(email)','Email has already existed.'),
	]
