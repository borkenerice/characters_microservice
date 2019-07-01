from api import db, ma
from sqlalchemy.orm import validates


class Character(db.Model):
    __tablename__ = "person"
    character_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    place_id = db.Column(db.Integer)
    king = db.Column(db.Boolean, nullable=False)
    alive = db.Column(db.Boolean, nullable=False, default=False)

    @validates('king')
    def validate_king(self, key, place_id):
        if self.alive:
            characters = Character.query.filter_by(place_id=self.place_id).all()
            for character in characters:
                if character.alive and character.king:
                    raise ValueError('The place defined already has a king')
        return place_id

    @validates('alive')
    def validate_alive(self, key, alive):
        if alive and not self.place_id:
            raise ValueError('Character cannot be alive and not have a place_id')
        return alive


class CharacterSchema(ma.ModelSchema):
    class Meta:
        model = Character
