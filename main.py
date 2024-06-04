import os, requests
from tkinter import *
from tkinter import ttk
from data_check import data_check, data_dir
from collate_data import import_files
from calculate import func2 # placeholder till math functions are coded
from window import new_window, choose_new_faction

def main():
    # check if data folder and contents exist. Download and create them if they are missing
    data_check()
    # import data from files
    armor_values, armors, weapons = import_files()
    # create window
    window, armor_select, faction_select, weapon_select = new_window(armors, armor_values, weapons)

    # TODO: make these functions actually change child comboboxes or displayed data
    # Don't forget to modify combobox grid size if needed
    def choose_new_armor(self):
        print(armor_select.get())

    def choose_new_faction(self):
        print(faction_select.get())

    def choose_new_weapon(self):
        print(weapon_select.get())

    armor_select.bind("<<ComboboxSelected>>", choose_new_armor)
    faction_select.bind("<<ComboboxSelected>>", choose_new_faction)
    weapon_select.bind("<<ComboboxSelected>>", choose_new_weapon)

    window.mainloop()

main()