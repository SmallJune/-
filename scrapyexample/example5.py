import urllib2


def text():
    req = urllib2.Request('http://www.baibai.com')

    try:urllib2.urlopen(req)

    except urllib2.URLError, e:
        print e.reason
if __name__ == '__main__':
    text()        