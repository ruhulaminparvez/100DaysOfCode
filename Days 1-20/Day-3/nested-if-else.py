# Nested if-else and elif 

print("Welcome to the rollercoaster ride!")
height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride rollercoaster!")
    age = int(input("What is your age? "))
    #nested if-else
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sry, you have to grow taller before you can ride.")