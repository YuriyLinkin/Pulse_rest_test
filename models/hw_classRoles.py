class Role:

    def __init__(self, id=None, name=None, type=None, level=None, book=None):
        self.name = name
        self.type = type
        self._id = id
        self.level = level
        self.book = book

    def set_id(self, id):
        self.id = id

    def get_dict(self):
        return {'name': self.name, 'type': self.type, 'level': self.level, 'book': self.book}

    def get_dict_with_id(self):
        return {'id': self.id, 'name': self.name, 'type': self.type, 'level': self.level, 'book': self.book}

    def get_dict_with_null(self, null):
        return {'id': self.id, 'name': self.name, 'type': self.type, 'level': null, 'book': null}






if __name__ == "__main__":
    m = Role()
    print(m.type)
    print(m.name)
    print(m.level)
    print(m.book)