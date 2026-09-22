import random
#this is the commnet 
numbers = [random.randint(1, 100) for _ in range(20)]

print("List:", numbers)
print("Even numbers:", [num for num in numbers if num % 2 == 0])
