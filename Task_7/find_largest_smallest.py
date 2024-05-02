#Find the Largest and Smallest Number in a List [10, 20, 5, 40, 30, 72, 34]
numbers = [10, 20, 5, 40, 30, 72, 34]
#Variable for Largest and Smallest
largest = numbers[0]
smallest = numbers[0]
#Find the largest and smallest
for num in numbers:
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num
#Final output
print("Largest number: ", largest)
print("Smallest number: ", smallest)
