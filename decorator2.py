def log(func):
    def a(*args,**kw):
        print('start call %s():'%func.__name__)
        return func(*args,**kw)
    return a
@log
def f():
    print('2016-3')
    print('end call')
f()
