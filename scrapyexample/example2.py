# coding=utf-8
import urllib
import urllib2
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

def text():
    url = 'http://www.someserver.com/register.cgi'
    values = {'name' : 'WHY',
              'location' : 'SDU',
              'language' : 'Python' }
    data = urllib.urlencode(values) # 编码工作
    req = urllib2.Request(url, data)  # 发送请求同时传data表单
    # response = urllib2.urlopen(req)  #接受反馈的信息
    # the_page = response.read()  #读取反馈的内容
    print data
    print req

if __name__ == '__main__':
    text()