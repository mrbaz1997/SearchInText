import itertools

start_count = itertools.count(1, 1)


class Document:

    # def __init__(self, data):
    #     self.data = data
    #
    # @classmethod
    # def text_docs(cls, _name, _body):
    #     cls._name = _name
    #     cls.body = _body
    #     cls._doc_id = next(start_count)
    #     return cls

    # @classmethod
    def __init__(self, id, title, tokens):
        self.title = title
        self.tokens = tokens
        self.doc_id = id

    def get_doc_id(self):
        return self.doc_id

    def get_name(self):
        return self.title

    def get_body(self):
        return self.tokens
