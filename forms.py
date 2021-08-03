from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, validators
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):
    name = StringField('Vardas', [validators.Length(min=4, max=25, message=('Min 4 simboliai')), DataRequired()])
    email = StringField('El.paštas', [validators.Length(min=6, max=35),
                                      DataRequired(),
                                      validators.Regexp("^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", message='Neteisingas el. pasto adresas')])
    message = TextAreaField('Jūsų pranešimas', [DataRequired(),
                                        Length(min=10,
                                        message=('Per trumpas tekstas. Min 10 simbolių'))])
    submit = SubmitField('Register')