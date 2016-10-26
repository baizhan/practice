while True:
    for b in range(5):
        a=int(input('chengfabiao:'))
        if a>20:
            print('%s太大了，浪费时间，请输入一个小点的值'%a)
        elif a<=0:
            print('%s是负数，应该输入正整数'%a)
        else:
            for i in range(1,a):
                for j in range(1,i+1):
                    print('{}x{}={}\t'.format(j,i,i*j),end='')
                print()
    else:
        print('超出次数了')
        break
