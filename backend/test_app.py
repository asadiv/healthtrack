import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING']=True
    with app.test_client() as client:
        yield client



# health
def test_health(client):
    response = client.get('/api/health')
    assert response.status_code ==200



# return list test
def test_list_patients(client):
    response = client.get('/api/patients')
    assert response.status_code ==200
    data = response.get_json()
    assert isinstance(data,list)


# unknown id

def test_unknown_id(client):
    response = client.get('/api/patients/999')
    assert response.status_code ==404
    

# post valid
def test_post(client):
    response = client.post('/api/patients',json={"name":"testa","condition":"flu"})
    assert response.status_code ==201


# post missing field
def test_missing(client):
    response = client.post('/api/patients',json={"name":"testa"})
    assert response.status_code ==400