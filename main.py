import os, requests
from tkinter import *
from tkinter import ttk
from data_check import data_check, data_dir
from collate_data import import_files
from calculate import func2 # placeholder till math functions are coded
from window import new_window, make_attack_grid, factions


def main():
    # check if data folder and contents exist. Download and create them if they are missing
    data_check()
    # import data from files
    armor_values, armors, helldivers, terminids, automatons = import_files()
    # create window
    (window,
     armor_select,
     faction_select,
     weapon_select,
     input_ui,
     output_ui) = new_window(armors, armor_values, helldivers)
    armor_select.current(0)
    faction_select.current(0)
    weapon_select.current(0)
    make_attack_grid(output_ui, factions[0], helldivers, weapon_select.get(), armor_values, armor_select.get())

    # TODO: make these functions actually change child comboboxes or displayed data
    # Don't forget to modify combobox grid size if needed
    def choose_new_armor(self):
        print(armor_select.get())

    def choose_new_faction(self):
        faction = faction_select.get()
        print(faction)
        if faction == factions[0]:
            weapon_select["values"] = list(helldivers)
        elif faction == factions[1]:
            weapon_select["values"] = list(terminids)
        elif faction == factions[2]:
            weapon_select["values"] = list(automatons)
        weapon_select.current(0)

    def choose_new_weapon(self):
        print(weapon_select.get())
        make_attack_grid(window, faction_select.get(), helldivers, weapon_select.get(), armor_values, armor_select.get())

    armor_select.bind("<<ComboboxSelected>>", choose_new_armor)
    faction_select.bind("<<ComboboxSelected>>", choose_new_faction)
    weapon_select.bind("<<ComboboxSelected>>", choose_new_weapon)

    window.mainloop()

main()