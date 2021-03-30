from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    height = db.Column(db.String(250), unique=True, nullable=False)
    mass = db.Column(db.String(250), unique=True, nullable=False)
    hair = db.Column(db.String(250), unique=True, nullable=False)
    gender = db.Column(db.String(250), unique=False, nullable=False)
    skin = db.Column(db.String(250), unique=True, nullable=False)
    eye = db.Column(db.String(250), unique=False, nullable=False)
    birth = db.Column(db.String(250), unique=True, nullable=False)

    def __repr__(self):
        return '<Character %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair": self.hair,
            "gender": self.gender,
            "skin": self.skin,
            "eye": self.eye,
            "birth": self.birth,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    population = db.Column(db.String(250), unique=False, nullable=False)
    terrain = db.Column(db.String(250), unique=False, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.planets

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            # do not serialize the password, its a security breach
        }

class FavoritesCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    character_id= db.Column(db.Integer, db.ForeignKey("Character.id"))

    def __repr__(self):
        return '<FavoritesCharacter %r>' % self.planets

    def serialize(self):
        return {
            "id": self.id,
            "username_id": self.username_id,
            "character_id": self.character_id,
            # do not serialize the password, its a security breach
        }

class FavoritesPlanet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    planet_id= db.Column(db.Integer, db.ForeignKey("Planets.id"))

    def __repr__(self):
        return '<FavoritesCharacter %r>' % self.planets

    def serialize(self):
        return {
            "id": self.id,
            "username_id": self.username_id,
            "planet_id": self.planet_id,
            # do not serialize the password, its a security breach
        }