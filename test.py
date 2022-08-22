from app import app

def test():
    response = app.test_client().get('/')
    assert response.status_code == 404

def test_book_route():
    response = app.test_client().get('/books')
    assert response.status_code == 200

def test_movies_route():
    response = app.test_client().get('/movies')
    assert response.status_code == 200

def test_navbar_content():
    response = app.test_client().get('/books')
    assert b"movie" in response.data
    assert b"books" in response.data
    assert b"players" in response.data
    assert b"Software" in response.data