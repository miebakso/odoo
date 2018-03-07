import re

from odoo import http
from odoo.exceptions import ValidationError



# ==========================================================================================================================

class Academy(http.Controller):
	
	@http.route('/classes', auth='public')
	def index(self, **kw):
		mode = http.request.env['training.center.class']
		classes = mode.search([['state', '=', 'open']])
		return http.request.render('training_center.index', {
			'classes': classes
		})	