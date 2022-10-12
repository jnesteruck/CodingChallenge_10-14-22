from LinkedList import LinkedList
from challenge import *

lst1 = LinkedList(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
lst2 = LinkedList(['5', '6', '7', '8', '9', 'A', 'B', '0'])
lst3 = LinkedList(['0', '1', '2', '3', '4', '5', '6', '7'])
lst4 = LinkedList([10, 20, 30, 40, 50, 60, 70, 80])

print("\nlst1: ", lst1)
print("lst2: ", lst2)
print("lst3: ", lst3)
print("lst4: ", lst4)

print("\nWhere do lst1 and lst2 intersect? ", intersection(lst1, lst2))
print("Where do lst2 and lst3 intersect? ", intersection(lst1, lst3))

# MODIFY lst1 TO CONTAIN A LOOP
inter = intersection(lst1, lst2)
lst1.tail.next = inter
lst1.tail = None

# PRINT WITH LOOP METHOD, STOP AFTER 20 NODES
print("\nlst1 (modified):  ", end="")
count = 0
for node in lst1:
    if count > 20:
        break
    if node.next is None:
        print(node.value, end="")
    else:
        print(node.value, "-> ", end = "")
    count += 1
print("\nStart of loop in lst1: ", loopDetection(lst1))

print("\nlst2: ", lst2)
count = 0
print("Start of loop in lst2: ", loopDetection(lst2))

# MODIFY lst1 TO CONTAIN A LOOP
count = 0
node4 = None
for node in lst4:
    if count > 2:
        node4 = node
        break
    count += 1
lst4.tail.next = node4
lst4.tail = None

# PRINT WITH LOOP METHOD, STOP AFTER 20 NODES
print("\nlst4 (modified):  ", end="")
count = 0
for node in lst4:
    if count > 20:
        break
    if node.next is None:
        print(node.value, end="")
    else:
        print(node.value, "-> ", end = "")
    count += 1
print()
print("Start of loop in lst4: ", loopDetection(lst4), "\n")