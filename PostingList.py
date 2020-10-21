
class PostingList:
    def __init__(self, doc_ids):
        self.doc_ids = doc_ids

    def add(self, id):
        self.doc_ids.append(id)

    def sort(self):
        self.doc_ids.sort()

    def size(self):
        return len(self.doc_ids)

    def get(self):
        # print(type(self.doc_ids))
        return self.doc_ids


def and_postinglist(this, other):
    i, j = 0, 0
    result = PostingList(list())
    sort_lists(other, this)
    while i < this.size() and j < other.size():
        a = this.doc_ids[i]
        b = other.doc_ids[j]

        if a == b:
            result.add(a)
            i += 1
            j += 1
        elif a < b:
            i += 1
        else:
            j += 1
    return result.get()


def or_postinglist(this, other):
    i, j = 0, 0
    result = PostingList(list())
    sort_lists(other, this)
    while i < this.size() and j < other.size():
        a = this.doc_ids[i]
        b = other.doc_ids[j]

        if a == b:
            result.add(a)
            i += 1
            j += 1
        elif a < b:
            result.add(a)
            i += 1
        else:
            result.add(b)
            j += 1

        if i == this.size() and j != other.size():
            result.add(b)
            j += 1
        elif i != this.size() and j == other.size():
            result.add(a)
            i += 1

    return result.get()


def not_postinglist(this, other):
    i, j = 0, 0
    result = PostingList(list())
    sort_lists(other, this)
    while i < this.size() and j < other.size():
        a = this.doc_ids[i]
        b = other.doc_ids[j]

        if a == b:
            i += 1
            j += 1
        elif a < b:
            result.add(a)
            i += 1
        else:
            j += 1
    return result.get()


def sort_lists(other, this):
    this.sort()
    other.sort()



# list1 = PostingList([13, 4, 6, 3, 1, 8])
# list1.get()
# list2 = PostingList([6, 5, 4, 8, 12, 22])
# list2.get()
# and_postinglist(list1, list2)
# or_postinglist(list1, list2)
# not_postinglist(list1, list2)
