from app import db


class Name(db.Model):
    id = db.Model(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), unique=True, nullable=False)
    middle_name = db.Column(db.String(120), nullable=True)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.relationship('Email', backref='name', lazy=True)
    address = db.relationship('Address', backref='name', lazy=True)
    # backref is a way to create a new property of the Email class. age.name to get to the email of the person
    # lazy is how SQLAlchemy loads the data from the two tables

    def __repr__(self):
        return f"Name('{self.first_name}', '{self.middle_name}', '{self.last_name}')"


class Email(db.Model):
    id = db.Model(db.Integer, primary_key=True)
    email = db.Column(db.Integer, nullable=False, unique=False)
    person_id = db.Column(db.Integer, db.ForeignKey('name.id'), nullabel=False)

    def __repr__(self):
        return f"Email('{self.email}')"


class Address(db.Model):
    id = db.Model(db.Integer, primary_key=True)
    address = db.Model(db.String(120), nullable=False)
    person_id = db.Column(db.Integfer, db.ForeignKey('name.id'), nullable=False)

    def __repr__(self):
        return f"Address('{self.address}')"

