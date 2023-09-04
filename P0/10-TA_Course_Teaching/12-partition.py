def partition(collection: list):
    if len(collection) == 1:
        print(collection)
        yield [collection]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[first] + subset] + smaller[n + 1:]
        # put `first` in its own subset
        yield [[first]] + smaller



something = list(range(1, 4))

for n, p in enumerate(partition(something), 1):
    print(n, sorted(p))
