# Akwaanya Cruise Ticketing
# Stage 4: serve visitors, reject impossible ages, and work out the results from a list

# A list remembers many values in one variable, in the order they were added.
# [] is an empty list: nothing in it yet.
# This list is now our only record: one price per valid visitor.
prices = []

# "while True" repeats forever, so we need break to get out of it.
while True:
    # We keep the entry as text first, so we can check for "q"
    # BEFORE converting to a number. int("q") would crash.
    entry = input("Enter the visitor's age (or q to finish): ")

    # The stop word: break leaves the loop immediately.
    if entry == "q":
        break

    # Now it's safe to convert the text to a whole number.
    age = int(entry)

    # Stage 3: reject impossible ages.
    # "or" is true when EITHER side is true: negative, or over 120.
    if age < 0 or age > 120:
        print("Invalid age, please try again")
        # continue skips the rest of this round and jumps back to the top
        # of the loop, so an invalid visitor is not priced or added to the list.
        continue

    # Same checks as Stage 1, but we store the price instead of printing it,
    # so we can add it to the list afterwards.
    if age <= 5:
        price = 0
    elif age <= 17:
        price = 30
    elif age <= 59:
        price = 60
    else:
        price = 40

    print("Ticket price: GHS", price)

    # append() adds one item to the END of the list.
    prices.append(price)

# This runs only after the loop has ended.
# len() counts the items in the list, so it equals the number of valid visitors.
print("Visitors served:", len(prices))

# sum() adds up all the numbers in the list.
print("Total collected: GHS", sum(prices))

# Printing a list shows all its items inside square brackets.
print("All prices:", prices)