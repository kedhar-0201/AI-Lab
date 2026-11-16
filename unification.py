
# Unification Algorithm in First-Order Logic

# Check whether a term is a variable
def is_variable(x):
    return isinstance(x, str) and x[0].islower()


# Apply substitutions to a term
def apply_substitution(term, substitution):

    if is_variable(term):
        if term in substitution:
            return apply_substitution(substitution[term], substitution)
        return term

    if isinstance(term, tuple):
        return tuple(apply_substitution(x, substitution) for x in term)

    return term


# Check occurs condition
def occurs(variable, term, substitution):

    term = apply_substitution(term, substitution)

    if variable == term:
        return True

    if isinstance(term, tuple):
        return any(occurs(variable, x, substitution) for x in term)

    return False


# Main unification function
def unify(x, y, substitution=None):

    if substitution is None:
        substitution = {}

    x = apply_substitution(x, substitution)
    y = apply_substitution(y, substitution)

    # If both terms are equal
    if x == y:
        return substitution

    # If x is a variable
    if is_variable(x):

        if occurs(x, y, substitution):
            return None

        substitution[x] = y
        return substitution

    # If y is a variable
    if is_variable(y):

        if occurs(y, x, substitution):
            return None

        substitution[y] = x
        return substitution

    # If both are compound expressions
    if isinstance(x, tuple) and isinstance(y, tuple):

        if len(x) != len(y) or x[0] != y[0]:
            return None

        for a, b in zip(x[1:], y[1:]):
            substitution = unify(a, b, substitution)

            if substitution is None:
                return None

        return substitution

    # Unification failure
    return None


# Main program
print("Unification in First Order Logic")

# Two expressions:
# Knows(x, John)
# Knows(Mary, y)

expr1 = ("Knows", "x", "John")
expr2 = ("Knows", "Mary", "y")

print("\nExpression 1:", expr1)
print("Expression 2:", expr2)

result = unify(expr1, expr2)

if result is not None:
    print("\nUnification Successful!")
    print("Substitution:", result)

    print("\nAfter Substitution:")
    print("Expression 1:", apply_substitution(expr1, result))
    print("Expression 2:", apply_substitution(expr2, result))
else:
    print("\nUnification Failed!")
    print("No valid substitution exists.")
