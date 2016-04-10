from flask_wtf import Form
from wtforms import TextField, TextAreaField, PasswordField, BooleanField, SelectField, FileField, SubmitField, validators
from wtforms.validators import Required

class SignUpForm(Form):
    uploadedfile = FileField("Upload A Picture")
    firstname = TextField("FirstName",[validators.Required()])
    lastname = TextField("LastName",[validators.Required()])
    address = TextField("Address",[validators.Required()])
    email = TextField("Email",[validators.Required()])
    password = PasswordField("Password",[validators.Required()])
    phonenumber = TextField("Phone Number",[validators.Required()])
    dob = TextField("Date Of Birth",[validators.Required()])
    submit = SubmitField("Submit")
