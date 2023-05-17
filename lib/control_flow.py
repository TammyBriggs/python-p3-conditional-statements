#!/usr/bin/env python3

def admin_login(username, password):
    if username == "ADMIN" or username == "admin" and password == "12345":
        print("Access granted")
    else:
        print("Access denied")
    pass

def hows_the_weather(temperature):
    if temperature < 40:
        print("It's brisk out there!")
    elif temperature >= 40 and temperature <= 65:
        print("It's a little chilly out there!")
    elif temperature > 85:
        print("It's too dang hot out there!")
    else:
        print("It's perfect out there!")
    pass

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
    pass

def calculator(operation, num1, num2):
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        print(num1 / num2)
    else:
        print("Invalid operation!")
        print(None)
    pass
