print("-----LRU running-----")

# TODO: make it work with rented movies for operations
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

LRU
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