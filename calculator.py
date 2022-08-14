while True:
    print("1 addition")
    print("2 subtraction")
    print("3 multiplication")
    print("Enter q or Q to exit")

    choice = input("enter your choice : ")

    if choice == 'q' or choice == 'Q':
        break

    num1 = float(input("enter number 1 :"))
    num2 = float(input("enter number 2 :"))

    if choice == "1":
        print(num1, "+", num2, "=", (num1+num2))

    elif choice == "2":
        print(num1, "-", num2, "=", (num1-num2))

    elif choice == "3":
        print(num1, "*", num2, "=", (num1*num2))

    elif choice == "4":
        if num2 == 0.0:
            print("Devide by 0 Error")
    else:
        print(num1, "/", num2, "=", (num1/num2))

else:
    print("invalic choice")
