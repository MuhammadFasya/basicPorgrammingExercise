#Take two strings as input and concatenate them. Print the resulting string.
#let user input the first name and also make it as string
firstString = str(input("Input your first word: "))

#let user input the last name and also make it as string
lastString = str(input("Input your last word: "))

#concatenate them
fullWord = str(firstString + " " + lastString)

#print the result
print("result :",fullWord)