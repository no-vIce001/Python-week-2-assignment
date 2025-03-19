# Creating an empty list called my_list:
my_list = []

# Appending the following items; 10, 20, 30, 40 to my_list: 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# Inserting the value 15 at the second position in the list:
my_list.insert(1, 15)
print(my_list)

# Extending my_list with another list; [50, 60, 70]:
another_list = [50, 60, 70]
my_list.extend(another_list)
print(my_list)

# Removing the last element from my_list:
my_list.remove(70)
print(my_list)

# Sorting my_list in ascending order:
my_list.sort()
print(my_list)

# Finding and printing the index of the value 30 in my_list:
print(my_list.index(30))