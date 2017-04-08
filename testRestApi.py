import unittest
from pulse_api_client import BookPulseRestApi

from modBook import Book


class BookCreationTests(unittest.TestCase):
    def setUp(self):
        self.client = BookPulseRestApi(resourse="books")

    def test_create_full_book(self):
        book = Book(title="New Book", author="Super Author")
        resp = self.client.create_book(book)
        self.assertEqual(resp.status_code, 201)
        self.assertDictEqual(resp.json(), book.get_dict_with_id())
        #self.client.get_book(book)
        self.assertIn(resp, title , 'books')

q = BookCreationTests()

print(q)