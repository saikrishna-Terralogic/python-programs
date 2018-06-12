str1 = input('enter the elements')
list1 = str1.split()
print(list1)
big = int(list1[0])
small = int(list1[0])
length = len(list1)
sum_value = 0
i = 0
while length > 0:
    if big <= int(list1[i]):
        big = int(list1[i])
    if small > int(list1[i]):
        small = int(list1[i])
    sum_value = sum_value + int(list1[i])
    i = i+1
    length = length-1
print(sum_value-big)
print(sum_value-small)
