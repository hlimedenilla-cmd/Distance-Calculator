#Distance from Kilometers to Miles

#Asks for the distance
kilometer = float(input("Enter the distance in kilometers: "))

#This is the number multiplied to the kilometer variable to get the distance in miles
factor_mile = 0.621371

#This gets the distance in miles
product = kilometer * factor_mile

#Prints the answer
print(f"The distance in miles {product}")

#Asks if we want to convert another distance again
new = input("Do you want to convert another distance (yes/no): ")
if new == "yes":
    new_kilometer = float(input("Enter the distance in kilometers: "))
    new_product = new_kilometer * factor_mile
    print(f"The distance in miles is: {new_product}")
    print("Program ended.")
else:
    print("Program ended.")