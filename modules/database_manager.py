import json

def write_to_file(file_name:str,data):
    with open(f"{file_name}",'w') as write_file:
        json.dump(data,write_file,indent=4)

def read_file(file_name:str):
    with open(f"{file_name}",'r') as read_file:
        data = json.load(read_file)
    return data