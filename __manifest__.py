{
	'name': 'Training Center System',
	'description': 'Simple module for training center.',
	'category': 'Training',
	'version': '1.0.0',
	'author': 'Test',
	'maintainer': 'test',
	'website': 'https://iaaaa.asd',
	'sequence': 150,
	'depends': [
		'base', 
		'web',
		'report',
	],
	'data': [
		'views/course_trainer_view.xml',
		'views/course_class_view.xml',
	],
	'qweb': [
	],
	'demo': [
	],
	'test': [
	],
	'auto_install': False,
	'installable': True,
}