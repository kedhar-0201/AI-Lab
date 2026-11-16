
from itertools import product

# Evaluate logical expressions
def evaluate(expr, model):

    if isinstance(expr, str):
        return model[expr]

    op = expr[0]

    if op == "NOT":
        return not evaluate(expr[1], model)

    elif op == "AND":
        return evaluate(expr[1], model) and evaluate(expr[2], model)

    elif op == "OR":
        return evaluate(expr[1], model) or evaluate(expr[2], model)

    elif op == "IMPLIES":
        return (not evaluate(expr[1], model)) or evaluate(expr[2], model)

    elif op == "IFF":
        return evaluate(expr[1], model) == evaluate(expr[2], model)


# Define propositions
symbols = ["P", "Q", "R", "S"]

# Create Knowledge Base
KB = [
    "P",
    ("IMPLIES", "P", "Q"),
    ("IMPLIES", "Q", "R")
]

# Define query
query = "R"

# Check entailment
def entails(KB, query, symbols):

    for values in product([True, False], repeat=len(symbols)):

        model = dict(zip(symbols, values))

        # Check whether all KB statements are true
        if all(evaluate(sentence, model) for sentence in KB):

            print("Model:", model)

            # Check the query
            if not evaluate(query, model):
                print("Query is False")
                return False

    return True


# Display Knowledge Base
print("Knowledge Base:")
for statement in KB:
    print(statement)

print("\nQuery:", query)

# Display result
if entails(KB, query, symbols):
    print("\nResult: KB entails the Query")
else:
    print("\nResult: KB does NOT entail the Query")
