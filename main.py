import os, requests
from data_check import data_check

def main():
    #check if data folder and contents exist. Download and create them if they are missing
    data_check()

main()