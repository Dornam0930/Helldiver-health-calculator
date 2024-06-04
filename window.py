from tkinter import *
from tkinter import ttk
factions = ["Helldivers", "Terminids", "Automatons"]

# creates a new window
def new_window(armors, armor_values, weapons):
    window = Tk()
    window.title("Helldiver health calculator")
    window.geometry("1280x720")
    #frame = ttk.Frame(window, padding=10)
    armor_select_label = ttk.Label(window, text="armors:")
    armor_select_label.grid(row=0, column=0, pady=3)
    armor_select = new_dropdown(window, armors, 8, 0, 1, 7, len(armors))
    faction_select_label = ttk.Label(window, text="factions:")
    faction_select_label.grid(row=0, column=1, pady=3)
    faction_select = new_dropdown(window, factions, 30, 1, 1, 1, len(factions))
    weapon_select = ttk.Label(window, text="weapon/enemy:")
    weapon_select.grid(row=0, column=2, pady=3)
    weapon_select = new_dropdown(window, weapons, 30, 2, 1, 1, len(weapons))
    return window, armor_select, faction_select, weapon_select

# creates a new dropdown menu with the specified info
def new_dropdown(window, values, width, location_x, location_y, columns=1, rows=1):
    a = StringVar()
    dropdown = ttk.Combobox(window, width=width, textvariable=a)
    print(type(values))
    if isinstance(values, list):
        dropdown["values"] = values
    elif isinstance(values, dict):
        print(values.keys())
        dropdown["values"] = list(values.keys())
    dropdown.grid(row=location_y, column=location_x, padx=10, pady=5)
    dropdown.current(0)
    return dropdown

# probably going to delete these and implement them in main.py
"""def choose_new_faction(faction):
    if faction == factions[0]:
        pass
    elif faction == factions[1]:
        pass
    elif faction == factions[2]:
        pass"""

"""# updates combobox with new entries based on faction_select
def update_dropdown(faction, weapon_select):
    new_list = weapon_select
    weapon_select["values"] = new_list"""

    