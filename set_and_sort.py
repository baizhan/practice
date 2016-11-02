a=['bb','a','ccc','ff','e','a','bb']
b=list(set(a))
b.sort(key=a.index)
print(b)
