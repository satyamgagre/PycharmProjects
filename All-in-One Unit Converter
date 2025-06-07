def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def sqft_to_sqm(sqft):
    return sqft * 0.092903

def sqm_to_sqft(sqm):
    return sqm * 10.7639

def kg_to_lb(kg):
    return kg * 2.20462

def lb_to_kg(lb):
    return lb / 2.20462

def liters_to_gallons(liters):
    return liters * 0.264172

def gallons_to_liters(gallons):
    return gallons / 0.264172

def acres_to_hectares(acres):
    return acres * 0.404686

def hectares_to_acres(hectares):
    return hectares / 0.404686

def main():
    while True:
        print("\n=== Unit Converter ===")
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")
        print("3. Celsius to Fahrenheit")
        print("4. Fahrenheit to Celsius")
        print("5. Square Feet to Square Meters")
        print("6. Square Meters to Square Feet")
        print("7. Kilograms to Pounds")
        print("8. Pounds to Kilograms")
        print("9. Liters to Gallons")
        print("10. Gallons to Liters")
        print("11. Acres to Hectares")
        print("12. Hectares to Acres")
        print("0. Exit")

        choice = input("Enter your choice (0-12): ")

        if choice == '1':
            km = float(input("Enter distance in kilometers: "))
            print(f"{km} km = {km_to_miles(km):.2f} miles")

        elif choice == '2':
            miles = float(input("Enter distance in miles: "))
            print(f"{miles} miles = {miles_to_km(miles):.2f} kilometers")

        elif choice == '3':
            c = float(input("Enter temperature in Celsius: "))
            print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")

        elif choice == '4':
            f = float(input("Enter temperature in Fahrenheit: "))
            print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")

        elif choice == '5':
            sqft = float(input("Enter area in square feet: "))
            print(f"{sqft} sqft = {sqft_to_sqm(sqft):.2f} square meters")

        elif choice == '6':
            sqm = float(input("Enter area in square meters: "))
            print(f"{sqm} sqm = {sqm_to_sqft(sqm):.2f} square feet")

        elif choice == '7':
            kg = float(input("Enter weight in kilograms: "))
            print(f"{kg} kg = {kg_to_lb(kg):.2f} pounds")

        elif choice == '8':
            lb = float(input("Enter weight in pounds: "))
            print(f"{lb} lb = {lb_to_kg(lb):.2f} kilograms")

        elif choice == '9':
            liters = float(input("Enter volume in liters: "))
            print(f"{liters} liters = {liters_to_gallons(liters):.2f} gallons")

        elif choice == '10':
            gallons = float(input("Enter volume in gallons: "))
            print(f"{gallons} gallons = {gallons_to_liters(gallons):.2f} liters")

        elif choice == '11':
            acres = float(input("Enter area in acres: "))
            print(f"{acres} acres = {acres_to_hectares(acres):.2f} hectares")

        elif choice == '12':
            hectares = float(input("Enter area in hectares: "))
            print(f"{hectares} hectares = {hectares_to_acres(hectares):.2f} acres")

        elif choice == '0':
            print("Thanks for using the Unit Converter. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 0 and 12.")

# Run the converter
main()