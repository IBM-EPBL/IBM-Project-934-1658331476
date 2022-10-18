from flask_wtf import Form
from wtforms import TextField, StringField, SubmitField, 

from wtforms import validators, ValidationError

class ContactForm(Form):
   username = TextField("User Name",[validators.Required("Please enter 
      your name.")]
   
   email = TextField("Email",[validators.Required("Please enter your email address."),
      validators.Email("Please enter your email address.")])
   
   number = StringField("Number")
   
   submit = SubmitField("Send")
