# -*- coding: utf-8 -*-
def addmodel(name,count):
    num=name[0:8]
    head=open("template/modelhead.html","r",encoding='UTF-8').read()
    mid=open("template/modelmid.html","r",encoding='UTF-8').read()
    foot=open("template/modelfoot.html","r",encoding='UTF-8').read()
    now="<div class=\"row pic-content\" id=\""+str(count)+"\">"+head+"<img class=\"pic\" src="+"pic/"+name+">"+mid+"<a href=\"https://www.pixiv.net/member_illust.php?mode=medium&illust_id="+num+"\">pid="+num+"</a>"+foot
    return now

import os

number=-1
fileing=os.walk("pic")
now=""
for root, dirs, files in fileing:
    for fileiii in files:
        number=number+1
        now+=addmodel(files[number],number+1)

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




