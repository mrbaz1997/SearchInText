docs = dict()


def get(id):
    return docs.get(id)


class DocumentStore:

    def __init__(self, doc):
        self.doc = doc

    def add(self):
        docs[self.doc.doc_id] = self.doc

    def get_all(self):
        return self.doc
