def odditer():
    n=1
    while True:
        n=n+2
        yield n
def notdivisible(n):
    return lambda x:x%n>0
def prime():
    yield 2
    it=odditer()
    while True:
        n=next(it)
        yield n
        it=filter(notdivisible(n),it)
for n in prime():
    if n<100:
        print(n)
    else:
        break
    
    
    
