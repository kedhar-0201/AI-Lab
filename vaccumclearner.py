def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    if location == "A":
        return "Move Right"
    return "Move Left"
rooms = {
    "A": "Dirty",
    "B": "Dirty"
}
location = "A"
while True:
    status = rooms[location]
    action = vacuum_agent(location, status)
    print("Location:", location)
    print("Status:", status)
    print("Action:", action)
    print()
    if action == "Suck":
        rooms[location] = "Clean"
    elif action == "Move Right":
        location = "B"
    elif action == "Move Left":
        location = "A"
    if rooms["A"] == "Clean" and rooms["B"] == "Clean":
        print("Both rooms are clean!")
        break
