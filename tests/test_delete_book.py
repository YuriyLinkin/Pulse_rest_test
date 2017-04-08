import pytest
from models.modBook import Book

@pytest.fixture
def book(app):
    v = Book (title= "For del", author= "for_del")
    app.create_book(v)
    return v

def test_delete(app, book):
    resp = app.delete_obj(book)

    assert resp.status_code == 204