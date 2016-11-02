def extendlist(val,list=[]):
    list.append(val)
    return list
list1=extendlist(10)
list2=extendlist(123,[])
list3=extendlist('a')
print(list1)
print(list2)
print(list3)
