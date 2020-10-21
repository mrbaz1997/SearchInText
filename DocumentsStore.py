
docs = dict()


def get(id):
    return docs[id]


class DocumentStore:

    def __init__(self, doc):
        self.doc = doc

    def add(self):
        docs[self.doc.get_doc_id()] = self.doc
        # print(self.doc.get_doc_id())
        # print(docs.get(self.doc.get_doc_id()).get_body())

    def get_all(self):
        return self.doc


# d1 = DocumentStore(Doc("alice", "this is body"))
# d1.add()
