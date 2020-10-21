from os import listdir
from os.path import isfile, join
import os
import Document
import DocumentsStore
import PostingList
import Inverted_index


texts = [f for f in listdir("resources") if isfile(join("resources", f))]
store = DocumentsStore.DocumentStore
index = Inverted_index.InvertedIndex

for name in texts:
    stream = open(os.path.join("resources", name), 'rb').read()
    body = str(stream).lower()
    document = Document.Document(name, body)

    store(document).add()
    index(document).add()
    # print(table)


while 1:
    line = input("Enter Your Query: ").lower()
    if line == "qq":
        break

    print(Inverted_index.table)
    # p_list = PostingList.PostingList(Inverted_index.get_index(line).get())
    # print(type(get_index(line).get()), get_index(line).get())
    # for doc_id in p_list:
    #     print(doc_id)

    # for match in list.PostingList(Index.get(line)).get():
    #     print(store.get(match))
