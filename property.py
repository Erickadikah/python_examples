class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
         return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

empl_1 = Employee('john', 'smith')

empl_1.fullname = 'erick adikah'

print(empl_1.first)
print(empl_1.email)
print(empl_1.fullname)

del empl_1.fullname




class Student:


    def setName(self, n):
        self.__name = n

    def getname(self):
        return self.__name

    def setmarks(self, m):
        self.__marks = m

    def getmarks(self):
        return self.__marks


    #user define method.


    def display(self):
        print('Name:', self.getname())
        print('marks:', self.getmarks())

        #object of class.

S = Student()
S.setName('erick')
S.setmarks(85.5)
S.display()


class School:

    pupil = 'higher'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    #getter methods.

    def get_m1(self):
        return self.m1

    #setter method

    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def info(cls):
        return cls.pupil

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3


s1 = School(34, 56, 78)
s2 = School(67, 89, 90)
print(pupil.info())
print(s1.avg()


class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def intro(self):
        print("name:", self.name)
        print("height:", self.height)

per = Person("Rency", 180)
per.intro()

class Student(Person):
    def __init__(self, name, height, age):
        self.age = age
        super().__init__(name, height)
    def stud_intro(self):
        print("name:", self.name)
        print("height:", self.height)
        print("age:", self.age)
print()
stud = Student("tom", 150, 34)
stud.stud_intro()
print()
stud.intro()
