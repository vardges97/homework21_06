def common_member(a, b):
    listA = set(a)
    listB = set(b)

    if len(listA.intersection(listB)) > 0:
        return (listA.intersection(listB))
    else:
        return ("no common elements")


a = [1, 2, 3, 4, 5, 6]
b = [5, 6, 7, 8, 9]
print(common_member(a, b))

