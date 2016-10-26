from multiprocessing.dummy import Pool
import os
import random
import time
def long_time_task(name):
    print('Run task %s(%s)...'%(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s runs %0.2f seconds'%(name,(end-start)))
if __name__=='__main__':
    print('Parent process %s'%os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task(i))
        print('waiting for all subprocessing done...')
        p.close()
        p.join()
        print('all process done')
    
    
