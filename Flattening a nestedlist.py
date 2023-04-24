#one way
#my_list = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]] output is:[1, 2, 3, 4, [5, 6], 7, 8, 9, [10]]
#for the below list the method is working and giving output:[1, 2, 3, 4, 5, 6, 7]
my_list=my_list = [[1], [2, 3], [4, 5, 6, 7]]
new_list=[]
for k in my_list:
    if type(k) is list:
        for l in k:
            new_list.append(l)
    else:
        new_list.append(k)
print(new_list)
#another way
from functools import reduce

from functools import reduce

my_list = [[1], [2, 3], [4, 5, 6, 7]]
print(reduce(lambda x, y: x+y, my_list))

#another way working for my_list = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]],output:[1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
for k in my_list:
    if type(k) is list:
        for l in k:
            if type(l) is list:
                for s in l:
                    new_list.append(s)
            else:
                new_list.append(l)
    else:
        new_list.append(k)
print(new_list)
#using lambda function
flatten = lambda x: [i for row in x for i in row]
lst = [[3,2,1], [4,5,6], [7,8,9]]
out = flatten(lst)
print(out)
#dictionary to list
d = {'python': 0, 'pool': 1}
l = []
for k in d:
    l.append(k)
    l.append(d[k])
print(l)

# Alternative
l = [i for n in [(k, z) for k, z in d.items()] for i in n]
print(l)


