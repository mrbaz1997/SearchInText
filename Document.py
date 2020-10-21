import itertools

start_count = itertools.count(1, 1)


class Document:

    def __init__(self, _name, _body):
        self._name = _name
        self.body = _body
        self._doc_id = next(start_count)

    def get_doc_id(self):
        return self._doc_id

    def get_name(self):
        return self._name

    def get_body(self):
        return self.body


# p1 = Document(" , "this is body")
# print(p1.get_body(), p2.get_doc_id(), p3.get_doc_id())
