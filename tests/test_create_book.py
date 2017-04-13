
import pytest
from models.modBook import Book
test_data= [Book(title="WhoIsPulse?", author="Yuriy"),
            Book(title="0", author="0")]

@pytest.mark.parametrize('book', test_data, ids=[repr(v) for v in test_data])
def test_create_full_book(app_book, book):
    resp = app_book.create_book(book)



# def test_create_book_NoAuthor(app):
#     book = Book(title="WhoIsPulse?")
#     resp = app.create_book(book)

    #Verification

    assert resp.status_code == 201
    assert resp.json() == book.get_dict_with_id ()
    #self.assertEqual(resp.status_code, 201)
    #self.assertDictEqual(resp.json(), book.get_dict_with_id())
    #self.client.get_book(book)


# q = BookCreationTests()
#
# print(q)