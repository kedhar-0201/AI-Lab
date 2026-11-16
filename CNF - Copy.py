
from sympy import symbols
from sympy.logic.boolalg import (
    Implies, And, Or, Not, to_cnf
)

# Define propositional variables
P, Q, R = symbols('P Q R')

print("FIRST ORDER LOGIC TO CNF CONVERSION")
print("-----------------------------------")

# Input logical expression
print("Enter the logical expression:")
print("Example: (P >> Q) & (Q >> R)")

expression = input("Expression: ")

try:
    # Convert input into a logical expression
    result = eval(
        expression,
        {
            "P": P, "Q": Q, "R": R,
            "And": And, "Or": Or,
            "Not": Not, "Implies": Implies
        }
    )

    # Convert expression into CNF
    cnf_result = to_cnf(result, simplify=True)

    print("\nOriginal Expression:")
    print(result)

    print("\nConjunctive Normal Form (CNF):")
    print(cnf_result)

except Exception as e:
    print("Invalid logical expression:", e)
