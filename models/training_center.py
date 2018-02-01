from odoo import models, fields

# ==========================================================================================================================

class Course(models.Model):
    _name = 'training.center.course'
    _description = 'Course master'

    name = fields.Char('Course Name', size=40, required=True)
    code = fields.Char('Course Code', size=10, required=True)
    course_desc = fields.Text('Course Description')
    syllabus_ids = fields.One2many('training.center.syllabus', 'course_id', 'Course Syllabuses')

    _sql_constraints = [
        ('unique_code', 'UNIQUE(code)', 'Course code must be unique.'),
    ]

# ==========================================================================================================================

class Session(models.Model):
    _name = 'training.center.session'
    _description = 'Session master'

    date = fields.Date('Session Date', required=True)

# ==========================================================================================================================

class Syllabus(models.Model):
    _name = 'training.center.syllabus'
    _description = 'Course syllabus master'

    sequences = fields.Integer('Sequence', required=True)
    name = fields.Char('Syllabus Name', size=20, required=True)
    desc = fields.Text('Syllabus Description')
    duration = fields.Float('Syllabus Duration')
    course_id = fields.Many2one('training.center.course', 'Course')

# ==========================================================================================================================

class Trainer(models.Model):
    _name = 'training.center.trainer'
    _description = 'Trainer master'

    name = fields.Char('Trainer Name', size=40, required=True)
    gender = fields.Selection([
        ('m', 'male'),
        ('f', 'female')
        ], 'Gender', required=True)
    age = fields.Integer('Age', required=True)
    birth_date = fields.Date('Birth Date', required=True)
    address = fields.Char('Address', size=100, required=True)
    email = fields.Char('E-mail', size=50, required=True)
    phone = fields.Char('Phone Number', size=20, required=True)

# ==========================================================================================================================

class Participant(models.Model):
    _name = 'training.center.participant'
    _description = 'Participant master'

    name = fields.Char('Participant Name' ,size=40, required=True)
    address = fields.Char('Participant Address', size=40, required=True)
	phone = fields.Char('Participant Phone Number', size=30, required=True)
	email = fields.Char('Participant E-mail', size=50, required=True)
	birth_date = fields.Date('Participant Birth Date', required=True)