no_of_test_cases = int(input("enter the number of test cases"))
for i in range(no_of_test_cases):
    a = input('enter the first input')
    b = input('enter the second input')
    try:
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as v:
        print("Error Code:", v)
    else:
        print('no error')


