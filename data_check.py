import os, requests

data_repo = "https://raw.githubusercontent.com/zeddidragon/helldivers-calc/main/data/"
data_dir = "./Data"
files_to_retrieve = "files to retrieve.txt"

# main function to check the data folder
def data_check():
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    file_list = open(files_to_retrieve, "r")
    for file in file_list:
        stripped_file = file.strip("\n")
        if stripped_file[0] == "#":
            continue
        data_repo_file_path = html_file_path(data_repo, stripped_file)
        data_dir_file_path = file_path(data_dir, stripped_file)
        if not check_file(data_dir_file_path):
            download_file(data_dir_file_path, data_repo_file_path)

# returns file path for your OS
def file_path(dir_path, file_name):
    return os.path.join(dir_path, file_name)

# returns file path for website download
def html_file_path(dir_path, file_name):
    return f"{dir_path}{file_name}"

# checks if a specified file already exists
def check_file(file_path):
    return os.path.isfile(file_path)

# downloads specified file and writes it to the data folder
def download_file(file_path, repo_path):
    download = requests.get(repo_path)
    new_file = open(file_path, "w")
    new_file.write(download.text)