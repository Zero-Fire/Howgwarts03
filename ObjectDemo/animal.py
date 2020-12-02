# -*- coding: utf-8 -*-
class Animal:
    name: str = None
    color: str = None
    age: int = None
    gender: str = None

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender

    def run(self):
        print(f'{self.name} will run')

    def call(self):
        print(f'{self.name} will cry')


class Cat(Animal):
    hair: str = '短毛'

    def __init__(self, hair, name, color, age, gender):
        self.hair = hair
        super().__init__(name, color, age, gender)

    def catch(self):
        print(f'{self.name} will catch mice')
        print(f'猫的名字是{self.name},它的颜色是{self.color},它的年龄是{self.age},它的性别是{self.gender},它的毛发是{self.hair},抓到老鼠了')

    def call(self):
        print(f'{self.name}会喵喵叫')


class Dog(Animal):
    hair: str = '长毛'

    def __init__(self, hair, name, color, age, gender):
        self.hair = hair
        super().__init__(name, color, age, gender)

    def watchdog(self):
        print(f'狗的名字是{self.name},它的颜色是{self.color},它的年龄是{self.age},它的性别是{self.gender},它的毛发是{self.hair}')

    def call(self):
        print(f'{self.name}会汪汪叫')


Tom = Cat("短毛", 'Tom', 'black', 2, 'female')
Jerry = Dog('长毛', 'Jerry', 'yellow', 3, 'male')
if __name__ == '__main__':
    Tom.catch()
    Jerry.watchdog()
