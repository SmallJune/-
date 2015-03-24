import urllib2

def test():
    req = urllib2.Request('http://www.google.com')

    try: urllib2.urlopen(req)

    except urllib2.URLError, e:
        print e.reason

if __name__ == '__main__':
    test()