"""
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
    -----------------------
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

    def detach(self, node) -> None:
        """ Breaks all the links for the given node and removes it from cache"""
        self.cache.__delitem__(node.key)
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        node.next = None
        node.prev = None

    def update(self, node) -> None:
        if self.cache.get(node.key):
            print(f"{node.key} - Existe en cache, chekear si es el primero")
            if self.head.next == node:
                print(f"{node.key} - Es el primero, no se hace mas nada!")
            else:
                print(f"{node.key} - NO es el primero, move it de primero")
        else:
            print(f"{node.key} - No existe en cache, add it de primero")
            
            if len(self.cache) == 3:
                print(f"{node.key} - CACHE ESTA LLENA, detach {self.tail.prev.key}")
                self.detach(self.tail.prev)
                node.next = self.head.next
                node.prev = self.head
                self.head.next.prev = node
                self.head.next = node

            else:
                if self.head.next == None:
                    print(f"La Head apunta a Tail, add {node.key} en el medio")
                    node.next = self.tail
                    node.prev = self.head
                    self.head.next = node
                    self.tail.prev = node
                else:
                    print(f"La Head no apunta a Tail, romper enlaces y add {node.key} de primero")
                    node.next = self.head.next
                    node.prev = self.head
                    self.head.next.prev = node
                    self.head.next = node

            self.cache[node.key] = node.value

        # if true and IS NOT the first, break links for the head.prev node, update node to the start
        # if true and IS the first, no need to update anything
        # if false check if cache is full,
        # if full, remove the oldest node, break links for the head.prev, append node to the start
        # if NOT full, break links for the head.prev, append node to the start

        """
        node.next = self.head

        if self.tail.next is None:
            self.head.prev = node
            node.prev = self.tail
            self.tail.next = node
        else:
            if len(self.cache.keys()) == 3:
                print('NO MORE ROOM...')
                self.detach(self.tail.next)

            aux_head = self.head.prev
            self.head.prev = node
            node.prev = aux_head
            aux_head.next = node

        self.cache[node.key] = node.value
        """


lru_cache = LRU()
movie1 = Node("movie1", "movie1 data from db")
movie2 = Node("movie2", "movie2 data from db")
movie3 = Node("movie3", "movie3 data from db")
movie4 = Node("movie4", "movie4 data from db")
movie3 = Node("movie3", "movie3 data from db")

lru_cache.update(movie1)
lru_cache.update(movie2)
lru_cache.update(movie3)
lru_cache.update(movie4)
lru_cache.update(movie3)


print('---------------------------------------------------------------------------------------------------')
print("CACHE: ", lru_cache.cache)
print("HEAD: ", lru_cache.head, "HEAD NEXT: ", lru_cache.head.next)
print("TAIL: ", lru_cache.tail, "TAIL PREV: ", lru_cache.tail.prev)
print("MOVIE1: ", movie1, "NEXT: ", movie1.next, "PREV: ", movie1.prev)
print("MOVIE2: ", movie2, "NEXT: ", movie2.next, "PREV: ", movie2.prev)
print("MOVIE3: ", movie3, "NEXT: ", movie3.next, "PREV: ", movie3.prev)
print("MOVIE4: ", movie4, "NEXT: ", movie4.next, "PREV: ", movie4.prev)