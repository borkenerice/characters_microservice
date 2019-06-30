from api import db, ma
from sqlalchemy.orm import validates


class Person(db.Model):
    __tablename__ = "person"
    person_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    place_id = db.Column(db.Integer, nullable=False)
    king = db.Column(db.Boolean, nullable=False)
    alive = db.Column(db.Boolean, nullable=False, default=False)

    @validates('name')
    def validate_name(self, key, name):
        if Person.query.filter(Person.name == name).one_or_none():
            raise ValueError('There is already a person with that name')
        return name


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
