from flask_wtf import Flaskform
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class DepartmentForm(Flaskform):
	"""
	Form for admin to add or delete a department
	"""
	name = StringField('Name', validators=[DataRequired()])
	description = StringField('Description', validators=[DataRequired()])
	submit = SubmitField('Submit')

