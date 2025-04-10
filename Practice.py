
# entry = input('Please Enter your age: ')
# age = int(entry)
# print(f'Thank you for telling me. You are {age} years olds.')

# if (age < 10) and (age > 0):
#     print("You are too young")
# elif (False) or 0 > 1:
#     pass
# else:
#     print(
#         'You are old enough'
#     )

# isFemale = input('Are you Lady? Y / N: ')
# match isFemale:
#     case 'Y' | 'y':
#         print("Hello Ma'am")
#     case 'N' | 'n' | _:
#         print('Hello Sir')

# maximum = 10
# minimum = 1

# coll = {
#     1: 'a', 
#     2: 'b', 
#     3: 'c',
#     1: 'z'
#     }

# for item in coll:
#     print(item)
# print(coll[1], coll[2])

# minimum = 2
# maximum = 10

# coll = range(minimum, maximum + 1)

# index = 0
# while index < len(coll):
#     print(coll[index])
#     index += 1

# users = {
#     1: 'Luffy',
#     2: 'Zoro',
# }


def addTwoNumbers(x, y):
    return x + y

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

total = addTwoNumbers(num1, num2)
print(f'The sum of {num1} and {num2} is {total}')