import re
import requests
f=open('e:/new.txt','r')
html=f.read()
f.close()
pic_url=re.findall('lazysrc="(.*?)" alt="',html,re.S)
name=re.findall('alt="(.*?)" /><span>',html,re.S)
i=0
for each in pic_url:
    print('现在正在下载:'+each)
    pic=requests.get(each)
    save_path='e://test/tupian/东哥的女人number%d.jpg'%i
    fp=open(save_path,'wb')
    fp.write(pic.content)
    fp.close()
    i+=1
