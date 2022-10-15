import pdb
from flask import render_template, url_for, redirect, flash, request
from flaskapp import app
from flaskapp.forms import UserForm, AddressForm
from flaskapp.models import Name, Email, Address
from flaskapp import db


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        # Creating a Name object for the database
        new_user = Name(name=form.name.data)
        # Adding the object
        db.session.add(new_user)
        # Committing the new user object to the database
        db.session.commit()
        flash(f'Data for {form.name.data} has been created', 'success')
        return redirect(url_for('register'))
    return render_template('register.html', form=form)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/database", methods=['GET'])
def display_from_db():
    users = Name.query.order_by(Name.date_posted.desc())[:5]
    return render_template('display_db.html', users=users)


@app.route("/clear", methods=['GET'])
def clear():

    Name.query.delete()
    db.session.commit()
    return redirect(url_for('home'))