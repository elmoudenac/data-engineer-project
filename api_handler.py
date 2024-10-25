import json


def read_data_from_file(filename):

    with open(filename, 'r') as f:
        data = json.load(f)
    return  data