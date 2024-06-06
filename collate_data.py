import json, os, csv
from data_check import data_dir, file_path
from calculate import hitboxes
from decimal import Decimal
valid_file_types = [".csv", ".json"]

def import_files():
    file_list = os.listdir(data_dir)
    for file in file_list:
        file_type = check_file_type(file)
        if file_type[1] not in valid_file_types:
            raise Exception(f"{file} is not a valid file type")
        if file_type[1] == ".csv":
            armor_values = convert_csv_to_dict(file)
            armors = []
            for armor in armor_values:
                if armor[-1] == "V":
                    break
                armors.append(armor)
        if file_type[1] == ".json":
            helldivers = convert_json_to_dict(file)
        terminids = {"term_placeholder1" : {"attack1" : 10, "attack2" : 20}}
        automatons = {"auto_placeholder1" : {"attack1" : 10, "attack2" : 20}}
    return armor_values, armors, helldivers, terminids, automatons

def check_file_type(file):
    return os.path.splitext(file)

# opens a json file and passes it to convert_list_to_dict
def convert_json_to_dict(file):
    path = file_path(data_dir, file)
    with open(path) as json_file:
        file_list_of_dicts = json.load(json_file)
        file_dict_of_dicts = convert_list_to_dict(file_list_of_dicts)
    return file_dict_of_dicts

# returns a dict of dicts with <weaponfullname> being the key
def convert_list_to_dict(json_file):
    dict_of_dicts = {}
    for item in json_file:
        if item == json_file[0]:
            continue
        dict_of_dicts[item["fullname"]] = item
    return dict_of_dicts

# returns a dict of dicts with <armorvalue> and <armorvalueV> (for vitality booster) being the key
def convert_csv_to_dict(csv_file):
    dict_of_dicts = {}
    path = file_path(data_dir, csv_file)
    with open(path, mode="r") as csv_file:
        file_list_of_dicts = csv.DictReader(csv_file)
        vitality = False
        for line in file_list_of_dicts:
            line_copy = convert_strings_to_floats(line)
            if line["Armor"] == "w/Vitality":
                vitality = True
                continue
            if vitality == False:
                dict_of_dicts[line["Armor"]] = line_copy
            else:
                dict_of_dicts[f'{line["Armor"]}V'] = line_copy
    return dict_of_dicts

def convert_strings_to_floats(line):
    if line[hitboxes[1]] == hitboxes[1]:
         return line
    line_copy = line
    for hitbox in hitboxes:
        line_copy[hitbox] = float(Decimal(line_copy[hitbox].rstrip("%")) / 100)
    return line_copy