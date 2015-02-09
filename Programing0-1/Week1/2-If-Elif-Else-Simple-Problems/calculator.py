a = input("Enter a: ")
b = input("Enter b: ")
oper = input("Enter operation: ")

a = int(a)
b = int(b)

print("Result is:")
if oper == "+":
    print(a+b)
elif oper == "-":
    print(a-b)
elif oper == "*":
    print(a*b)
elif oper == "/":
    print(a/b)
else:
    print("We do not support that operation.")
