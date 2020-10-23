from os import listdir
from os.path import isfile, join
from Document import Document
from DocumentsStore import DocumentStore
from Inverted_index import InvertedIndex
import shelve
import PostingList

resource = "resources"
texts = [f for f in listdir(resource) if isfile(join(resource, f))]
store = DocumentStore
index = InvertedIndex

table = shelve.open('posting list', writeback=True)
for name in texts:
    stream = open(join(resource, name), 'rb').read()
    body = str(stream).lower()
    name = name.replace(".txt", "")
    document = Document(name, body)
    store(document).add()
    print("Indexing {0}".format(name))
    index(document, table).add()

_table = shelve.open('posting list')


def simple_search():
    try:
        for x in _table.get(line):
            get_id_name(x)
    except TypeError:
        print("No Match")
    except KeyError:
        print("error while storing books!")


def and_ing():
    try:
        compare(PostingList.and_postinglist(_table.get(words[0]), _table.get(words[1])))
    except TypeError:
        print("No Match")


def or_ing():
    try:
        compare(PostingList.or_postinglist(_table.get(words[0]), _table.get(words[1])))
    except TypeError:
        print("No Match")


def not_ing():
    try:
        compare(PostingList.not_postinglist(_table.get(words[0]), _table.get(words[1])))
    except TypeError:
        print("No Match")


def compare(_words):
    try:
        for x in _words:
            get_id_name(x)
    except IndexError:
        print("error! Insert two words e.g: blue green")


def get_id_name(_word):
    print(Document.get_doc_id(DocumentsStore.get(_word)),
          Document.get_name(DocumentsStore.get(_word)))


table.close()
while 1:
    print("\n1.Simple Search\n"
          "2.And_ing Search of two word\n"
          "3.Or_ing Search of two word\n"
          "4.Not_ing Search of two word")

    def simple():
        simple_search()

    def anding():
        and_ing()

    def oring():
        or_ing()

    def noting():
        not_ing()

    options = {
        1: simple,
        2: anding,
        3: oring,
        4: noting,
    }
    select = int(input("input: "))
    while 1:
        line = input("\nEnter Your Query(q to Quit): ").lower()
        if line == "q":
            break

        words = line.split(" ")
        options[select]()

    table.close()
