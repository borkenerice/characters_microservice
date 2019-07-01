from flask import abort
from sqlalchemy.exc import IntegrityError

from api import db
from api.models import Character, CharacterSchema


def find_all_characters():
    characters = Character.query.order_by(Character.name).all()
    character_schema = CharacterSchema(many=True)
    data = character_schema.dump(characters).data
    return data


def find_character_by_id(character_id):
    character = Character.query.get_or_404(character_id, description=f'Character not found with the id: {character_id}')
    character_schema = CharacterSchema()
    data = character_schema.dump(character).data
    return data


def find_characters_by_place_id(place_id):
    characters = Character.query.filter_by(place_id=place_id).order_by(Character.name).all()
    character_schema = CharacterSchema(many=True, exclude=('place_id',))
    data = character_schema.dump(characters).data
    return data


def update_character(character_id, character_data):
    character = Character.query.get_or_404(character_id, description=f'Character not found with the id: {character_id}')
    character_schema = CharacterSchema()
    try:
        updated_character = character_schema.load(character_data, session=db.session).data
        updated_character.character_id = character.character_id
        db.session.merge(updated_character)
        db.session.commit()
        data = character_schema.dump(updated_character).data
        return data, 201
    except IntegrityError as i:
        db.session.rollback()
        abort(400, f'Character: {character_id} could not be updated: {i.orig}')
    except ValueError as v:
        db.session.rollback()
        abort(400, f'Character: {character_id} could not be updated: {v}')


def create_character(character_data):
    try:
        schema = CharacterSchema()
        new_character = schema.load(character_data, session=db.session).data
        db.session.add(new_character)
        db.session.commit()
        data = schema.dump(new_character).data
        return data, 201
    except IntegrityError as i:
        db.session.rollback()
        abort(400, f'Character could not be created: {i.orig}')
    except ValueError as v:
        db.session.rollback()
        abort(400, f'Character could not be created: {v}')


def delete_character_by_id(character_id):
    character = Character.query.get_or_404(character_id, description=f'Character not found with the id: {character_id}')
    db.session.delete(character)
    db.session.commit()
    return

