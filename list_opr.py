list1 = []
print("You can perform :\n   1.insert pos ele 2.print  3.remove ele \n   4.append ele 5.sort 6.pop 7.reverse")
n = input("enter no of commands to perform:\n")
for i in range(int(n)):
    com = input()
    str = com.split()
    #try:
    #    if(str[1] && str[2] != null):
    try:
        if str[0] == "insert":
            list1.insert(int(str[1]),int(str[2]))
        elif str[0] == "print":
            print(list1)
        elif str[0] == "remove":
            list1.remove(int(str[1]))
        elif str[0] == "append":
            list1.append(int(str[1]))
        elif str[0] == "sort":
            list1.sort()
        elif str[0] == "pop":
            list1.pop()
        elif str[0] == "reverse":
            list1.reverse()
        else :
            print("provide only given commands in given syntax")
    except Exception as e:
        print(e)