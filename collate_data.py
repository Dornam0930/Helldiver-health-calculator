import json, os, csv
from data_check import data_dir, file_path
valid_file_types = [".csv", ".json"]

def import_files():
    file_list = os.listdir(data_dir)
    for file in file_list:
        file_type = check_file_type(file)
        if file_type[1] not in valid_file_types:
            raise Exception(f"{file} is not a valid file type")
        if file_type[1] == ".csv":
            armor_values = convert_csv_to_dict(file)
        if file_type[1] == ".json":
            weapons = convert_json_to_dict(file)
    return armor_values, weapons

def check_file_type(file):
    return os.path.splitext(file)

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
            print(line)
            if line["Armor"] == "w/Vitality":
                vitality = True
                continue
            if vitality == False:
                dict_of_dicts[line["Armor"]] = line
            else:
                dict_of_dicts[f'{line["Armor"]}V'] = line
    return dict_of_dicts