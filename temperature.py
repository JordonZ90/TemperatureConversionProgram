def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) / 1.8 + 273.15
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = kelvin * 1.8 - 459.67
    return fahrenheit
