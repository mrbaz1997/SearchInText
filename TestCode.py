from time import time
from xml.etree import ElementTree as et
import re
import Normalize
from InvertedIndex import NormalizedInvertedIndex as index
from Document import Document
import DocumentStore


def spend_time(job, _start_time):
    return "{}: {:0.3f} seconds".format(job, _start_time)


def get_id_name(_word):
    print("Title\tID")
    for item in _word:
        print(Document.get_doc_id(DocumentStore.get(item)),
              Document.get_name(DocumentStore.get(item)))
    print("{1} result found for {0}".format(line, len(_word)))


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

# def Normal_process(phrase):
#     phrase = Normalize.harekat.sub('', phrase)
#     phrase = Normalize.vav_hamze_pat.sub('و', phrase)
#     phrase = Normalize.yeh_hamze_pat.sub('ی', phrase)
#     phrase = Normalize.alef.sub('ا', phrase)
#     phrase = Normalize.heh_hamze_pat.sub('ه', phrase)
#     phrase = re.sub(r'([A-Z])', lambda pat: pat.group(1).lower(), phrase)
#
#     return phrase


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
normalization_time = [0, 0]
Tokenization_time = [0, 0]
indexing_time = [0, 0]
for child in root:  # read abstract tags
    id = iterator_count.__str__()  # every abstract has an ID (Auto Increment)
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
print(iterator_count)

print(spend_time("Tokenize", Tokenization_time[1]))
print(spend_time("Normalize", normalization_time[1]))
print(spend_time("Indexing", indexing_time[1]))

# print(table)
while 1:
    line = input("\nEnter Your Query(q to Quit): ").lower()
    if line == "q":
        break

    words = line.split(" ")

    try:
        # for x in table.get(words):
        words = normalize(words)
        get_id_name(table.get(words[0]))
    except Exception as e:
        print(e)
