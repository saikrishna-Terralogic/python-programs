list2 = []
val = "yes"
while val == "yes":
    value = int(input("enter a val"))
    list2.append(value)
    val = input("do u want to enter value to list if yes then enter True else False")
big = list2[0]
for i in list2:
    if big < i:
        big = i

print(big)

