num = 1
sum = 0
print("enter a number. please eneter zero(0) to exit")
while num != 0:
    num = float(input("number?"))
    sum = sum + num
    print("sum = ", sum)
else:
    print("finished sum")


i = 0

while i < 5:
    print("the value of i is : ", i)
    i += 1  # = i + 1
else:
    print("finished while loop")
