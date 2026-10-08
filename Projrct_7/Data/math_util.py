import math


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def calculate_log(number):
    if number <= 0:
        return "Number must be greater than zero"
    return math.log(number)


def calculate_power(base, exponent):
    return base ** exponent