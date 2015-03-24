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
    url = 'http://test1.lovewith.me/u/ajax/get/album_share'
    values = {'aid' : 3,
              'page' : 1,}
    data = urllib.urlencode(values)
    log(data)
    full_url = url + '?' + data
    log(full_url)
    response = urllib2.urlopen(full_url)
    data = response.read()
    print data

if __name__ == '__main__':
    text()