#Remove Duplicates from a List: [1, 2, 3, 4, 2, 3, 5, 6, 1]
my_list = [1, 2, 3, 4, 2, 3, 5, 6, 1]
final_list = []
for num in my_list:
    if num not in final_list:
        final_list.append(num) 

print("Original List: ", my_list)
print("Removed duplicate from list: ", final_list)