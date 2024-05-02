#Reverse a String by input your name
def reverse_string(name):
    reversed_name = ""
    for i in range(len(name) - 1, -1, -1):
        reversed_name += name[i]
    return reversed_name

name = input("Enter your name: ")
reversed_name = reverse_string(name)
print("Reversed name:", reversed_name)