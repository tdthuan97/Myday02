def order_words(array):
    d = {}
    for word in array:
        d.setdefault(len(word), []).append(word)
    result = [d[n] for n in sorted(d)]
    for arr in result:
        arr.sort()
    if len(result) == 0:
        return [[]]
    return result
