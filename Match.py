# gender = input("Please enter your gender: ")


# match gender.upper():
#     case 'FEMALE':
#         print('User is girl')
#     case 'MALE' | 'BOY':
#         print('User is boy')    
#     case _:
#         print("I don't know you")

x = 1

while x <= 10:
    print(f'Number is {x}')
    x += 1
    
    if x % 5 == 0:
        break;