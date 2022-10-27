#args and kwargs combined
def myFun(*args, **kwargs):
    print("args:", args)
    print("kwargs", kwargs)

#we are using both *args , **kwargs
# to pass arguments to this function:


myFun('Erick', 'is', 'adikah', firstname="Erick", lastname="Adikah", lastlast="is the name")
class car():
    def __init__(self,*args): #args receives unlimited no. of arguments as an array
        self.speed = args[0] #acces args idex like array does
        self.colour=args[1]

#creating object of car class

audi=car(200, 'red')
bmw=car(250, 'balck')
mb=car(190,'white')

print(audi.colour)
print(bmw.speed)

def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("%s == %s" %(key, value))

greet_me(fname="Erick", lname="adikah")


def test_args_kwargs(*argv):
    for arg in argv:
        print(arg)

test_args_kwargs('hello', 'my', 'name', 'is', 'erick', 'adikah')
