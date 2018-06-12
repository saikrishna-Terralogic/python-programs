import re
s = input("enter the string you want to enter")
p = input("enter the pattern to search in the string")
result = re.match(p, s)
if result.group() == s:
    print("pattern matched")
else:
    print("pattern did not match")

