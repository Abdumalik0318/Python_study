name = input("What is your name? ")
age = int(input("How old are you? "))
goal = input("What is your career goal? ")

print(f"Hello {name}!")

if age < 20:
    print("You are starting very young - huge advantage for you!")
elif age < 30:
    print("Perfct age to make a career change!")
else:
    print("It is never too late to start!")

if "informatiker" in goal.lower():
    print("Great goal! The IT market in Germamy is boomingg")
else:
    print(f"Nice goal! Work hard and you will get there. ")