
class Node:

    def __init__(self, key, value, next=None, prev=None) -> None:
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class LRU:
    cache = {}
    cache_size = 0

    def __init__(self, cache_size=3) -> None:
        self.cache_size = cache_size
        self.head = Node("head", "head")
        self.tail = Node("tail", "tail")

    def remove(self, node) -> None:
        """ Removes the given node from cache """
        self.cache.__delitem__(node.key)
    
    def detach(self, node) -> None:
        """ Breaks all the links for the given node """
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        node.next = None
        node.prev = None

    def prepend(self, node) -> None:
        """ Adds a node at the start of the cache """
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def update(self, node) -> None:
        """ Given a node it moves it to the start of the cache following cache rules """
        if self.cache.get(node.key):
            print(f"{node.key} - Existe en cache, chekear si es el primero")
            if self.head.next == node:
                print(f"{node.key} - Es el primero, no se hace mas nada!")
            else:
                print(f"{node.key} - NO es el primero, detach it, move it de primero")
                self.detach(node)
                self.prepend(node)
        else:
            print(f"{node.key} - No existe en cache, add it de primero")
            
            if len(self.cache) == self.cache_size:
                print(f"{node.key} - CACHE ESTA LLENA, detach {self.tail.prev.key} y add {node.key} de primero")
                self.remove(self.tail.prev)
                self.detach(self.tail.prev)
                self.prepend(node)
            else:
                if self.head.next == None:
                    print(f"La Head apunta a Tail, add {node.key} de primero")
                    node.next = self.tail
                    node.prev = self.head
                    self.head.next = node
                    self.tail.prev = node
                else:
                    print(f"La Head no apunta a Tail, romper enlaces y add {node.key} de primero")
                    self.prepend(node)

            self.cache[node.key] = node.value

lru_cache = LRU(3)
movie1 = Node("movie1", "movie1 data from db")
movie2 = Node("movie2", "movie2 data from db")
movie3 = Node("movie3", "movie3 data from db")
movie4 = Node("movie4", "movie4 data from db")
movie3 = Node("movie3", "movie3 data from db")
movie3 = Node("movie3", "movie3 data from db")

lru_cache.update(movie1)
lru_cache.update(movie2)
lru_cache.update(movie3)
lru_cache.update(movie4)
lru_cache.update(movie3)
lru_cache.update(movie3)


print('---------------------------------------------------------------------------------------------------')
print("CACHE: ", lru_cache.cache)
print("HEAD: ", lru_cache.head, "HEAD NEXT: ", lru_cache.head.next)
print("TAIL: ", lru_cache.tail, "TAIL PREV: ", lru_cache.tail.prev)
print("MOVIE1: ", movie1, "NEXT: ", movie1.next, "PREV: ", movie1.prev)
print("MOVIE2: ", movie2, "NEXT: ", movie2.next, "PREV: ", movie2.prev)
print("MOVIE3: ", movie3, "NEXT: ", movie3.next, "PREV: ", movie3.prev)
print("MOVIE4: ", movie4, "NEXT: ", movie4.next, "PREV: ", movie4.prev)

"""
if lru_cache.head.next == movie4 and movie4.next == movie3 and movie3.next == movie2 and movie2.next == lru_cache.tail:
    print("True forwards")
else:
    print("False forwards")

if lru_cache.tail.prev == movie2 and movie2.prev == movie3 and movie3.prev == movie4 and movie4.prev == lru_cache.head:
    print("True backwards")
else:
    print("False backwards")

    
if lru_cache.head.next == movie3 and movie3.next == movie4 and movie4.next == movie2 and movie2.next == lru_cache.tail:
    print("True forwards")
else:
    print("False forwards")

if lru_cache.tail.prev == movie2 and movie2.prev == movie4 and movie4.prev == movie3 and movie3.prev == lru_cache.head:
    print("True backwards")
else:
    print("False backwards")
"""
