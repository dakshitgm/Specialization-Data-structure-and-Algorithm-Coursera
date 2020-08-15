# python3


class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == "check":
            self.ind = int(query[1])
        else:
            self.s = query[1]


class node:
    def __init__(self, str):
        self.str = str
        self.next = None


class lst:
    def __init__(self):
        self.next = None


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [lst() for _ in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print("yes" if was_found else "no")

    def write_chain(self, chain):
        print(" ".join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            strs = []
            next_ref = self.elems[query.ind]
            while next_ref.next != None:
                next_ref = next_ref.next
                strs.append(next_ref.str)
            self.write_chain(strs)
        else:
            hash_ind = self._hash_func(query.s)
            found = None
            next_ref = self.elems[hash_ind]
            while next_ref.next != None:
                if query.s == next_ref.next.str:
                    found = next_ref
                    break
                next_ref = next_ref.next
            if query.type == "add" and found == None:
                st_node = node(query.s)
                st_node.next = self.elems[hash_ind].next
                self.elems[hash_ind].next = st_node
            elif query.type == "find":
                self.write_search_result(found != None)
            elif query.type == "del" and found != None:
                found.next = found.next.next

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == "__main__":
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
