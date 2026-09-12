n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    x = int(input("Enter element: "))
    lst.append(x)

print("Original list:", lst)

pos = int(input("Enter position for insertion: "))
value = int(input("Enter value to insert: "))

lst.insert(pos, value)
print("After insertion:", lst)

pos = int(input("Enter position for deletion: "))

del lst[pos]
print("After deletion:", lst)