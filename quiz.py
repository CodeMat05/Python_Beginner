# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# celsiusTemp = float(input('Enter the Temperature in Celsius: '))
# fahrenheit_temp = celsius_to_fahrenheit(celsiusTemp)
# print(f'{celsiusTemp}°C is equal to {fahrenheit_temp}°F')


# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):  # Only check up to √n
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(99))  
# print(is_prime(37)) 

# def factorial(x):
#     if x == 0 or x == 1:
#         return 1
#     return x * factorial(x - 1)

# print(factorial(6))

# words = ["mathien", "hadji", "ali", "samad"]
# upper_Case = map(lambda words: words.upper(), words)

# print(list(upper_Case))

# 

# from functools import reduce

# numbers = [2, 2, 2, 2, 2]
# product = reduce(lambda x, y: x * y, numbers)

# print(product)