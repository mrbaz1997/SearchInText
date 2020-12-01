from time import time
from xml.etree import ElementTree as et
import re
import Normalize
from InvertedIndex import NormalizedInvertedIndex as index
from Document import Document
import DocumentStore
import PostingList


def spend_time(job, _start_time):
    return "{}: {:0.3f} seconds".format(job, _start_time)


def simple_search(t):
    print("Title\tID")
    try:
        for x in [*t.get(inputs[0])]:
            get_id_name(x)
    except Exception:
        print("No Match")
    print("{1} result found for {0}".format(line, len([*t.get(inputs[0])])))


def and_ing(t):
    try:
        and_list = PostingList.and_postinglist(t.get(inputs[0]), t.get(inputs[2]))
        compare(and_list)
        print("↑ {} abstracts contain both the words \"{}\" and \"{}\"".format(len(and_list), inputs[0], inputs[2]))
    except Exception as ex:
        handle_error(type(ex).__name__)


def get_id_name(_word):
    print(Document.get_doc_id(DocumentStore.get(_word)),
          Document.get_name(DocumentStore.get(_word)))


def compare(_words):
    for x in _words:
        get_id_name(x)


def handle_error(error):
    if error == "TypeError":
        print("No Match")
    else:
        print("error! Insert two words e.g: blue AND green")


def normalize(_list):
    _x = 0
    # try:
    normalization_time[0] = time()  # Calculate normalization runtime
    while _x < len(_list):  # To normalize and find stop words, we need to scroll through the abstract list

        if _list[_x] in stop_words:  # Is this pharse (in the abstract list) a stop word?
            _list.remove(_list[_x])  # If yes, so remove the pharse
            continue  # and "Continue" to next item in the abstract list.

        for letter in _list[_x]:  # Check all letters of the phrase
            if letter in Normalize.grouping.keys():  # If it's not Normal, normalize it!
                _list[_x] = _list[_x].replace(letter, Normalize.grouping[letter])
        _x += 1
    normalization_time[1] += time() - normalization_time[0]
    return _list


table = dict()
start_time = time()
source = "resources/xml/simple2.xml"
parser = et.parse(source)
print(spend_time("Parsing", time() - start_time))
root = parser.getroot()

stop_words = {'است', 'و', 'یا', 'با', 'را', 'که', 'هم', 'به',
              'از', 'در', 'هر', 'بر', 'دارد', 'آن', 'بود', 'پس',
              'سر', 'اگر', 'تا', 'دارند', 'شد', 'این'}
regex = r"[^\'. '\s\=\|\}\{\(\)\"\{\}\'\_\“\:؛\،\;\?\!\؟]+"

iterator_count = 0
progress_percent = 100
normalization_time = [0, 0]
Tokenization_time = [0, 0]
indexing_time = [0, 0]
for child in root:  # read child tags
    id = iterator_count  # every abstract has an ID (Auto Increment)
    title = child.find('title').text.split(" ")  # as a doc every abstract has a title
    del title[0]
    title = " ".join(title)

    Tokenization_time[0] = time()  # calculate tokeniztion runtime
    try:
        result = re.findall(regex, child.find('abstract').text)  # tokenize abstract
    except Exception:
        continue
    Tokenization_time[1] += time() - Tokenization_time[0]

    result = normalize(result)
    document = Document(id, title, result)
    DocumentStore.DocumentStore(document).add()
    indexing_time[0] = time()  # Calculate indexing runtime
    index(document, table).add()
    # table.update(index(title, result).add())               # Index current abstract and update table dictionary
    indexing_time[1] += time() - indexing_time[0]
    iterator_count += 1
    # print(result)
    if iterator_count == int(762216 / progress_percent):
        print("\r", "{:.0f}% of doc Indexed".format(100 / progress_percent), end="")
        progress_percent *= 0.99

print("\n")

print(spend_time("Tokenize", Tokenization_time[1]))
print(spend_time("Normalize", normalization_time[1]))
print(spend_time("Indexing", indexing_time[1]))
# print(table)


def advanced_search():
    counter = 0
    k = list()
    k_append = False
    doc_id = dict()
    final_list = list()
    for x in inputs:
        if x.startswith("/"):
            k.append(int(x.replace('/', '')))
            k_append = True
        elif x.startswith("&"):
            k.append(0)
            k_append = True
        elif counter == 0:
            doc_id[counter] = table.get(x)
            counter += 1
        else:
            if not k_append:
                k.append(1)
            else:
                k_append = False
            doc_id[counter] = table.get(x)
            counter += 1
    # print(k)

    and_list = [*doc_id[0]]
    for x in range(1, counter):
        and_list = PostingList.and_postinglist(and_list, [*doc_id[x]])

    for x in and_list:
        aprroved = list()
        for space in range(len(k)):
            first_word = doc_id[space][x]
            second_word = doc_id[space+1][x]
            i, j = 0, 0
            if k[space] > 0:
                while i < len(first_word) and j < len(second_word):
                    if second_word[j] - first_word[i] < 0:
                        j += 1
                    elif second_word[j] - first_word[i] <= k[space]:
                        aprroved.append(1)
                        break
                    else:
                        i += 1
            elif k[space] == 0:
                aprroved.append(1)
        if len(aprroved) == len(k):
            final_list.append(x)
    # print(len(final_list))
    compare(final_list)
    print("{1} result found for {0}".format(line, len(final_list)))


while 1:
    line = input("\nEnter Your Query(q to Quit): ").lower()
    if line == "q":
        break

    inputs = line.split(" ")

    try:
        # for x in table.get(words):
        inputs = normalize(inputs)
        if len(inputs) > 1:
            advanced_search()
        else:
            simple_search(table)
    except Exception as e:
        print(e)
