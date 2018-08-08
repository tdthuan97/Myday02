def cal(lst):
    n = len(lst)
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted(lst)[n//2]
    else:
        return sum(sorted(lst)[n//2-1:n//2+1])/2.0


x = input("Give me a series of numbers and I will give you their median.\n")
list = []
while x != "":
    list.append(int(x))
    x = input("")
if len(list) == 0:
    print("Error, empty dataset")
else:
    print(cal(list))
