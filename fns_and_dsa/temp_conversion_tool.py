FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = input("Enter the temperature to convert: ")
if not temperature.replace('.', '', 1).isdigit():
    raise ValueError("Invalid temperature. Please enter a numeric value.")
temperature = float(temperature)

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "F":
    converted = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted}°C")
elif unit == "C":
    converted = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted}°F")
else:
    raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
