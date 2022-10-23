def myFun(arg1, *argv):
    print("first argument : ", arg1)
    for arg in argv:
        print("next argument through *argv :", arg)

myFun('hello', 'my', 'name', 'is', 'Erick Adikah')
