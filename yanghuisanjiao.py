def yanghui(n):
    l=[1]
    if n==1:
        return l
    else:
        l=[1]+[yanghui(n-1)[i]+yanghui(n-1)[i+1] for i in range(n-2)]+[1]
        return l
        
        
