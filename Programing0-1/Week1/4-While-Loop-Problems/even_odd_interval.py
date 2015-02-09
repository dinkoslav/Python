start = input("Enter a number to start from: ")
end = input("Enter a number to end with: ")
start = int(start)
end = int(end)
if start < end:
    while start <= end:
        if start % 2 == 0:
            print(str(start) + " - even")
        else:
            print(str(start) + " - odd")
        start = start + 1
elif start > end:
    while end <= start:
        if end % 2 == 0:
            print(str(end) + " - even")
        else:
            print(str(end) + " - odd")
        end = end + 1
else:
    if end % 2 == 0:
            print(str(end) + " - even")
    else:
            print(str(end) + " - odd")
