import requests
import re
class spider(object):
    def __init__(self):
        print('开始爬取内容。。。')
    def getsource(self,url):
        html=requests.get(url)
        return html.text
    def changepage(self,url,total_page):
        now_page=int(re.search('(\d+)&filter=',url,re.S).group(1)
        page_group=[]
        for i in range(now_page,total_page+1):
            link=re.sub('\d+&filter=','%s&filter='%i*25,url,re.S)
            pagegroup.append(link)
        return page_group
    def geteveryclass(self,source):
        everyclass=re.findall('<ol class="grid_view">.*?</ol>',source,re.S)
        return everyclass
    def getinfo(self,eachclass):
        info={}
        info['片名']=re.search('<span class="title">(.*?)</span>',eachclass,re.S)
        info['导演']=re.search('<p class="">(.*?)&nbsp;',eachclass,re.S)
        info['主演']=re.search(';&nbsp;&nbsp;主演:(.*?)/...<br>',eachclass,re.S)
        info['评分']=re.search('<span property="v:best" content="(.*?)"></span>',eachclass,re.S)
        info['人数']=re.search('<span property="v:best" content="10.0"></span><span>(.*?评价</span>',eachclass,re.S)
        return info
    def saveinfo(self,classinfo):
        f=open('info.txt','a')
        for each in classinfo:
            f.writelines('片名:'+each['片名']+'\n')
            f.writelines('导演:'+each['导演']+'\n')
            f.writelines('主演:'+each['主演']+'\n')
            f.writelines('评分:'+each['评分']+'\n')
            f.writelines('人数:'+each['人数']+'\n')
        f.close()
if __name__=='__main__':
    classinfo=[]
    url='https://movie.douban.com/top250?start=0&filter='
    donggespider=spider()
    all_links=donggespider.changepage(url,10)
    for link in all_links:
        print('正在处理页面:'+link)
        html=donggespider.getsource(link)
        everyclass=donggespider.geteveryclass(html)
        for each in everyclass:
            info=donggespider.getinfo(each)
            classinfo.append(info)
        donggespider.saveinfo(classinfo)
