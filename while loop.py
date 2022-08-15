num = 1
sum = 0
print("enter a number. please eneter zero(0) to exit")
while num != 0:
    num = float(input("number?"))
    sum = sum + num
    print("sum = ", sum)
else:
    print("finished sum")
