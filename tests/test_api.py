import pytest
from api import create_app, db
from api.models import Character


@pytest.fixture(scope='module')
def test_client():
    """
    fixture that initializes the flask app to be used in the tests
    :return: flask app
    """
    app = create_app()
    client = app.test_client()
    with app.app_context():
        yield client


@pytest.fixture(scope='module')
def init_database():
    """
    fixture that initializes the db to be used in the tests
    :return: db
    """
    db.create_all()
    character = Character(name='Jon Test', place_id=1, king=True, alive=True)
    character2 = Character(name='Perrete Test', place_id=2, king=False, alive=False)
    db.session.add(character)
    db.session.add(character2)
    db.session.commit()
    yield db
    db.drop_all()


def test_get_all_characters_response_status(test_client, init_database):
    """
    Check correct response code for a get request to get all the characters available
    :param test_client: fixture
    :param init_database: fixture
    :return:
    """
    response = test_client.get('/api/character')
    assert response.status_code == 200


def test_get_all_characters_by_place_id_response_status(test_client, init_database):
    """
    Check correct response code for a get request to get all the characters available in an specified place_id
    :param test_client: fixture
    :param init_database: fixture
    :return:
    """
    response = test_client.get('/api/character/findByPlace/2')
    assert response.status_code == 200


def test_get_character_by_id_response_code(test_client, init_database):
    """
    Check correct response code for a get request to a character identified by its id
    :param test_client: fixture
    :param init_database: fixture
    :return:
    """
    response = test_client.get('/api/character/1')
    assert response.status_code == 200


def test_get_character_by_id_do_not_exists_response_code(test_client, init_database):
    """
    Check correct response code for a get request to a character identified by its id if it does not exists
    :param test_client: fixture
    :param init_database: fixture
    :return:
    """
    response = test_client.get('/api/character/4')
    assert response.status_code == 404


def test_create_character_response_code(test_client, init_database):
    """
    Check correct response code for a post request to create a character
    :param test_client: fixture
    :param init_database: fixture
    :return:
    """
    character = {
        'name': 'Tirria',
        'place_id': "3",
        'king': False,
        'alive': True
    }
    response = test_client.post('/api/character', json=character)
    assert response.status_code == 201


def test_create_character_same_name_error_response_code(test_client, init_database):
    """
    Check correct response code for a post request to create a character if it has the same name as
    one that already exists
    :param test_client: fixture
    :param init_database: fixture
    :return:
    """
    character = {
        'name': 'Tirria',
        'place_id': "3",
        'king': False,
        'alive': True
    }
    response = test_client.post('/api/character', json=character)
    assert response.status_code == 400


def test_create_character_alive_without_place_id(test_client, init_database):
    """
        Check correct response code for a post request to create a character
        alive and without place_id
        :param test_client: fixture
        :param init_database: fixture
        :return:
        """
    character = {
        'name': 'Manolin',
        'king': True,
        'alive': True
    }
    response = test_client.post('/api/character', json=character)
    assert response.status_code == 400


def test_create_character_not_valid_king(test_client, init_database):
    """
        Check correct response code for a post request to create a character
        and set ir as king if already exists a king in the same place
        :param test_client: fixture
        :param init_database: fixture
        :return:
        """
    character = {
        'name': 'Manolin',
        'place_id': "1",
        'king': True,
        'alive': True
    }
    response = test_client.post('/api/character', json=character)
    assert response.status_code == 400


def test_update_character_response_code(test_client, init_database):
    """
    Check correct response code for a put request to update a character
    :param test_client: fixture
    :param init_database: fixture
    :return:
    """
    character = {
        'name': 'Arrolla',
        'place_id': "3",
        'king': True,
        'alive': True
    }
    response = test_client.put('/api/character/1', json=character)
    assert response.status_code == 201


def test_update_character_same_name_error_response_code(test_client, init_database):
    """
    Check correct response code for a put request to update a character
    if it has the same name as one that already exists
    :param test_client: fixture
    :param init_database: fixture
    :return:
    """
    character = {
        'name': 'Tirria',
        'place_id': "3",
        'king': False,
        'alive': True
    }
    response = test_client.put('/api/character/2', json=character)
    assert response.status_code == 400


def test_update_character_not_valid_king(test_client, init_database):
    """
        Check correct response code for a put request to update a character
        and set ir as king if already exists a king in the same place
        :param test_client: fixture
        :param init_database: fixture
        :return:
        """
    character = {
        'name': 'Manolin',
        'place_id': "3",
        'king': True,
        'alive': True
    }
    response = test_client.put('/api/character/2', json=character)
    assert response.status_code == 400


def test_update_character_alive_without_place_id(test_client, init_database):
    """
        Check correct response code for a put request to update a character
        and set it as alive without place id
        :param test_client: fixture
        :param init_database: fixture
        :return:
        """
    character = {
        'name': 'Manolin',
        'king': True,
        'alive': True
    }
    response = test_client.put('/api/character/2', json=character)
    assert response.status_code == 400


def test_delete_character_response_code(test_client, init_database):
    """
    Check correct response code for a delete request to delete a character
    :param test_client: fixture
    :param init_database: fixture
    :return:
    """
    response = test_client.delete('/api/character/1')
    assert response.status_code == 200


def test_delete_character_does_not_exists_error_response_code(test_client, init_database):
    """
    Check correct response code for a delete request to delete a place that do not exists
    :param test_client: fixture
    :param init_database: fixture
    :return:
    """
    response = test_client.delete('/api/character/80')
    assert response.status_code == 404




