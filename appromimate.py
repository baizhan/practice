a={1000:['kb','mb','gb','tb','pb','eb','zb','yb'],1024:['kib','mib','tib','pib','eib','zib','yib']}
def c(size,b=True):
    if size<0:
        raise ValueError('number must be non-negative')
    multiple=1024 if b else 1000
    for suffix in a[multiple]:
        size=size/multiple
        if size<multiple:
            return('{0:.1f}{1}'.format(size,suffix))
        raise ValueError('number too large')
    if __name__=='__main__':
        print(c(1000000000000,False))
        print(c(1000000000000))
        
