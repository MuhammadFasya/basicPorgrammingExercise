#Write a program that compares two integers and prints whether they are equal, greater, or smaller
while True:
    try:
        #let user input number
        integer1 = int(input("input your number :"))
        integer2 = int(input("input your second number :"))
        if integer1 == integer2:
            print("same")
        elif integer1 > integer2:
            print("first number bigger than second number")
        else:
            print("second number bigger than first number")
            #stop looping
        break
    
    #if the input is not integer, show wrong input message and loop back to the input
    except ValueError:
        print("The input is wrong, please input an integer value.")