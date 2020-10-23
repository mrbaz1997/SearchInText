from os import listdir
from os.path import isfile, join
from Document import Document
import DocumentsStore
from Inverted_index import InvertedIndex
import shelve
import PostingList

resource = "resources"
texts = [f for f in listdir(resource) if isfile(join(resource, f))]
store = DocumentsStore.DocumentStore
index = InvertedIndex

table_name = 'posting list'
table = shelve.open(table_name, writeback=True)
for name in texts:
    stream = open(join(resource, name), 'rb').read()
    body = str(stream).lower()
    name = name.replace(".txt", "")
    document = Document(name, body)
    store(document).add()
    print("Indexing {0}".format(name))
    index(document, table).add()

_table = shelve.open(table_name)


def simple_search():
    try:
        for x in _table.get(line):
            get_id_name(x)
    except Exception as e:
        handle_error(type(e).__name__)


def and_ing():
    try:
        compare(PostingList.and_postinglist(_table.get(words[0]), _table.get(words[1])))
        print("↑These books contain both the words \"{}\" and \"{}\"".format(words[0], words[1]))
    except Exception as e:
        handle_error(type(e).__name__)


def or_ing():
    try:
        compare(PostingList.or_postinglist(_table.get(words[0]), _table.get(words[1])))
        print("↑These books contain at least one of the words \"{}\" or \"{}\"".format(words[0], words[1]))
    except Exception as e:
        handle_error(type(e).__name__)


def not_ing():
    try:
        compare(PostingList.not_postinglist(_table.get(words[0]), _table.get(words[1])))
        print("↑These books only contain \"{}\" and don't contain \"{}\"".format(words[0], words[1]))
    except Exception as e:
        handle_error(type(e).__name__)


def handle_error(error):
    if error == "TypeError":
        print("No Match")
    else:
        print("error! Insert two words e.g: blue green")


def compare(_words):
    for x in _words:
        get_id_name(x)


def get_id_name(_word):
    print(Document.get_doc_id(DocumentsStore.get(_word)),
          Document.get_name(DocumentsStore.get(_word)))


table.close()
while 1:
    print("\n1.Simple Search\n"
          "2.AND_ing Search of two word\n"
          "3.OR_ing Search of two word\n"
          "4.NOT_ing Search of two word")


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
    try:
        select = int(input("input: "))
    except Exception:
        print("Invalid Value, Try again!")
        continue

    while 1:
        line = input("\nEnter Your Query(q to Quit): ").lower()
        if line == "q":
            break

        words = line.split(" ")
        options[select]()

    # table.close()
