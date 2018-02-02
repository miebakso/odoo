import re

from odoo import models, fields, api
from odoo.exceptions import ValidationError

# ==========================================================================================================================

class Course(models.Model):
    _name = 'training.center.course'
    _description = 'Course master'

    name = fields.Char('Course Name', size=40, required=True)
    code = fields.Char('Course Code', size=10, required=True)
    course_desc = fields.Text('Course Description')
    syllabus_ids = fields.One2many('training.center.course.syllabus', 'course_id', 'Course Syllabuses')

    _sql_constraints = [
        ('unique_code', 'UNIQUE(code)', 'Course code must be unique.'),
        ('unique_name', 'UNIQUE(name)', 'Course name must be unique.'),
    ]

# ==========================================================================================================================

class Session(models.Model):
    _name = 'training.center.session'
    _description = 'Session master'

    date = fields.Date('Session Date', required=True)

# ==========================================================================================================================

class Syllabus(models.Model):
    _name = 'training.center.course.syllabus'
    _description = 'Course syllabus master'

    sequence = fields.Integer('Sequence', required=True)
    name = fields.Char('Syllabus Title', size=20, required=True)
    desc = fields.Text('Syllabus Description')
    duration = fields.Float('Syllabus Duration')
    course_id = fields.Many2one('training.center.course', 'Course')

    _sql_constraints = [
    	('unique_name_in_course', 'UNIQUE(name, course_id)', 'Title has already existed in this course.'),
    ]

    @api.constrains('duration')
    def _check_duration_value(self):
        for record in self:
            if record.duration >= 8 or record.duration <= 0.5:
                raise ValidationError('Duration must rage from 00:30  to 08:00')


# ==========================================================================================================================

class Trainer(models.Model):
    _name = 'training.center.trainer'
    _description = 'Trainer master'

    id_number = fields.Char('ID Number', size=16, required=True)
    name = fields.Char('Trainer Name', size=40, required=True)
    gender = fields.Selection([
        ('m', 'Male'),
        ('f', 'Female')
        ], 'Gender', required=True, default='m')
    age = fields.Integer('Age', required=True, default=10)
    birth_date = fields.Date('Birth Date', required=True)
    address = fields.Char('Address', size=100, required=True)
    email = fields.Char('E-mail', size=50, required=True)
    phone = fields.Char('Phone Number', size=20, required=True)

    _sql_constraints = [
        ('unique_email', 'UNIQUE(email)', 'E-mail must has already been used')
    ]

    @api.constrains('age')
    def _check_age_value(self):
        for record in self:
            if record.age < 10:
                raise ValidationError('Age must be greater or equal to 10')

    @api.constrains('id_number')
    def _check_id_number_value(self):
        for record in self:
            if len(record.id_number) != 16:
                raise ValidationError('The length of NIK number must be 16 digits')
            if not record.id_number.isdigit():
                raise ValidationError('NIK must be a number')

    @api.constrains('email')
    def _check_email_value(self):
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        for record in self:
            if not email_regex.match(record.email):
                raise ValidationError('E-mail is invalid')


    @api.constrains('phone')
    def _check_phone_value(self):
        for record in self:
            if not record.id_number.isdigit():
                raise ValidationError('Invalid Phone Number')



# ==========================================================================================================================

class Participant(models.Model):
    _name = 'training.center.participant'
    _description = 'Participant master'

    name = fields.Char('Participant Name' ,size=40, required=True)
    address = fields.Char('Participant Address', size=40, required=True)
    phone = fields.Integer('Participant Phone Number', required=True)
    email = fields.Char('Participant E-mail', size=50, required=True)
    birth_date = fields.Date('Participant Birth Date', required=True)

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
            if not record.id_number.isdigit():
                raise ValidationError('Invalid Phone Number')



