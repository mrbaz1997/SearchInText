from PostingList import PostingList
import re


class InvertedIndex:
    def __init__(self, doc, table):
        self.doc = doc
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
        # print()


class NormalizedInvertedIndex:

    def __init__(self, doc, table):
        self.doc = doc
        # self.tokens = doc
        self.table = table
        self.distinct_tokens = set()
        # self.positional_index = dict()
        self.counter = 0
        self.next_progress = 0

    def add(self):
        # tokens = re.findall(r"[\w']+", self.doc.get_body())
        tokens = self.doc.get_body()

        position = 0
        for token in tokens:
            self.distinct_tokens.add(token)

        for token in tokens:
            # progress = int((self.counter * 100 / len(self.distinct_tokens)))
            # self.counter += 1
            # if progress - self.next_progress == 1:
            #     self.next_progress = progress
            # print("|", end="", flush=True)

            # tmp = list()
            positions = list()
            if token not in self.table:
                self.table[token] = dict()
            # elif self.table.get(token) is not None:
            #     tmp = self.table[token]
            # tmp.append(self.doc.doc_id)
            # self.table[token] = tmp
            if self.doc.doc_id not in self.table[token]:
                self.table[token][self.doc.doc_id] = list()
            elif self.table[token].get(self.doc.doc_id) is not None:
                positions = self.table[token][self.doc.doc_id]
            positions.append(position)
            self.table[token][self.doc.doc_id] = positions
            # print()
            position += 1

        # print(self.table)
        # return self.table
