#append
swamy=[2,1,2,3,4,5,6]
swamy.append("raju")
print(swamy)

#extend
chandu=[0,9,8,7,6,5]
chandu.extend(['vasa',1,2,3])
print(chandu)

#copy
v=chandu.copy()
print(v)

#clear
chandu.clear()
print(chandu)

#count
chandu=(1,4,2,3,4,5)
chandu.count(4)
print(chandu.count(4))

#index
chandu=(1,4,2,3,4,5)
print(chandu.index(1))


#pop
lis=[1,2,3,4,5,6,7]
lis.pop(4)
print(lis)

#insert
chandu=[1,2,3,4,5,6,7,8]
chandu.insert(2,"gopi")
print(chandu)

#remove
chandu=[1,2,3,4,5,6,7]
chandu.remove(2)
print(chandu)

#reverse
chandu=[1,2,3,4,5,6]
chandu.reverse()
print(chandu)

#sort
chandu.sort()
print(chandu)

# #list comprehensivess
# ANIMALS=["LION","TIGER","deer","elephant","wolf"]
# newlist[x for x in ANIMALS if "a" in x]
# print(newlist)