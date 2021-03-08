import pytest
from django.core.exceptions import ValidationError

from tables.models import Table, Leg, Foot


@pytest.fixture
def user(django_user_model):
    user = django_user_model.objects.create_user(
        username="test_user",
        password="test_password"
    )
    return user


def test_tables_create(user, client, django_user_model):
    client.force_login(user)

    response = client.post('/api/tables/', {"name": "Table One"})
    assert response.status_code == 201

    response = client.post('/api/tables/', {"name": "Table One"})
    assert response.status_code == 400


def test_tables_list(user, client, django_user_model):
    client.force_login(user)
    client.post('/api/tables/', {"name": "Table One"})
    client.post('/api/tables/', {"name": "Table Two"})

    response = client.get('/api/tables/')
    assert response.status_code == 200
    assert response.json()["count"] == 2


def test_tables_detail(user, client, django_user_model):
    client.force_login(user)
    client.post('/api/tables/', {"name": "Table One"})

    response = client.get('/api/tables/1/')
    assert response.status_code == 200
    assert response.json()["name"] == "Table One"


def test_tables_update(user, client, django_user_model):
    client.force_login(user)
    client.post('/api/tables/', {"name": "Table One"})
    client.post('/api/tables/', {"name": "Table Two"})

    response = client.put('/api/tables/1/',
                          data='{"name": "Table One Updated"}',
                          content_type='application/json')
    assert response.status_code == 200
    assert response.json()["name"] == "Table One Updated"

    response = client.put('/api/tables/1/',
                          data='{"name": "Table Two"}',
                          content_type='application/json')
    assert response.status_code == 400


def test_tables_delete(user, client, django_user_model):
    client.force_login(user)
    client.post('/api/tables/', {"name": "Table One"})

    response = client.delete('/api/tables/1/')
    assert response.status_code == 204


def test_legs_create(user, client, django_user_model):
    client.force_login(user)
    client.post('/api/tables/', {"name": "Table One"})

    response = client.post('/api/legs/', {"table_id": "1"})
    assert response.status_code == 201

    response = client.post('/api/legs/', {"table_id": "2"})
    assert response.status_code == 400


def test_legs_list(user, client, django_user_model):
    client.force_login(user)
    client.post('/api/tables/', {"name": "Table One"})
    client.post('/api/legs/', {"table_id": "1"})
    client.post('/api/legs/', {"table_id": "1"})
    client.post('/api/legs/', {"table_id": "1"})

    response = client.get('/api/legs/')
    assert response.status_code == 200
    assert response.json()["count"] == 3


def test_legs_update(user, client, django_user_model):
    client.force_login(user)
    client.post('/api/tables/', {"name": "Table One"})
    client.post('/api/tables/', {"name": "Table Two"})
    client.post('/api/legs/', {"table_id": "1"})

    response = client.put('/api/legs/1/',
                          data='{"table_id": "2"}',
                          content_type='application/json')
    assert response.status_code == 200
    assert response.json()["table_id"] == 2

    response = client.put('/api/legs/1/',
                          data='{"table_id": "4"}',
                          content_type='application/json')
    assert response.status_code == 400


def test_legs_detail(user, client, django_user_model):
    client.force_login(user)
    client.post('/api/tables/', {"name": "Table One"})
    client.post('/api/tables/', {"name": "Table Two"})
    client.post('/api/legs/', {"table_id": "2"})

    response = client.get('/api/legs/1/')
    assert response.status_code == 200
    assert response.json()["table_id"] == 2


def test_legs_delete(user, client, django_user_model):
    client.force_login(user)
    client.post('/api/tables/', {"name": "Table One"})
    client.post('/api/legs/', {"table_id": "1"})

    response = client.delete('/api/legs/1/')
    assert response.status_code == 204


def test_feet_create(user, client, django_user_model):
    client.force_login(user)
    client.post('/api/tables/', {"name": "Table One"})
    client.post('/api/tables/', {"name": "Table Two"})
    client.post('/api/legs/', {"table_id": "1"})
    client.post('/api/legs/', {"table_id": "1"})
    client.post('/api/legs/', {"table_id": "2"})

    response = client.post('/api/feet/',
                           {"legs": [1, 2, 3], "radius": 2.0})
    assert response.status_code == 201

    with pytest.raises(ValidationError) as excinfo:
        response = client.post('/api/feet/',
                               {"legs": [1, 2], "radius": 2.0, "length": 4})
    assert "ValidationError" in str(excinfo)

    with pytest.raises(ValidationError) as excinfo:
        response = client.post('/api/feet/',
                               {"legs": [1, 2], "length": 4})
    assert "ValidationError" in str(excinfo)

    with pytest.raises(ValidationError) as excinfo:
        response = client.post('/api/feet/',
                               {"legs": [1, 2], "width": 5})
    assert "ValidationError" in str(excinfo)


def test_feet_list(user, client, django_user_model):
    client.force_login(user)
    client.post('/api/tables/', {"name": "Table One"})
    client.post('/api/tables/', {"name": "Table Two"})
    client.post('/api/legs/', {"table_id": "1"})
    client.post('/api/legs/', {"table_id": "1"})
    client.post('/api/legs/', {"table_id": "2"})
    client.post('/api/feet/', {"legs": [1, 2, 3], "radius": 2.0})
    client.post('/api/feet/', {"legs": [2, 3], "length": 7.5, "width": 2.5})
    client.post('/api/feet/', {"legs": [2, 3], "length": 17, "width": 3.1})

    response = client.get('/api/feet/')
    assert response.status_code == 200
    assert response.json()["count"] == 3


def test_feet_detail(user, client, django_user_model):
    client.force_login(user)
    client.post('/api/tables/', {"name": "Table One"})
    client.post('/api/tables/', {"name": "Table Two"})
    client.post('/api/legs/', {"table_id": "1"})
    client.post('/api/legs/', {"table_id": "1"})
    client.post('/api/legs/', {"table_id": "2"})
    client.post('/api/feet/', {"legs": [1, 2, 3], "radius": 2.0})
    client.post('/api/feet/', {"legs": [2, 3], "length": 7.5, "width": 2.5})
    client.post('/api/feet/', {"legs": [1, 3], "length": 17, "width": 3.1})

    response = client.get('/api/feet/3/')
    assert response.status_code == 200
    assert response.json()["length"] == 17


def test_feet_update(user, client, django_user_model):
    client.force_login(user)
    client.post('/api/tables/', {"name": "Table One"})
    client.post('/api/tables/', {"name": "Table Two"})
    client.post('/api/legs/', {"table_id": "1"})
    client.post('/api/legs/', {"table_id": "1"})
    client.post('/api/legs/', {"table_id": "2"})
    client.post('/api/feet/', {"legs": [1, 2, 3], "radius": 2.0})
    client.post('/api/feet/', {"legs": [2, 3], "length": 7.5, "width": 2.5})
    client.post('/api/feet/', {"legs": [1, 3], "length": 9, "width": 3.1})

    response = client.put('/api/feet/1/',
                          data='{"legs": [1, 3]}',
                          content_type='application/json')
    assert response.status_code == 200
    assert response.json()["legs"] == [1, 3]

    response = client.put('/api/feet/1/',
                          data='{"length": 12.2}',
                          content_type='application/json')
    assert response.status_code == 400

    response = client.put('/api/feet/2/',
                          data='{"length": 0}',
                          content_type='application/json')
    assert response.status_code == 400

    response = client.put('/api/feet/3/',
                          data='{"width": 0}',
                          content_type='application/json')
    assert response.status_code == 400


def test_feet_delete(user, client, django_user_model):
    client.force_login(user)
    client.post('/api/tables/', {"name": "Table One"})
    client.post('/api/legs/', {"table_id": "1"})
    client.post('/api/feet/', {"legs": [1], "radius": 2.0})

    response = client.delete('/api/feet/1/')
    assert response.status_code == 204
