from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'secretkey'
app.secret_key = "some secret string"


class MyForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
	submit = SubmitField("Log In")


@app.route('/')
def index():
	return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
	form = MyForm()
	if form.validate_on_submit():
		if form.email.data == "admin@gmail.com" and form.password.data == "12345678":
			return render_template("success.html")
		else:
			return render_template("denied.html")
	return render_template("login.html", form=form)


if __name__ == '__main__':
	app.run(debug=True)
