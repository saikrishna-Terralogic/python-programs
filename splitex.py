str1 = input('enter the elements')
list1 = str1.split()
print(list1)
big = int(list1[0])
small = int(list1[0])
length = len(list1)
i = 0
while length > 0:
    if big <= int(list1[i]):
        big = int(list1[i])
    i = i+1
    length = length-1
k=0
sum_val = 0
length = len(list1)
while length > 0:
    if big!=int(list1[k]):
        sum_val = sum_val + int(list1[k])
    k = k + 1
    length = length - 1
j = 0
length = len(list1)
while length > 0:
    if small > int(list1[j]):
        small = int(list1[j])
    j = j + 1
    length = length - 1
l = 0
sum_val1 = 0
length = len(list1)
while length > 0:
    if small != int(list1[l]):
        sum_val1 = sum_val1 + int(list1[l])
    l = l + 1
    length = length - 1
print(sum_val)
print(sum_val1)

