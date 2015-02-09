n = input("Enter first number: ")
m = input("Enter second number: ")
n = int(n)
m = int(m)
lastNumOfN = n % 10
lastNumOfM = m % 10
if lastNumOfN > lastNumOfM:
    print(n)
elif lastNumOfN < lastNumOfM:
    print(m)
else:
    if n > m:
        print(n)
    elif n < m:
        print(m)
    else:
        print("Numbers are equal!")
