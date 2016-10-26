def fenjie(n):
    i=n-1
    while i>0:
        if n//i==n/i:
            a=n//i
            print(a)
            return fenjie(i)
        i=i-1
