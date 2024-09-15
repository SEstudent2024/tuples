# 1. Tuple Mastery in Python
# Objective: The aim of this assignment is to deepen your understanding of tuples in Python.

# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. 
# Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
# The function should format and return a string that lists each itinerary. 
# For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, 
# the output should be a string formatted as:

# Itinerary 1: Alice - From New York to London
# Itinerary 2: Bob - From Tokyo to San Francisco

def format_flight_itineraries(itineraries):
    formatted_itineraries = []

    for index, itinerary in enumerate(itineraries):
        traveler_name, origin, destination = itinerary
        formatted_itineraries.append(
            f"Itinerary {index + 1}: {traveler_name} - From {origin} to {destination}"
        )

    return "\n".join(formatted_itineraries)

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

formatted_output = format_flight_itineraries(itineraries)
print(formatted_output)