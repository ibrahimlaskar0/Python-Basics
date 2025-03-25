a ={ 1, 2, 3, 4}
b ={3,5,4,77,8}

#a.discard(66) doesnt give any error if there is no 66 to remove but remove . gives error
#print(a)

#print(a.union(b))
#print(a.intersection(b))

# print(a.difference(b)) means subtracting b from a


print(a.isdisjoint(b)) # to chck if there is no elements common in both the set
