for n in range(1,1000):
    b=[]
    i=n-1
    while i>0:
        if n//i==n/i:
            a=n//i
            b.append(a)
           
    i=i-1
    k=0
    for i in b:
        k+=i
    if k==n:
        print(k)
        
            
