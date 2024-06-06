from tkinter import *
from tkinter import ttk
from calculate import calc_all_damage

factions = ["Helldivers", "Terminids", "Automatons"]
damage_label_list = []

# creates a new window
def new_window(armors, armor_values, helldivers):
    window = Tk()
    window.title("Helldiver health calculator")
    window.geometry("1280x720")

    input_ui = Frame(window, height=100, width=200)
    input_ui["bg"] = "grey"
    input_ui.grid(row=0, column=0)

    output_ui = Frame(window)
    output_ui["bg"] = "grey"
    output_ui.grid(row=0, column=1)

    armor_select_label = ttk.Label(input_ui, text="armors:")
    armor_select_label.grid(row=0, column=0, pady=3)
    armor_select = new_dropdown(input_ui, armors, 8, 0, 1, 7, len(armors))

    faction_select_label = ttk.Label(input_ui, text="factions:")
    faction_select_label.grid(row=0, column=1, pady=3)
    faction_select = new_dropdown(input_ui, factions, 20, 1, 1, 1, len(factions))

    weapon_select_label = ttk.Label(input_ui, text="weapon/enemy:")
    weapon_select_label.grid(row=0, column=2, pady=3)
    weapon_select = new_dropdown(input_ui, helldivers, 20, 2, 1, 1, len(helldivers))

    attack_label = ttk.Label(output_ui, text="Attacks:")
    attack_label.grid(row=0, column=3, pady=3)

    attack_value_label = ttk.Label(output_ui, text="Damage values:")
    attack_value_label.grid(row=0, column=4, pady=3)

    hp_label = ttk.Label(output_ui, text="Damage after reductions/remaining hp")
    hp_label.grid(row=0, column=5, pady=1, columnspan=7)

    overall = ttk.Label(output_ui, text="Overall:", width=9)
    overall.grid(row=1, column=5, pady=1)

    explosion = ttk.Label(output_ui, text="Explosion:", width=9)
    explosion.grid(row=1, column=6, pady=1)

    exp_resist = ttk.Label(output_ui, text="Exp resist:", width=9)
    exp_resist.grid(row=1, column=7, pady=1)

    head = ttk.Label(output_ui, text="Head:", width=9)
    head.grid(row=1, column=8, pady=1)

    chest = ttk.Label(output_ui, text="Chest:", width=9)
    chest.grid(row=1, column=9, pady=1)

    arm = ttk.Label(output_ui, text="Arm:", width=9)
    arm.grid(row=1, column=10, pady=1)

    leg = ttk.Label(output_ui, text="Leg:", width=9)
    leg.grid(row=1, column=11, pady=1)

    hp_label_v = ttk.Label(output_ui, text="Damage after reductions with vitality booster/remaining hp")
    hp_label_v.grid(row=3, column=5, pady=1, columnspan=7)

    overall_v = ttk.Label(output_ui, text="Overall:", width=9)
    overall_v.grid(row=5, column=5, pady=1)

    explosion_v = ttk.Label(output_ui, text="Explosion:", width=9)
    explosion_v.grid(row=5, column=6, pady=1)

    exp_resist_v = ttk.Label(output_ui, text="Exp resist:", width=9)
    exp_resist_v.grid(row=5, column=7, pady=1)

    head_v = ttk.Label(output_ui, text="Head:", width=9)
    head_v.grid(row=5, column=8, pady=1)

    chest_v = ttk.Label(output_ui, text="Chest:", width=9)
    chest_v.grid(row=5, column=9, pady=1)

    arm_v = ttk.Label(output_ui, text="Arm:", width=9)
    arm_v.grid(row=5, column=10, pady=1)

    leg_v = ttk.Label(output_ui, text="Leg:", width=9)
    leg_v.grid(row=5, column=11, pady=1)

    return window, armor_select, faction_select, weapon_select, input_ui, output_ui

# creates a new dropdown menu with the specified info
def new_dropdown(frame, values, width, location_x, location_y, columns=1, rows=1):
    a = StringVar()
    dropdown = ttk.Combobox(frame, width=width, textvariable=a)
    if isinstance(values, list):
        dropdown["values"] = values
    elif isinstance(values, dict):
        dropdown["values"] = list(values.keys())
    dropdown.grid(row=location_y, column=location_x, padx=10, pady=5)
    return dropdown

def make_attack_grid(frame, faction, helldivers, weapon, armor_values, armor):
    if faction == factions[0]:
        attack_type = ttk.Label(frame, text=weapon, width=30)
        attack_type.grid(row=1, column=3, pady=3)

        attack_value = ttk.Label(frame, text=helldivers[weapon]["damage"], width=10)
        attack_value.grid(row=1, column=4, pady=3)

        damage = helldivers[weapon].get("damage")
        explosive_damage = helldivers[weapon].get("xdamage")
        explosive_value = ttk.Label(frame, text=f"Exp: {explosive_damage}", width=10)
        explosive_value.grid(row=2, column=4, pady=1)

        # TODO: pipe the damage & remaining hp into the grid for displaying in GUI
        damage_list, damage_listv, remaining_hp, remaining_hpv = calc_all_damage(damage, explosive_damage, armor_values, armor)
        for i in range(7):
            if damage_list[i] == "N/A":
                damage_label_list.append(ttk.Label(frame, text=damage_list[i]))
            else:
                damage_label_list.append(ttk.Label(frame, text=f"{damage_list[i]}/{remaining_hp[i]}"))
            damage_label_list[i].grid(row=2, column=5 + i, pady=1)
        for i in range(7):
            if damage_listv[i] == "N/A":
                damage_label_list.append(ttk.Label(frame, text=damage_listv[i]))
            else:
                damage_label_list.append(ttk.Label(frame, text=f"{damage_listv[i]}/{remaining_hpv[i]}"))
            damage_label_list[i + 7].grid(row=6, column=5 + i, pady=1)

        print(damage_list)
        print(damage_listv)
        print(remaining_hp)
        print(remaining_hpv)

        
        

def fill_attack_values():
    pass

    