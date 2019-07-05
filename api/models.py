from api import db, ma
from sqlalchemy.orm import validates


class Character(db.Model):
    __tablename__ = "person"
    character_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    place_id = db.Column(db.Integer)
    king = db.Column(db.Boolean, nullable=False)
    alive = db.Column(db.Boolean, nullable=False, default=False)

    def is_valid_king(self):
        characters = Character.query.filter_by(place_id=self.place_id).all()
        for character in characters:
            if character.alive and character.king:
                return False
        return True

    @validates('place_id', 'king', 'alive')
    def validate_character(self, key, value):
        # we need all the values of the parameters to validate correctly, checking the last one in the decorator ensures
        # we have all the needed values
        if key == 'alive':
            if value and self.king and self.place_id:
                if not self.is_valid_king():
                    raise ValueError('The place defined already has a king')
            if value and not self.place_id:
                raise ValueError('If the character is alive, it must have a place_id')
        return value


class CharacterSchema(ma.ModelSchema):
    class Meta:
        model = Character
        ordered = True
