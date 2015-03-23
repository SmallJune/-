# coding=utf-8
import os, subprocess, signal

def kill():
    proc = subprocess.Popen('ps aux|grep cgi',shell=True,stdout=subprocess.PIPE)
    result = proc.communicate()[0].split('\n')
    for i in result:
        if 'python' in i:
            pid=int(i.split(None)[1])
            os.kill(pid,signal.SIGKILL)
    print 'old process killed\n'
    os.system('python /var/www/lovewith.me/manage.py runfcgi method=threaded host=127.0.0.1 port=9001')
    print 'start service success!'

if __name__ == '__main__':
    kill()