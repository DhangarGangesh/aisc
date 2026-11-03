"""
Experiment 1: Smart Irrigation System using Five AI Agent Models
Models: Simple Reflex, Model-Based Reflex, Goal-Based, Utility-Based, Learning Agent
Based on the second case study in the user's AISC Experiment 1 report.
"""


def simple_reflex_agent(environment):
    print("Initial Soil Moisture:", environment["Moisture"], "%")
    if environment["Moisture"] < 40:
        print("Pump ON")
        environment["Moisture"] += 20
        print("Watering Crops...")
    else:
        print("Pump OFF")
    print("Final Soil Moisture:", environment["Moisture"], "%")


def model_based_agent(environment):
    memory = {}
    memory["Previous Moisture"] = environment["Moisture"]
    print("Previous Moisture:", memory["Previous Moisture"], "%")
    if environment["Moisture"] < 40:
        print("Pump ON")
        environment["Moisture"] += 20
    else:
        print("Pump OFF")
    memory["Current Moisture"] = environment["Moisture"]
    print("Updated Moisture:", memory["Current Moisture"], "%")


def goal_based_agent(environment):
    goal = 60
    print("Goal Moisture:", goal, "%")
    while environment["Moisture"] < goal:
        print("Pump ON")
        environment["Moisture"] += 10
        print("Current Moisture:", environment["Moisture"], "%")
    print("Goal Achieved")
    print("Pump OFF")


def utility_based_agent(environment):
    utility = 0
    print("Initial Moisture:", environment["Moisture"], "%")
    if environment["Moisture"] < 40:
        print("Pump ON")
        environment["Moisture"] += 20
        utility += 10
    else:
        print("Pump OFF")
        utility += 5
    print("Final Moisture:", environment["Moisture"], "%")
    print("Utility Score:", utility)


def performance_element(environment):
    if environment["Moisture"] < 40:
        return "Pump ON"
    return "Pump OFF"


def critic(environment):
    if environment["Moisture"] >= 40:
        return "Good Irrigation"
    return "Need More Water"


def learning_element(memory, feedback):
    memory.append(feedback)


def problem_generator():
    return "Check soil moisture before watering"


def learning_agent(environment):
    memory = []
    print("Initial Soil Moisture:", environment["Moisture"], "%")
    action = performance_element(environment)
    print("Action:", action)
    if action == "Pump ON":
        environment["Moisture"] += 20
        print("Watering Crops...")
    print("Final Soil Moisture:", environment["Moisture"], "%")
    feedback = critic(environment)
    print("Feedback:", feedback)
    learning_element(memory, feedback)
    suggestion = problem_generator()
    print("Suggestion:", suggestion)
    print("Memory:", memory)


if __name__ == "__main__":
    cases = [
        ("1. SIMPLE REFLEX SMART IRRIGATION AGENT", simple_reflex_agent, {"Moisture": 30}),
        ("2. MODEL-BASED REFLEX SMART IRRIGATION AGENT", model_based_agent, {"Moisture": 35}),
        ("3. GOAL-BASED SMART IRRIGATION AGENT", goal_based_agent, {"Moisture": 25}),
        ("4. UTILITY-BASED SMART IRRIGATION AGENT", utility_based_agent, {"Moisture": 30}),
        ("5. LEARNING SMART IRRIGATION AGENT", learning_agent, {"Moisture": 30}),
    ]
    for title, function, environment in cases:
        print("\n" + "=" * 65)
        print(title)
        print("=" * 65)
        function(environment)
