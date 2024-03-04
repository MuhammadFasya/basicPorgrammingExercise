#Project 3: Develop a program that checks if a user's age is between 18 and 65 (inclusive) and prints whether they are eligible to vote.
#loop
#loop
while True:
    try:
        #let user to input age
        age = int(input("Input your age here: "))
        
        if (age >= 18 and age <= 65):
        #if age is between 18 and 65
            print(f"Your age is {age}, and you're eligible to vote")
        else:
            print(f"Your age is {age}, and you're not eligible to vote")
        
        #stop looping
        break
    
    except ValueError:
        #if the input is not number, show wrong input message and loop back to the input
        print("Wrong input. Please input number.")