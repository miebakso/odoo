from odoo import models, fields

class Trainer(models.Model):

	_name = 'training.center.trainer'
	_description = 'Master Trainer' 

	name = fields.Char('Trainer Name', size=40, required=True)
	gender = fields.Selection([
		('m','Male'),
		('f','Female')
		],'Gender', required=True)
	age = fields.Integer('Age', required=True)
	birth_date = fields.Date('Birth Date', required=True)
	address = fields.Char('Address', size=100, required=True)
	email = fields.Char('Email', size=50, required=True)
	phone = fields.Char('Phone Number', size=20, required=True)

	