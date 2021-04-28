import temperature


def display_menu():
    print("MENU")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Fahrenheit to Kelvin")
    print("4. Kelvin to Fahrenheit")
    print()


def convert_temp():
    option = int(input("Enter a menu option "))
    if option == 1:
        fahrenheit = int(input("Enter degrees in Fahrenheit "))
        celsius = temperature.fahrenheit_to_celsius(fahrenheit)
        celsius = round(celsius, 2)
        print(f"Degrees {celsius} Celsius")
    elif option == 2:
        celsius = int(input("Enter degrees in Celsius "))
        fahrenheit = temperature.celsius_to_fahrenheit(celsius)
        fahrenheit = round(fahrenheit, 2)
        print(f"Degrees {fahrenheit} Fahrenheit")
    elif option == 3:
        fahrenheit = int(input("Enter degrees in Fahrenheit "))
        kelvin = temperature.fahrenheit_to_kelvin(fahrenheit)
        kelvin = round(kelvin, 2)
        print(f"Degrees {kelvin} kelvin")
    elif option == 4:
        kelvin = float(input("Enter degrees in Kelvin "))
        fahrenheit = temperature.kelvin_to_fahrenheit(kelvin)
        fahrenheit = round(fahrenheit, 2)
        print(f"Degrees {fahrenheit} Fahrenheit")
    else:
        print("You must enter a valid menu number")


def main():
    display_menu()
    again = "y"
    while again.lower() == "y":
        convert_temp()
        print()
        again = input("Convert another temperature? (y|n) ")
        print()
    print("Goodbye!")


if __name__ == "__main__":
    main()