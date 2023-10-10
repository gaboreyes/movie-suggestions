"""
Rent movie 1, 2, 3, 4, 2...
if movie was not in cache hit the db
if movie was in cache, pull its data from cache

NODE
{
    prev: nodo
    next: nodo
    value: movie from db
    key: movie id
}

Least Recently Used
{
    -----------------------
    movie1: node object,
    movie2: node object,
    movie3: node object
    ----------------------- tengo la movie 4 en cache? -> query db -> update cache
    movie2: node object,
    movie3: node object,
    movie4: node object
    -----------------------
}
"""
class Node:

    def __init__(self, key, value, next=None, prev=None) -> None:
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRU:
    cache = None

    def __init__(self) -> None:
        self.cache = {}
        self.head = Node("head", "head")
        self.tail = Node("tail", "tail")

    # head - tail
    # head <-> movie1 <-> tail
    # head <-> movie2 <-> movie1 <-> tail
    # head <-> movie3 <-> movie2 <-> movie1 <-> tail
    # head <-> movie4 <-> movie3 <-> movie2 <-> tail

    def add_node(self, node): 
        node.next = self.head

        if self.tail.next == None:
            self.head.prev = node
            node.prev = self.tail
            self.tail.next = node
        else:
            aux_head = self.head.prev
            self.head.prev = node
            node.prev = aux_head
            aux_head.next = node

        self.cache[node.key] = node.value

        

lru_cache = LRU()
movie1 = Node("movie1", "movie1 data from db")
lru_cache.add_node(movie1)

print("CACHE: ", lru_cache.cache)
print("HEAD: ", lru_cache.head)
print("TAIL: ", lru_cache.tail)
print("HEAD PREV: ", lru_cache.head.prev)
print("TAIL NEXT: ", lru_cache.tail.next)
print("MOVIE1: ", movie1)
print("MOVIE1 NEXT: ", movie1.next)
print("MOVIE1 PREV: ", movie1.prev)

print('---------------------------------')

movie2 = Node("movie2", "movie2 data from db")
lru_cache.add_node(movie2)

print("CACHE: ", lru_cache.cache)
print("HEAD: ", lru_cache.head)
print("TAIL: ", lru_cache.tail)
print("HEAD PREV: ", lru_cache.head.prev)
print("TAIL NEXT: ", lru_cache.tail.next)
print("MOVIE2: ", movie2)
print("MOVIE2 NEXT: ", movie2.next)
print("MOVIE2 PREV: ", movie2.prev)

print('---------------------------------')

movie3 = Node("movie3", "movie3 data from db")
lru_cache.add_node(movie3)

print("CACHE: ", lru_cache.cache)
print("HEAD: ", lru_cache.head)
print("TAIL: ", lru_cache.tail)
print("HEAD PREV: ", lru_cache.head.prev)
print("TAIL NEXT: ", lru_cache.tail.next)
print("MOVIE3: ", movie3)
print("MOVIE3 NEXT: ", movie3.next)
print("MOVIE3 PREV: ", movie3.prev)
print("MOVIE2: ", movie2)
print("MOVIE2 NEXT: ", movie2.next)
print("MOVIE2 PREV: ", movie2.prev)
print("MOVIE1: ", movie1)
print("MOVIE1 NEXT: ", movie1.next)
print("MOVIE1 PREV: ", movie1.prev)
"""
"""

















"""
operations = [1, 2, 3, 4, 2, 3, 1]
lru_cache = []

for x in operations:
    if x in lru_cache:
        print("skipped io")
        lru_cache.append(x)
        lru_cache.remove(x)
    else:
        print("io to database")
        if len(lru_cache) < 3:
            lru_cache.append(x)
        else:
            lru_cache.pop(0)
            lru_cache.append(x)

    print(lru_cache)
    print('')

"""
