def swaplist(list):
    list[0],list[-1]=list[-1],list[0]
    return list
l=[1,2,3]
print(swaplist(l))