"""
Experiment 1: Different AI Agent Models - Vacuum Cleaner Case Study
Models: Simple Reflex, Model-Based Reflex, Goal-Based, Utility-Based, Learning Agent
Based on the user's AISC Experiment 1 report.
"""

from copy import deepcopy


def simple_reflex_agent(environment):
    """Uses only the current room percept and IF-THEN rules."""
    for room in ["A", "B"]:
        print(f"\nVacuum is in Room {room}")
        if environment[room] == "Dirty":
            print(f"Room {room} is Dirty. Cleaning...")
            environment[room] = "Clean"
            print(f"Room {room} is now Clean.")
        else:
            print(f"Room {room} is already Clean.")
    print("\nFinal Environment:", environment)


def model_based_reflex_agent(environment):
    """Maintains an internal model of the room conditions."""
    model = {}
    for room in ["A", "B"]:
        model[room] = environment[room]
        print(f"\nVacuum is in Room {room}")
        print("Memory:", model)
        if model[room] == "Dirty":
            print(f"Room {room} is Dirty. Cleaning...")
            environment[room] = "Clean"
            model[room] = "Clean"
            print(f"Room {room} is now Clean.")
        else:
            print(f"Room {room} is already Clean.")
    print("\nInternal Model:", model)
    print("Final Environment:", environment)


def goal_based_agent(environment):
    """Acts until the goal state (both rooms clean) is achieved."""
    goal = {"A": "Clean", "B": "Clean"}
    print("Goal:", goal)
    for room in ["A", "B"]:
        print(f"\nChecking Room {room}")
        if environment[room] != goal[room]:
            print(f"Room {room} is Dirty. Cleaning...")
            environment[room] = "Clean"
        else:
            print(f"Room {room} already satisfies the goal.")
    if environment == goal:
        print("\nGoal Achieved!")
    print("Final Environment:", environment)


def utility_based_agent(environment):
    """Assigns utility values to cleaning and avoiding unnecessary cleaning."""
    utility = 0
    for room in ["A", "B"]:
        print(f"\nVacuum is in Room {room}")
        if environment[room] == "Dirty":
            print(f"Cleaning Room {room}")
            environment[room] = "Clean"
            utility += 10
        else:
            print(f"Room {room} is already Clean")
            utility += 5
    print("\nFinal Environment:", environment)
    print("Utility Score:", utility)


def performance_element(environment):
    actions = []
    for room in ["A", "B"]:
        if environment[room] == "Dirty":
            actions.append(f"Clean Room {room}")
            environment[room] = "Clean"
        else:
            actions.append(f"Room {room} already Clean")
    return actions, environment


def critic(environment):
    if all(state == "Clean" for state in environment.values()):
        return "Good Performance: All rooms are clean."
    return "Poor Performance: Some rooms are still dirty."


def learning_element(memory, feedback):
    memory.append(feedback)
    print("\nLearning from Feedback...")
    print("Feedback Stored:", feedback)


def problem_generator():
    print("\nProblem Generator:")
    print("Suggestion: Next time check the dirtiest room first to improve efficiency.")


def learning_agent(environment):
    memory = []
    print("Initial Environment:", environment)
    actions, environment = performance_element(environment)
    print("\nActions Performed:")
    for action in actions:
        print(action)
    feedback = critic(environment)
    print("\nCritic:", feedback)
    learning_element(memory, feedback)
    problem_generator()
    print("\nFinal Environment:", environment)
    print("Agent Memory:", memory)


if __name__ == "__main__":
    print("=" * 65)
    print("1. SIMPLE REFLEX VACUUM CLEANER AGENT")
    print("=" * 65)
    simple_reflex_agent({"A": "Dirty", "B": "Clean"})

    print("\n" + "=" * 65)
    print("2. MODEL-BASED REFLEX VACUUM CLEANER AGENT")
    print("=" * 65)
    model_based_reflex_agent({"A": "Dirty", "B": "Dirty"})

    print("\n" + "=" * 65)
    print("3. GOAL-BASED VACUUM CLEANER AGENT")
    print("=" * 65)
    goal_based_agent({"A": "Dirty", "B": "Dirty"})

    print("\n" + "=" * 65)
    print("4. UTILITY-BASED VACUUM CLEANER AGENT")
    print("=" * 65)
    utility_based_agent({"A": "Dirty", "B": "Clean"})

    print("\n" + "=" * 65)
    print("5. LEARNING VACUUM CLEANER AGENT")
    print("=" * 65)
    learning_agent({"A": "Dirty", "B": "Dirty"})
