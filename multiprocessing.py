from multiprocessing.dummy import Pool
import requests
import time
def getsource(url):
    html=requests.get(url)
urls=[]
for i in range(10):
    newpage='https://movie.douban.com/top250?start=%d&filter='%(i*25)
    urls.append(newpage)
time1=time.time()

for i in urls:
    print(i)
    getsource(i)
time2=time.time()
print('单线程耗时：'+str(time2-time1))
pool=Pool(4)
time3=time.time()
results=pool.map(getsource,urls)
for i in results:
    print(i)
pool.close()
pool.join()
time4=time.time()
print('并行耗时：'+str(time4-time3))
