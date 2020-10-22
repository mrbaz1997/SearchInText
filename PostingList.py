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
        return self.doc_ids


def and_postinglist(this, other):
    i, j = 0, 0
    result = PostingList(list())
    sort_lists(other, this)
    while i < len(this) and j < len(other):
        a = this[i]
        b = other[j]

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
    i, j, a, b = 0, 0, 0, 0
    a_over, b_over = False, False
    result = PostingList(list())
    sort_lists(other, this)
    while i < len(this) or j < len(other):
        if i >= len(this):
            a_over = True
        elif j >= len(other):
            b_over = True

        if not a_over:
            a = this[i]
        if not b_over:
            b = other[j]

        if a_over or b_over:
            if not a_over:
                result.add(a)
                i += 1
            else:
                result.add(b)
                j += 1
        else:
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
    return result.get()


def not_postinglist(this, other):
    i, j = 0, 0
    result = PostingList(list())
    sort_lists(other, this)
    while i < len(this) and j < len(other):
        a = this[i]
        b = other[j]

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
    try:
        this.sort()
        other.sort()
    except AttributeError:
        # print("No Match")
        return "No Match"

# list1 = PostingList([13, 4, 6, 3, 1, 8])
# list1.get()
# list2 = PostingList([6, 5, 4, 8, 12, 22])
# list2.get()
# and_postinglist(list1, list2)
# or_postinglist(list1, list2)
# not_postinglist(list1, list2)
