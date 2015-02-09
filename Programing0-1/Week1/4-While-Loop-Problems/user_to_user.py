start = input("Enter a number to start from: ")
end = input("Enter a number to end with: ")
start = int(start)
end = int(end)
if start < end:
    while start <= end:
        print(start)
        start = start + 1
elif start > end:
    while end <= start:
        print(end)
        end = end + 1
else:
    print(start)
