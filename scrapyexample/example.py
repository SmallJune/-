# coding=utf-8
import urllib2
def kill():
    req = urllib2.Request('http://www.baidu.com')
    response = urllib2.urlopen(req)
    the_page = response.read()
    print the_page

if __name__ == '__main__':
    kill()