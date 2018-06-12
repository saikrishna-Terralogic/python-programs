fb = open("D:\git.txt", "w")
c = True
while c == True:
    str1 = input("input string")
    fb.write(str1)
    fb.write("\n")
    c = input("do you want to continue yes or no")
    if c in ('yes', 'y', 'Yes', 'Y'):
        c=True
    else:
        break
fb.close()
print("write done")

