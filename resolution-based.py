
# Resolution Algorithm in Propositional Logic

# Function to find the opposite of a literal
def negate(literal):
    if literal.startswith("~"):
        return literal[1:]
    return "~" + literal


# Function to perform resolution
def resolve(c1, c2):
    resolvents = []

    for literal in c1:
        opposite = negate(literal)

        if opposite in c2:
            new_clause = (c1 - {literal}) | (c2 - {opposite})

            # Remove tautological clauses
            if not any(negate(x) in new_clause for x in new_clause):
                resolvents.append(frozenset(new_clause))

    return resolvents


# Resolution algorithm
def resolution(KB, query):

    clauses = [frozenset(c) for c in KB]

    # Add negation of the query
    clauses.append(frozenset([negate(query)]))

    print("\nInitial Clauses:")
    for c in clauses:
        print(c)

    while True:
        new_clauses = set()

        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):

                resolvents = resolve(clauses[i], clauses[j])

                for res in resolvents:

                    if len(res) == 0:
                        print("\nResolvent: Empty Clause (□)")
                        print("Query is PROVED using Resolution!")
                        return True

                    if res not in clauses:
                        new_clauses.add(res)

        if not new_clauses:
            print("\nNo new clauses can be generated.")
            print("Query cannot be proved.")
            return False

        print("\nNew Clauses Generated:")
        for c in new_clauses:
            print(c)

        clauses.extend(new_clauses)


# Knowledge Base in CNF
KB = [
    ["P"],
    ["~P", "Q"],
    ["~Q", "R"]
]

# Given query
query = "R"

print("Knowledge Base:")
print("1. P")
print("2. P -> Q")
print("3. Q -> R")

print("\nQuery:", query)

# Check using resolution
resolution(KB, query)
