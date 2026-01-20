'List in python is a built-in data structure that help to store multiple items in a single variable. Lists are ordered, changeable, and allow duplicate values. They are defined by enclosing elements in square brackets [] and separating them with commas.'

#example of list

my_list = [1, 2, 3, "apple", "banana", True, 3.14]'
print(my_list)  # Output: [1, 2, 3, 'apple``

"this list can store different data types including integers, strings, booleans, and floats."
'-------------------------------------------------------------'

#append - (add) method for list:

my_list.append("orange") 
print(my_list)  # Output: [1, 2, 3, 'apple', 'banana', True, 3.14, 'orange'] 

#remove method for list:
my_list.remove(index(2)) #index 2 is number 3
print(my_list)  # Output: [1, 2, 'apple', 'banana', True, 3.14, 'orange']

#pop (it means remove and return) method for list:
popped_item = my_list.pop()  # removes and returns the last item
print(popped_item)  # Output: 'orange'

'this method will be useful when we want to impletement stack data structure in python, which follows LIFO (last in first out) principle.'

#basic example for pop method:
house_types = ("bungalow", "duplex", "apartment", "villa")
popped_house = house_types.pop()  # removes and returns the last item
print(popped_house)  # Output: 'villa'
print(house_types)  # Output: ['bungalow', 'duplex', 'apartment']

#insert method for list:
house_types.insert(1, "cottage")  # inserts 'cottage' at index 1
print(house_types)  # Output: ['bungalow', 'cottage', 'duplex', 'apartment']

