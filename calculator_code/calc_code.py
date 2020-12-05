# -*- coding: utf-8 -*-
class Calculator:

    def add(self,a,b):
        return a+b

    def div(self,a,b):
        if b==0:
            return 'ZeroDivisionError'
        else:
            return a/b

# a=Calculator()
# print(a.div(0,1))
