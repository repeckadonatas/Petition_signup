from flask import Flask, render_template, request
from forms import ContactForm
import os
from app import db, Peticijos, app

db.create_all()

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = ContactForm()
    if form.validate_on_submit():
        peticija = Peticijos(form.name, form.email, form.message)
        db.session.add(peticija)
        db.session.commit()
        return render_template('register_success.html', form=form)
    return render_template('register.html', form=form)


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)