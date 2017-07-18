def sortList(data):
    newList = []
    while data:
        minimum = data[0]  # arbitrary number in list 
        for x in data: 
            if x < minimum:
                minimum = x
        newList.append(minimum)
        data.remove(minimum)    
    return newList


print(sortList([67, 45, 2, 13, 1, 998]))
print(sortList([89, 23, 33, 45, 10, 12, 45, 45, 45]))
