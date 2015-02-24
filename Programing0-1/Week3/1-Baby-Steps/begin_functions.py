def square(n):
    return n * n

print(square(2))
print(square(5))

def fact(n):
    sum = 1
    while n != 0:
        sum = sum * n
        n = n - 1
    return sum

print(fact(5))
print(fact(0))
print(fact(6))

def count_elements(items):
    count = 0
    for item in items:
        count = count + 1
    return count

print(count_elements([]))
print(count_elements([1, 2, 3]))

def member(x, xs):
    for s in xs:
        if x == s:
            return True
    return False

print(member(1, [1,2,3]))
print(member("Python", ["Django", "Rails"]))
        
def grades_that_pass(students, grades, limit):
    index = 0
    grades_that_pass = []
    for student in students:
        if grades[index] >= limit:
            grades_that_pass = grades_that_pass + [students[index]]
        index = index + 1
    return grades_that_pass

students = ["Rado", "Ivo", "Maria", "Nina"]
grades = [3, 4.5, 5.5, 6]
result = grades_that_pass(students, grades, 4.0)
print(result)













            
