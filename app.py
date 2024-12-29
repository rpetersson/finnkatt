import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_googlemaps import GoogleMaps, Map
from forms import RegisterCatForm
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ensure the data directory exists
if not os.path.exists('data'):
    os.makedirs('data')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
# you can set key as config

# Initialize the extension
GoogleMaps(app, key=os.getenv('GOOGLEMAPS_KEY'))

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    breed = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)  # New column for address

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'date_of_birth': self.date_of_birth.isoformat(),
            'breed': self.breed,
            'address': self.address
        }

@app.route('/')
def home():
    return render_template('base.html', googlemaps_key=os.getenv('GOOGLEMAPS_KEY'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterCatForm()
    if form.validate_on_submit():
        cat = Cat(name=form.name.data, date_of_birth=form.date_of_birth.data, breed=form.breed.data, address=form.address.data)
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html', form=form, googlemaps_key=os.getenv('GOOGLEMAPS_KEY'))

if __name__ == '__main__':
    app.run(debug=True)
