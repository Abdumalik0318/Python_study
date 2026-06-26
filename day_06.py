groceries = []

print("let's build a grocery list! Type 'done' when finished. ")

item = input("Add an item: ")

while item != "done":
    groceries.append(item)
    item = input("Add an item: ")

print("\nHere is your grocery list:")

for grocery in groceries:
    print(f"- {grocery}")

print(f"\nYou have {len(groceries)} items in your grocery list.")