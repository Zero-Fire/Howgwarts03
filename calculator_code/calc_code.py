# -*- coding: utf-8 -*-
class Calculator:

    def add(self,a,b):
        if (type(a) !=int and type(a) !=float) or (type(b)!=int and type(b) !=float):
            return '请输入数字'
        return a+b

    def sub(self,a,b):
        if (type(a) !=int and type(a) !=float) or (type(b)!=int and type(b) !=float):
            return "请输入数字"
        return a - b

    def mul(self,a,b):
        if (type(a) !=int and type(a) !=float) or (type(b)!=int and type(b) !=float):
            return "请输入数字"

    def div(self,a,b):
        if (type(a) !=int and type(a) !=float) or (type(b)!=int and type(b) !=float):
            return "请输入数字"
        elif b==0:
            return 'ZeroDivisionError'
        else:
            return a/b


a=Calculator()
print(a.div(1,1))
# print(a.div(0,1))
