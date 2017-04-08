import pytest
from pulse_api_client import BookPulseRestApi

from modBook import Book

@pytest.fixture()
def app():
    fixture = BookPulseRestApi(resourse="books")
    return fixture

def test_create_full_book(app):
    book = Book(title="WhoIsPulse?", author="Yuriy")
    resp = app.create_book(book)

    #Verification

    assert resp.status_code == 201
    assert resp.json() == book.get_dict_with_id ()
    #self.assertEqual(resp.status_code, 201)
    #self.assertDictEqual(resp.json(), book.get_dict_with_id())
    #self.client.get_book(book)


# q = BookCreationTests()
#
# print(q)