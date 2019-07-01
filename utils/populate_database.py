import os
import config
from api import db, create_app
from api.models import Person

# Data to initialize database with
PERSONS = [
    {
        "name": "Jon",
        "place_id": "1",
        "king": False,
        "alive": False
    },
    {
        "name": "Sansa",
        "place_id": "1",
        "king": True,
        "alive": True
    },
    {
        "name": "Doggie",
        "place_id": "2",
        "king": False,
        "alive": False
    },
]


def create_database():
    # Delete database file if it exists currently
    if os.path.exists(os.path.join(config.BASE_DIR, 'persons.db')):
        os.remove(os.path.join(config.BASE_DIR, 'persons.db'))
    # Create the database
    app = create_app()
    with app.app_context():
        db.create_all()
        # iterate over the PEOPLE structure and populate the database
        for person in PERSONS:
            p = Person(name=person.get("name"), place_id=person.get("place_id"), king=person.get("king"),
                       alive=person.get("alive"))
            db.session.add(p)
        db.session.commit()


if __name__ == '__main__':
    create_database()
