from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange

class AddPetForm(FlaskForm):
  name = StringField("Pet Name", validators=[InputRequired()])
  species = SelectField("Pet Species", validators=[InputRequired()])
  photo_url = StringField("Pet Photo", validators=[Optional()])
  age = IntegerField("Pet Age", validators=[Optional(), NumberRange(min=0, max=30)])
  notes = StringField("Notes", validators=[Optional()])
  available = BooleanField("Is available")