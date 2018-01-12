x = ["hello", 2, 54, -2,7,12,98,"World"]

def firstlast (x):
    newList = []
    y = len(x) - 1
    newList.append(x[0])
    newList.append(x[y])
    print newList

firstlast(x)