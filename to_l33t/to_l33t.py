def to_l33t(string):
    a = ""
    for ch in string:
        c = ch.lower()
        if c == 'a':
            a += "4"
        elif c == 'e':
            a += "3"
        elif c == 'i':
            a += "1"
        elif c == 'o':
            a += "0"
        elif c == 'u':
            a += "8"
        else:
            a += ch
    return a
