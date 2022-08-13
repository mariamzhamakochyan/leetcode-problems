n = int(input("Enter the number: "))
list = []
list1 = []
target = [1, 7]
for i in range(1, target[-1] + 1):
    list.append(i)
    if i  in target:
       list1.append("Push")
    else:
       list1.append("Push")
       list1.append("Pop")
print(list1)
