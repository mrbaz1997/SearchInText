from PostingList import PostingList
import re


class InvertedIndex:
    def __init__(self, doc, table):
        self.doc = doc
        self.postinglist = PostingList
        self.distinct_tokens = set()
        self.table = table
        self.counter = 0
        self.next_progress = 0

    def add(self):
        tokens = re.findall(r"[\w']+", self.doc.get_body())

        for token in tokens:
            self.distinct_tokens.add(token)

        for token in self.distinct_tokens:
            progress = int((self.counter * 100 / len(self.distinct_tokens)))
            self.counter += 1
            if progress - self.next_progress == 1:
                self.next_progress = progress
                print("|", end="", flush=True)

            tmp = list()
            if token not in self.table:
                self.table[token] = []
            elif self.table.get(token) is not None:
                tmp = self.table[token]
            tmp.append(self.doc.get_doc_id())
            self.table[token] = tmp
        print()
