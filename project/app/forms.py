from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class LoginForm(FlaskForm):
    street = TextField('street', validators = [Required()])
    house = TextField('house', validators = [Required()])
    building = TextField('building', validators = [Required()])
    letter = TextField('letter', validators = [Required()])