rules = {
    "dirty": "clean",
    "obstacle": "move_left",
    "clear": "move_forward"
}

state = "unknown"
action = None

def update_state(state, action, percept, model):
    return percept

def rule_match(state, rules):
    if state in rules:
        return rules[state]
    return "do_nothing"

def model_based_reflex_agent(percept):
    global state, action
    state = update_state(state, action, percept, None)
    action = rule_match(state, rules)
    return action

percepts = ["dirty", "clear", "obstacle", "clear"]

for percept in percepts:
    print("Percept:", percept)
    print("Action:", model_based_reflex_agent(percept))
