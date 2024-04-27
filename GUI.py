import tkinter as tk
from tkinter import ttk
from aima.logic import *
from exps import activity_kb
from engine import inference_engine

def submit():
    user_profile = {
        "Name": name_entry.get().title(),
        "social_interaction": social_interaction_var.get(),
        "dev": dev_var.get(),
        "ActivityType": activity_type_var.get(),
        "Age": age_var.get(),
        "goalTime": goal_time_var.get(),
        "moneySpendingByMounth": money_spending_var.get(),
        "materialNeeded": material_needed_var.get(),
        "place": place_var.get()

    }
    
    recommendations = inference_engine(activity_kb, user_profile)
    results_text.insert(tk.END, f"Recommended activities for {user_profile['Name']}:\n")
    for act in recommendations:
        print(act)
        results_text.insert(tk.END, f"{act}\n")
    
root = tk.Tk()
root.geometry('600x600')
results_text = tk.Text(root)

# Define options for different criteria
social_interaction_options = ["Alone", "Group"]
dev_options = ["Soul", "Brain", "Body"]
activity_type_options = ["Mental", "Physical"]
age_options = ["Teen", "Adult", "Young"]
goal_time_options = ["Long", "Short"]
money_spending_options = ["Free", "Moderate", "Expensive", "VeryExpensive"]
material_needed_options = ["Minimal", "Moderate", "Expensive"]
place_options = ["Interior", "Exterior"]


# Create GUI elements
name_label = tk.Label(root, text="Name")
name_entry = tk.Entry(root)

social_interaction_label = tk.Label(root, text="Social Interaction")
social_interaction_var = tk.StringVar(root)
social_interaction_var.set("Alone")  # default value
social_interaction_option = ttk.Combobox(root, textvariable=social_interaction_var, values=social_interaction_options)

dev_label = tk.Label(root, text="Development")
dev_var = tk.StringVar(root)
dev_var.set("Soul")  # default value
dev_option = ttk.Combobox(root, textvariable=dev_var, values=dev_options)

activity_type_label = tk.Label(root, text="Activity Type")
activity_type_var = tk.StringVar(root)
activity_type_var.set("Mental")  # default value
activity_type_option = ttk.Combobox(root, textvariable=activity_type_var, values=activity_type_options)

age_label = tk.Label(root, text="Age")
age_var = tk.StringVar(root)
age_var.set("Teen")  # default value
age_option = ttk.Combobox(root, textvariable=age_var, values=age_options)

goal_time_label = tk.Label(root, text="Goal Time")
goal_time_var = tk.StringVar(root)
goal_time_var.set("Long")  # default value
goal_time_option = ttk.Combobox(root, textvariable=goal_time_var, values=goal_time_options)

place_label = tk.Label(root, text="Place")
place_var = tk.StringVar(root)
place_var.set("Interior")  # default value
place_option = ttk.Combobox(root, textvariable=place_var, values=place_options)

money_spending_label = tk.Label(root, text="Money Spending")
money_spending_var = tk.StringVar(root)
money_spending_var.set("Free")  # default value
money_spending_option = ttk.Combobox(root, textvariable=money_spending_var, values=money_spending_options)

material_needed_label = tk.Label(root, text="Material Needed")
material_needed_var = tk.StringVar(root)
material_needed_var.set("Minimal")  # default value
material_needed_option = ttk.Combobox(root, textvariable=material_needed_var, values=material_needed_options)

submit_button = tk.Button(root, text="Submit", command=submit)

# Pack GUI elements
name_label.pack()
name_entry.pack()

social_interaction_label.pack()
social_interaction_option.pack()

dev_label.pack()
dev_option.pack()

activity_type_label.pack()
activity_type_option.pack()

age_label.pack()
age_option.pack()

goal_time_label.pack()
goal_time_option.pack()

place_label.pack()
place_option.pack()

money_spending_label.pack()
money_spending_option.pack()

material_needed_label.pack()
material_needed_option.pack()

submit_button.pack()
results_text.pack()

root.mainloop()
