# coding=utf-8
import cookielib
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


def test():
    postdata = urllib.urlencode({
        'username':'汪小光',
        'password':'why888',
        'continueURI':'http://www.verycd.com/',
        'fk':'',
        'login_submit':'登录'
    })
    req = urllib2.Request(
        url = 'http://secure.verycd.com/signin',
        data = postdata
    )
    result = urllib2.urlopen(req)
    print result.read()

if __name__ == '__main__':
    test()