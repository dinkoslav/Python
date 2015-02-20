p = input("Enter p: ")
p = int(p)


twins = [p-2, p, p+2]
twin_primes = []

for twin in twins:
    count = 2
    is_prime = True
    while count <= twin/2:
        if twin % count == 0:
            is_prime = False
        count = count + 1
    if is_prime == True and twin != 1 and twin != 2:
        twin_primes = twin_primes + [is_prime]
    else:
        twin_primes = twin_primes + [False]

if twin_primes[1] == False:
    print(str(twins[1]) + " is not a prime.")
else:
    print("Twin primes with " + str(twins[1]) + ":")
    if twin_primes[0] == True:
        print(str(twins[0]) + ", " + str(twins[1]))
    else:
        print(str(twins[0]) + " is not")
    if twin_primes[2] == True:
        print(str(twins[2]) + ", " + str(twins[1]))
    else:
        print(str(twins[2]) + " is not")

