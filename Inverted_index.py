import PostingList
table = dict()
distinct_tokens = set()


def get_index(token):
    # print(type(table.get(token)))
    return table.get(token)


class InvertedIndex:
    def __init__(self, doc):
        self.doc = doc
        # self.list = PostingList(self.doc.get_doc_id
        self.postinglist = PostingList.PostingList

    def add(self):
        tokens = self.doc.get_body().split(" ")

        for token in tokens:
            distinct_tokens.add(token)
        # print(distinct_tokens)

        for token in tokens:
            if token not in table:
                table.update({token: PostingList.PostingList(self.doc.get_doc_id())})
                table.get(token)
                # print(self.doc.get_body())


# p = Document("funny", "there are no man no")
# p1 = InvertedIndex(p)
# p1.add()
