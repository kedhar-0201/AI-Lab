
# Forward Chaining using First Order Logic

# Step 1: Initialize Knowledge Base with facts
facts = [
    ("Human", "John"),
    ("Human", "Mary")
]

# Step 2: Define rules
# Format: (IF predicate, THEN predicate)
rules = [
    ("Human", "Mortal"),
    ("Mortal", "CanDie")
]

# Step 3: Display Knowledge Base
print("KNOWLEDGE BASE")
print("--------------")

print("Facts:")
for fact in facts:
    print(fact[0] + "(" + fact[1] + ")")

print("\nRules:")
for rule in rules:
    print(rule[0] + "(x) -> " + rule[1] + "(x)")

# Step 4: Get query from user
query = input("\nEnter query (Example: Mortal(John)): ")

# Parse query
predicate, argument = query.replace(")", "").split("(")
query_fact = (predicate.strip(), argument.strip())

# Step 5: Apply Forward Chaining
print("\nFORWARD CHAINING PROCESS")
print("------------------------")

changed = True

while changed:
    changed = False

    for rule in rules:
        body, head = rule

        for fact in facts[:]:
            if fact[0] == body:
                new_fact = (head, fact[1])

                if new_fact not in facts:
                    facts.append(new_fact)
                    changed = True

                    print("Derived:", head + "(" + fact[1] + ")")

# Step 6: Check whether query is proved
print("\nFINAL RESULT")
print("------------")

if query_fact in facts:
    print("Query Proved:", query)
else:
    print("Query Cannot Be Proved:", query)
