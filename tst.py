import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client): #создаём виртуального клиента
    response = client.get('/') #делаем запрос на главную страницу
    assert response.status_code == 200 #при получении кода ответ 200
    assert b"Last Hello World !!" in response.data 
