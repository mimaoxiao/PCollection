# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
import urllib.request

def addmodel(name,count):

    num=name[0:8]

    print("reading page from id "+num)
    url = 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id=27372812'
    res = urllib.request.urlopen(url=url)
    print("reading complete, start reading information")

    soup = BeautifulSoup(res.read(),"lxml")

    title=soup.find('div',class_="userdata").h1.string #标题

    x=soup.find_all('span',class_="views") #浏览与赞
    visit=x[0].string
    like=x[1].string

    decoration=(soup.find('div',id="caption_long").string) #图片描述

    userrow=soup.find('div',class_="userdata-row") #用户名 主页 发布日期
    user=userrow.h2.a.string
    userpage=userrow.h2.a['href']
    date=userrow.span.string

    print("reading information complete, start generating html")

    pic=open("template/pic.html","r",encoding='UTF-8').read() #图片模版

    puserdata=open("template/userdata.html","r",encoding='UTF-8').read() #描述模版

    pid=open("template/pid.html","r",encoding='UTF-8').read() #PID模版
    
    picHtml=pic.replace('pic-name',name) #html 图片部分

    temp=puserdata.replace('template-date',date) #html 描述部分
    temp=temp.replace('template-userpage',userpage)
    temp=temp.replace('template-title',title)
    temp=temp.replace('template-user',user)
    temp=temp.replace('template-decoration',decoration)
    temp=temp.replace('template-like',like)
    temp=temp.replace('template-visit',visit)
    puserdataHtml=temp

    pidHtml=pid.replace('pixivid',num) #html pid部分

    print("generating html complete")

    now=picHtml+puserdataHtml+pidHtml
    return now

print("start reading picture")

number=-1
fileing=os.walk("pic")
now=""
for root, dirs, files in fileing:
    for fileiii in files:
        number=number+1
        now+=addmodel(files[number],number+1)

print("reading picture complete, start generating PCollection.html")

number=number+1
midcontrol="<div class=\"text-center mid-control row\" id=\"control\">1/"+str(number)+"</div>"

f1=open("template/head.html","r",encoding='UTF-8')
headhtml=f1.read()
f2=open("template/foot.html","r",encoding='UTF-8')
foothtml=f2.read()
f1.close()
f2.close()

result=headhtml+midcontrol+now+"<script>var maxpos="+str(number)+"</script>"+foothtml

f3=open("PCollection.html","w",encoding='UTF-8')
f3.write(result)
print("mission complete")




