d = {'a':1, 'b':2, 'c':2, 'd': 0}
keys = list(d.keys())
# for i in range(len(keys)):
#     print(d[keys[i]], "nice")
d_sort = sorted(d.items())
for k in d.keys():
    print(d[k]) # this returns value
print("-----------")
for i in d_sort:
    print(i[1])