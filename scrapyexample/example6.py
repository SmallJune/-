# coding=utf-8
import re
import urllib2
import datetime
import time

def log(content="debug", path='/tmp/test.log', ):
    # logging.basicConfig(level=logging.DEBUG,
    # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #                     datefmt='%a, %d %b %Y %H:%M:%S',
    #                     filename=path,
    #                     filemode='w')
    # logging.info(content)
    fsock = open(path, 'a')
    now = time.strftime("%Y-%m-%d %H %M %S", time.localtime())
    result = '%s--%s\n' % (now, content)
    fsock.write(result)
    fsock.close()
    return result


def findAuthorArticleWithoutLogin(authorId,date1):

    FidList={280:u'计算机技术',119:u'学术民主湖',14:u'江风竹雨',27:u'人文社科',63:u'好摄之徒',17:u'书香重大',
              109:u'外语角',83:u'黄桷树下',123:u'鱼食天下',107:u'鱼游天下',30:u'激情天下',181:u'数码广场',
             18:u'轻松一刻',92:u'老乡会所',195:u'健康大家谈',100:u'心语新缘',234:u'曝光台',103:u'张贴栏',
             138:u'生物学院'
             #203:u'租房',218:u'兼职',180:u'民主湖超市'
             }
    #findAuthorArticle(authorId,100,FidList[100],date1)
    for key in FidList:
       print FidList[key]
       findAuthorArticle(authorId,key,FidList[key],date1)
def findAuthorArticle(authorId,Fid,FidName,date1):
    ###该函数主要用来访问近几年用户，从第一页访问
     pageStart=1#从第一页访问
     pageEnd=500#最多访问500页，结束
     urlstr='http://www.cqumzh.cn/bbs/forumdisplay.php?fid='+str(Fid);
     matchstr='space.php?uid='+str(authorId)
     for i in range(pageStart,pageEnd):
         print u'爬虫爬到第'+str(i)+u'页'
         #合成URL路径
         urlstr2=urlstr+'&page='+str(i)
         #模拟请求网址
         request = urllib2.Request(urlstr2)
         request.add_header('User-Agent', 'fake-client')
         response = urllib2.urlopen(request)
         myPage =response.read()
         #匹配目标内容
         myItems=re.findall('<a title=(.*?)>(.*?)</a></span>.*?<td align="center" style="overflow:hidden"nowrap="nowrap">\r\n<cite>\r\n<a href="(.*?)">(.*?)</a>',myPage,re.S)
         for item in myItems:
          #print item[1]+'authour='+item[2]
          #f.writelines(item[1]+'authour='+item[2]+'\n\r')
             str1=str(item[2])
             #找到目标作者
             if str1 == matchstr :
                 #addr=getWebAdress(item[0])
                 info=item[0].replace('&','&')
                 print FidName+u','+item[1]+','+info
                 #保存到文件
                 f.writelines(str(FidName)+u',第'+str(i)+u'页，'+item[1]+','+info+'\n\r')
         length=len(myItems)
         date2=getItemPage(myItems[length-1][0])
         #print date2
         dderror=date2-date1
         if dderror.days<0:
             return

def getWebAdress(objStr):
             addr=re.findall('.*?href="(.*?)"',objStr,re.S)
             return addr[0]
def getItemPage(objStr):
    mItems=re.findall('\d{4}-\d{1,2}-\d{1,2}',objStr,re.S)
    mdate=datetime.datetime.strptime(str(mItems[0]), "%Y-%m-%d")
    return mdate
if __name__=="__main__":
    #此处输入收缩需要的信息
    authorId=133788

    dtstr = '2011-9-8'
    dd=datetime.datetime.strptime(dtstr, "%Y-%m-%d")
    print u"爬虫开始爬民主湖了 ......"
    f = open('Bid'+str(authorId)+'.txt','w+')
    f.writelines(u"作者"+str(authorId)+u"\n\r")
    findAuthorArticleWithoutLogin(authorId,dd)
    f.close()