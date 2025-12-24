
# [For Loops] are another sort of loop just like the while they will repeat a piece of code at the difference that they don't depend on conditions to terminate

for element in range(1,11):
    print(element)
# No condition has to be met the loop will go through or iterate a range of numbers starting at 1 and finishing at 10 this becomes super useful especially when combined with [Lists]

# [List] for now see them as better variables because where a variable could only store one values lists can store multiple values and of different data types too

inventory = ["Sword","Potion","Map"] # This list represents the content of an inventory in a video game

# Each element in a list has a position,it's index all list has as first element index 0
# Let's say that I would like to print the item at the first position of our list(index: 0)
print(inventory[0])

len(inventory) # The [len()] allows us to know the size or length of a list

inventory.append("Spell") # The [append()] allows us to add an element at the END of a list
print(inventory)

inventory.insert(0,"Water") # The [insert()] allows you to add an element at the position/index of your choice
print(inventory)

inventory.pop() # The [pop()] allows you to remove the last element of a list
print(inventory)

# NOTE: The [list] has way more functions related to it feel free to google it

# Let's now combine our knowledge of Lists and For Loops

for item in inventory:
    print(item)

# This loops looks at all the items in our inventory list then displays them in the console,
# For loops allows us to have a more automated/efficient way of accessing lists