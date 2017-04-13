import pytest
from models.modBook import Book

@pytest.fixture
def book(app_book):
    v = Book (title= "For del", author= "for_del")
    app_book.create_book(v)
    return v

def test_delete(app_book, book):
    resp = app_book.delete_obj(book)

    assert resp.status_code == 204