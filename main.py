import os, requests
from data_check import data_check, data_dir
from collate_data import import_files
from calculate import func2 # placeholder till math functions are coded

def main():
    # check if data folder and contents exist. Download and create them if they are missing
    data_check()
    armor_values, weapons = import_files()

main()