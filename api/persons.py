from flask import abort
from sqlalchemy.exc import IntegrityError

from api import db
from api.models import Person, PersonSchema


def read_all_persons():
    persons = Person.query.order_by(Person.name).all()
    person_schema = PersonSchema(many=True)
    data = person_schema.dump(persons).data
    return data


def read_person(person_id):
    person = Person.query.get_or_404(person_id, description=f'Person not found with the id: {person_id}')
    person_schema = PersonSchema()
    data = person_schema.dump(person).data
    return data


def update_person(person_id, person_data):
    person = Person.query.get_or_404(person_id, description=f'Person not found with the id: {person_id}')
    person_schema = PersonSchema()
    try:
        updated_person = person_schema.load(person_data, session=db.session).data
        updated_person.person_id = person.person_id
        db.session.merge(updated_person)
        db.session.commit()
        data = person_schema.dump(updated_person).data
        return data, 201
    except IntegrityError as i:
        db.session.rollback()
        abort(400, f'Person: {person_id} could not be updated: {i.orig}')


def create_person(person_data):
    try:
        schema = PersonSchema()
        new_person = schema.load(person_data, session=db.session).data
        db.session.add(new_person)
        db.session.commit()
        data = schema.dump(new_person).data
        return data, 201
    except IntegrityError as i:
        db.session.rollback()
        abort(400, f'Person could not be created: {i.orig}')


def delete_person(person_id):
    person = Person.query.get_or_404(person_id, description=f'Person not found with the id: {person_id}')
    db.session.delete(person)
    db.session.commit()
    return

