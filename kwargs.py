def myFun(*arg, **kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


#Driver code

myFun("Hi", firt='erick', mid='adikah', last='is my name')