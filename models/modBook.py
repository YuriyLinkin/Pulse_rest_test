class Book:

    def __init__(self, title=None, author=None, id=None):
        self.title = title
        self.author = author
        self._id = id

    def __repr__(self):
        return "{}:{}".format(self._id, self.title, self.author)

    def set_id(self, id):
        self._id = id

    def get_dict(self):
        return {'title': self.title, 'author': self.author}

    def get_dict_with_id(self):
        return {'id': self._id, 'title': self.title, 'author': self.author}




if __name__ == "__main__":
    m = Book()
    print(m.title)
    print(m.author)