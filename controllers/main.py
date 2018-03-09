import re

from odoo import http
from odoo.exceptions import ValidationError



# ==========================================================================================================================

class Academy(http.Controller):
	
	@http.route('/classes', auth='public')
	def index(self):
		mode = http.request.env['training.center.class']
		classes = mode.search([['state', '=', 'open']])
		return http.request.render('training_center.index', {
			'classes': classes
		})

	@http.route('/classes/register/<int:id>', auth='public')
	def form(self, id):
		mode = http.request.env['training.center.class']
		classes = mode.search([['state', '=', 'open']])
		return http.request.render('training_center.form', {
			'classes': classes, 'id': id
		})

	@http.route('/classes/register', auth='public')
	def form_empty(self):
		mode = http.request.env['training.center.class']
		classes = mode.search([['state', '=', 'open']])
		return http.request.render('training_center.form', {
			'classes': classes, 'id': -1
		})
