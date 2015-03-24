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
    data = {}

    data['name'] = 'WHY'
    data['location'] = 'SDU'
    data['language'] = 'Python'

    url_values = urllib.urlencode(data)
    print url_values


if __name__ == '__main__':
    text()