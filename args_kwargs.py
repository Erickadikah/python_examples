#args and kwargs combined
def myFun(*args, **kwargs):
    print("args:", args)
    print("kwargs", kwargs)

#we are using both *args , **kwargs
# to pass arguments to this function:


myFun('Erick', 'is', 'adikah', firstname="Erick", lastname="Adikah", lastlast="is the name")