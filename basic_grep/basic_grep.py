def basic_grep(text, stri):
    my_list = text.split("\n")
    s = ""
    list = []
    for i in range(len(stri)):
        while i < len(stri) and stri[i] != '$' and stri[i] != '^':
            s += stri[i]
            i += 1
        if s != "":
            print(i)
            list.append(s)
            s = ""
    result = [item for item in my_list if any(x in item for x in list)]
    return result
