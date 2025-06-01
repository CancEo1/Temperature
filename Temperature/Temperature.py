# Temperature conversion program
def to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# converting temerature to fahrenheit or celsius 
# This code doesn't run if this module isnt the main module
def main():
    for temp in range (0, 212, 40):
        print(temp, "Fahrenheit =", round(to_celsius(temp)), "Celsius")

    for temp in range(0, 100, 20):
        print(temp, "Celsius =", round(to_fahrenheit(temp)), "Fahrenheit")

# if this module is the main module, call the main() function
# to test the other functions
if __name__ == "__main__":
    main()