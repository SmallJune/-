# -*- coding:utf-8 -*-
import random

__author__ = 'huangfu'


class ExampleApi:
    def __init__(self):
        pass


    @staticmethod
    def getrandata(num=None):
        a = []
        i = 0
        while i < num:
            a.append(random.randint(0, 10000000))
            i += 1
        return a

    @staticmethod
    def bubbleSort(a=None):
        l = len(a)-2
        i = 0
        while i < l:
            j = l
            while j >= i:
                if(a[j+1]>a[j]):
                    a[j], a[j+1] = a[j+1], a[j]
                j -= 1
            i += 1
        return a