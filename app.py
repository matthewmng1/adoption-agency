from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "booyahshaka"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page():
  pets = Pet.query.all()
  return render_template("home.html", pets=pets)

@app.route('/pets/new', methods=["GET", "POST"])
def add_pet():
  form = AddPetForm()
  pets = db.session.query(Pet.species)
  form.species.choices = [(p.species) for p in pets]

  if form.validate_on_submit():
    name = form.name.data
    species = form.species.data
    photo_url = form.photo_url.data
    age = form.age.data
    notes = form.notes.data
    available = form.available.data

    pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
    db.session.add(pet)
    db.session.commit()
    return redirect('/')
  else:
    return render_template("add_pet_form.html", form=form)

@app.route('/pets/edit/<int:id>', methods=["GET", "POST"])
def edit_pet(id):
  pet = Pet.query.get_or_404(id)
  form = AddPetForm(obj=pet)

  pets = db.session.query(Pet.species)
  form.species.choices = [(p.species) for p in pets]

  if form.validate_on_submit():
    pet.name = form.name.data
    pet.species = form.species.data
    pet.photo_url = form.photo_url.data
    pet.age = form.age.data
    pet.notes = form.notes.data
    pet.available = form.available.data

    db.session.commit()
    return redirect ('/')
  else:     
    return render_template('edit_pet_form.html', form=form)
# Make a page that shows some information about the pet:

# Name
# Species
# Photo, if present
# Age, if present
# It should also show a form that allows us to edit this pet:

# Photo URL
# Notes
# Available
# This should be at the URL /[pet-id-number]. Make the homepage link to this.