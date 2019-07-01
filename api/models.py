from api import db, ma


class Person(db.Model):
    __tablename__ = "person"
    person_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    place_id = db.Column(db.Integer, nullable=False)
    king = db.Column(db.Boolean, nullable=False)
    alive = db.Column(db.Boolean, nullable=False, default=False)


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
