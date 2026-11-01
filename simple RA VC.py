environment = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

while True:
    print("\nLocation:", location)
    print("Status:", environment[location])

    if environment[location] == "Dirty":
        print("Action: Suck")
        environment[location] = "Clean"

    elif location == "A":
        print("Action: Move Right")
        location = "B"

    elif location == "B":
        print("Action: Move Left")
        location = "A"

    if environment["A"] == "Clean" and environment["B"] == "Clean":
        print("Both locations are clean.")
        break

print("Final environment:", environment)