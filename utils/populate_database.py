import os
import config
from api import db, create_app
from api.models import Character

# Data to initialize database with
CHARACTERS = [
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
    if os.path.exists(os.path.join(config.BASE_DIR, 'characters.db')):
        os.remove(os.path.join(config.BASE_DIR, 'characters.db'))
    # Create the database
    app = create_app()
    with app.app_context():
        db.create_all()
        # iterate over the PEOPLE structure and populate the database
        for character in CHARACTERS:
            p = Character(name=character.get("name"), place_id=character.get("place_id"), king=character.get("king"),
                          alive=character.get("alive"))
            db.session.add(p)
        db.session.commit()


if __name__ == '__main__':
    create_database()
