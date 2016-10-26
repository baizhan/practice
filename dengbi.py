for n in range(1,200):
    sq=n*n
    str_sq=str(sq)
    istr_sq=str_sq[::-1]
    if str_sq==istr_sq:
        print(n)
        
