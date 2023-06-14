from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,RadioField,SelectField,TextAreaField,SubmitField)
from wtforms.validators import DataRequired

def to_int(s):

    return int(s)


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    activity = StringField('Login',validators=[DataRequired()])
    activity2 = StringField('password',validators=[DataRequired()])
    submit = SubmitField('Submit')
    login="fsfs"
    password="1234"


@app.route('/', methods=['GET', 'POST'])
def index():

    # Create instance of the form.
    form = InfoForm()

    session['activity'] = form.activity.data
    session['activity2'] = form.activity2.data
    if form.validate_on_submit():
        if session['activity'] == form.login and session['activity2'] == form.password:
            return redirect(url_for("thankyou"))

        else:
            return redirect(url_for("fail"))


    return render_template('home.html', form=form)




@app.route('/thankyou')
def thankyou():

    return render_template('01-thankyou.html')

@app.route('/fail')
def fail():

    return render_template('failure.html')


if __name__ == '__main__':
    app.run(debug=True)