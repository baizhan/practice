def avg(*arg):
    l=sorted(arg)
    l.pop(0)
    l.pop(-1)
    ax=0
    for n in l:
        ax=ax+n
    av=ax/len(l)
    return av
