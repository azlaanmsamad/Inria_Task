from flask import render_template, url_for, flash, redirect, request, Blueprint
from app import db
from app.models import Name, Address, Email
from app.forms import UserForm, AddressForm, EmailForm

user = Blueprint('user', __name__)

@user.route("/register", methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        new_user = Name(first_name=form.firstname.data, last_name=form.lastname.data, middle_name=form.middlename.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('register.home'))
    return render_template('register.html', title='Register', form=form)

@user.route("/address", methods=['GET', 'POST'])
def address():
    form = AddressForm()
    if form.validate_on_submit():
        new_address = Address(address=form.address.data)
        db.session.add(new_address)
        db.session.commit()
        flash('Your address has been added.', 'success')


