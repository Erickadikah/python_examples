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