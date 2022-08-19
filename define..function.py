# adding two values
def sum(arg1, arg2):
    if type(arg1) != type(arg2):
        print("please give args of the same type")
        return
    print(arg1 + arg2)


sum(15, 60)
sum('Hello', '  world')
sum(15.647, 80.258)
sum("")
