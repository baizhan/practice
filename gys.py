for i in range(5):
    while True:
        a=int(input('x:'))
        b=int(input('y:'))
        if a>b:
            biger=a
            while True:
                if biger%a==0 and biger%b==0:
                    gys=biger
                    print(gys)
                    break
                else:
                    biger+=1
        else:
            biger=b
            while True:
                if biger%a==0 and biger%b==0:
                    gys=biger
                    print(gys)
                    break
                else:
                    biger+=1
