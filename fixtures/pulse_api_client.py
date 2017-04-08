import requests

class BookPulseRestApi:
    def __init__(self, resourse):
        self.host = 'pulse-rest-testing.herokuapp.com'
        self.base_url = "http://{}/".format(self.host)
        self.url = self.base_url + resourse + '/'



    def create_book(self, obj):
        resp = requests.post(self.url, data={'title': obj.title, 'author': obj.author})

        if resp.status_code == 201:
            obj.set_id(resp.json()['id'])
        return resp

    def get_objects(self):
        resp = requests.get(self.url)#, params=obj.get_dict())
        p = resp.json()
        print(p)
        return p


    def get_obj(self, obj):
        resp = requests.get(self.url + str(obj.get_dict_with_id()['id']))
        return resp

    def delete_obj(self, obj):
        resp = requests.delete(self.url + obj.set_id())
        return resp


    def modify_obj(self, obj):
        resp = requests.put(self.url, data={'title': obj.title, 'author': obj.author})
        obj.set_id(resp.json()['id'])
        return resp


if __name__ == "__main__":
    m = BookPulseRestApi('books')
    from models.modBook import Book
    book_data = m.get_objects()[2]
    book = Book(**book_data)
    print(book.id)
    a = m.get_obj(book)
    print(a.status_code)
    print(a.json())



