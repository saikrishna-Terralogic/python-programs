num_of_ele = int(input("enter the number of list elements"))
mylist1 = []
count=1
while count <= num_of_ele:
    val = int(input("enter the element to the list"))
    mylist1.append(val)
    count=count+1
position = int(input("enter the position you want to enter new element to the list"))
mylist1[position] = int(input("enter the element"))
print(mylist1)
del mylist1[0]
mylist1.append(int(input("enter the element to the list")))
print(mylist1)
mylist1.sort()
print(mylist1)
poppedelement = mylist1.pop()
print(poppedelement)
mylist1.reverse()
print(mylist1)







