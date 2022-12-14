class Student:
    def __init__(self, name, age):
        # private member
        self.name = name
        self.age = age

    # getter method
    def get_age(self):
        return self.__age

    # setter method
    def set_age(self, age):
        self.__age = age

stud = Student('Jessa', 14)

# retrieving age using getter
print('Name:', stud.name, stud.get_age())

# changing age using setter
stud.set_age(16)

# retrieving age using getter
print('Name:', stud.name, stud.get_age())

stud.name = "Jessica"
print(stud.name)
stud.__age = 15
print(stud.__age)

