import tkinter as tk

# Define the expert system rules and facts
rules = {
    "rule1": {"if": ["sunny"], "then": "Wear sunglasses and a hat."},
    "rule2": {"if": ["rainy"], "then": "Grab an umbrella and wear a raincoat."},
    "rule3": {"if": ["cloudy"], "then": "Wear a light jacket."},
    "rule4": {"if": ["cold"], "then": "Dress warmly with a coat and gloves."},
}

# Function to determine the decision using forward chaining
def determine_decision(weather_conditions):
    decision = "No decision found."
    for rule_name, rule in rules.items():
        if all(condition in weather_conditions for condition in rule["if"]):
            decision = rule["then"]
            break
    return decision

# Function to update the decision label
def update_decision():
    weather_conditions = input_entry.get().lower().split()
    decision = determine_decision(weather_conditions)
    decision_label.config(text=decision)

# Create the main application window
app = tk.Tk()
app.title("Weather Decision Expert System")

# Create and configure widgets
input_label = tk.Label(app, text="Enter weather conditions (e.g., sunny rainy):")
input_entry = tk.Entry(app)
decision_label = tk.Label(app, text="Decision will appear here.")
determine_button = tk.Button(app, text="Determine Decision", command=update_decision)

# Arrange widgets on the window
input_label.pack()
input_entry.pack()
determine_button.pack()
decision_label.pack()

# Start the main event loop
app.mainloop()