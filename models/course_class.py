import re

from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import ValidationError
from datetime import datetime, time, timedelta

# ==========================================================================================================================

class CourseClass(models.Model):
	_name = 'training.center.class'
	_description = 'Opened training classes'

	course_id = fields.Many2one('training.center.course','Course', required=True, ondelete="restrict")
	open_date = fields.Date('Open Date', required=True)
	start_date = fields.Date('Start Date', readonly=True)
	finish_date = fields.Date('Finished Date', readonly=True)
	trainer_id = fields.Many2one('training.center.trainer','Trainer', ondelete="restrict")
	state = fields.Selection((
		('draft','Draft'),
		('open','Open'),
		('ongoing','Ongoing'),
		('done','Done'),
		('canceled','Canceled')
		), 'state', default="draft")
	session_ids = fields.One2many('training.center.class.session','class_id','Sessions')
	participant_ids = fields.One2many('training.center.class.participant','class_id','Participant')
	capacity = fields.Integer('Capacity', required=True)

	_sql_constraints = {
		('check_capacity','CHECK(capacity > 0)','Capacity must be more than zero.'),
	}

	@api.onchange('course_id')
	def onchange_course_id(self):
	# otomatis isi session berdasarkan silabus course
		sessions = []
		for session in self.course_id.syllabus_ids:
			sessions.append([0,False,{
				'sequence': session.sequence,
				'name': session.name,
				'desc': session.desc,
				'duration': session.duration,
				}])
		self.session_ids = sessions

	# batasi pilihan trainer
	
		trainer_ids = []
		for trainer in self.course_id.trainer_ids:
			trainer_ids.append(trainer.trainer_id.id)
		domain = [('id','in',trainer_ids)]
		return {
			'domain': {
				'trainer_id': domain,
			}
		}
# ==========================================================================================================================

class ClassSession(models.Model):
	_name = 'training.center.class.session'
	_description = 'Class sessions'

	class_id = fields.Many2one('training.center.class', 'Class', ondelete="cascade")
	sequence = fields.Integer('Sequence', required=True)
	name = fields.Char('Syllabus Title', size=20, required=True)
	desc = fields.Text('Syllabus Description')
	duration = fields.Float('Syllabus Duration')
	session_start = fields.Datetime('Session Start', required=True)
	session_end = fields.Datetime('Session End', required=True)

	@api.onchange('duration','session_start')
	def onchange_duration_start(self):
		if not (self.session_start and self.duration): return
		session_start = datetime.strptime(self.session_start, DEFAULT_SERVER_DATETIME_FORMAT)
		session_end = session_start + timedelta(hours=self.duration)
		self.session_end = session_end.strftime(DEFAULT_SERVER_DATETIME_FORMAT)


# ==========================================================================================================================


class Participant(models.Model):
	_name = 'training.center.participant'
	_description = 'Participant master'

	name = fields.Char('Participant Name' ,size=40, required=True)
	address = fields.Char('Participant Address', size=40, required=True)
	phone = fields.Char('Participant Phone Number', size = 20, required=True)
	email = fields.Char('Participant E-mail', size=50, required=True)
	birth_date = fields.Date('Participant Birth Date', required=True)
	par_id = fields.Char('Participant id ', size=9, readonly=True)

	_sql_constraints = [
		('unique_email','UNIQUE(email)','Email has already been used.')
	]

	@api.constrains('email')
	def _check_email_value(self):

		email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
		for record in self:
			if not email_regex.match(record.email):
				raise ValidationError('E-mail is invalid')

	@api.constrains('phone')
	def _check_phone_value(self):
		for record in self:
			if not record.phone.isdigit():
				raise ValidationError('Invalid Phone Number')

	@api.model
	def create(self, vals):
		#isikan nomor urut peserta secara otomatis
		year = datetime.datetime.now().strftime("%Y")
		latest_par = self.search([('par_id','like',year)], order="par_id DESC", limit = 1)
		if len(latest_par) == 0:
			new_id = "%s00001" % (year)
		else:
			latest_id = latest_par.par_id
			new_id = str(int(latest_id)+1)
		vals['par_id'] = new_id
		return super(Participant, self).create(vals)

	"""
	@api.one
	def _compute_id(self):
		year = datetime.datetime.now().strftime("%Y")
		template = year+"00000"
		par_id = int (template)+self.id
		# self.write('par_id': par_id) 
		self.par_id = par_id
	"""


# ==========================================================================================================================

class ClasslassParticipant(models.Model):
	_name = 'training.center.class.participant'
	_description = 'Class participant'

	class_id = fields.Many2one('training.center.class', 'Class', ondelete="cascade")
	participant_id = fields.Many2one('training.center.participant','Participant', ondelete="cascade")