from timeit import Timer

x=list(range(2000000))
pop_zero=Timer('x.pop(0)','from __main__ import x')
print('pop_zero',pop_zero.timeit(number=1000),'millsseconds')

x=list(range(2000000))
pop_end=Timer('x.pop()','from __main__ import x')
print('pop_end',pop_end.timeit(number=1000),'milliseconds')


