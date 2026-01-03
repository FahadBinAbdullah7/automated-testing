def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def convert_fahrenheit_to_celsius(f):
    if f < -459.67:  # absolute zero in Fahrenheit
        raise AssertionError("Temperature below absolute zero")
    return (f - 32) * 5 / 9
