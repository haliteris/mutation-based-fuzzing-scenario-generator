import json
from datetime import datetime
import os

# Function to read JSON data from a local file
def read_json_from_local(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to fetch all parameters from JSON data recursively
def fetch_all_parameters(data, parent_key='', sep='.'):
    items = []
    if isinstance(data, dict):
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            items.extend(fetch_all_parameters(v, new_key, sep=sep))
    elif isinstance(data, list):
        for i, v in enumerate(data):
            new_key = f"{parent_key}{sep}{i}" if parent_key else str(i)
            items.extend(fetch_all_parameters(v, new_key, sep=sep))
    else:
        items.append((parent_key, data))
    return items

# Enhanced function to change a parameter value, handling different data types
def change_parameter(data, key_path, new_value, sep='.'):
    keys = key_path.split(sep)
    sub_data = data
    for key in keys[:-1]:
        sub_data = sub_data[int(key)] if key.isdigit() else sub_data[key]
    last_key = keys[-1]

    old_value = None
    if last_key.isdigit():
        index = int(last_key)
        if isinstance(sub_data, list) and isinstance(new_value, type(sub_data[index])):
            old_value = sub_data[index]
            sub_data[index] = new_value
        else:
            raise ValueError("New value type does not match the original type.")
    else:
        if isinstance(new_value, type(sub_data[last_key])):
            old_value = sub_data[last_key]
            sub_data[last_key] = new_value
        else:
            raise ValueError("New value type does not match the original type.")
    
    return old_value

# Function to get the current index number for naming files
def get_current_index(directory):
    index_file = os.path.join(directory, 'current_index.txt')
    if os.path.exists(index_file):
        with open(index_file, 'r') as file:
            index = int(file.read().strip())
    else:
        index = 0
    return index

# Function to update the index number for naming files
def update_index(directory, index):
    index_file = os.path.join(directory, 'current_index.txt')
    with open(index_file, 'w') as file:
        file.write(str(index))

# Function to save JSON data to a specified directory with a unique name
def save_json_to_local(data, directory, prefix='logical_scenario', index=None):
    if not os.path.exists(directory):
        os.makedirs(directory)
    if index is None:
        index = get_current_index(directory)
    unique_filename = f"{prefix}_{datetime.now().strftime('%Y%m%d')}_{index}.json"
    file_path = os.path.join(directory, unique_filename)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
    return file_path, index

# Function to log modifications to a specified directory
def log_modification(directory, modification_messages, index=None):
    if not os.path.exists(directory):
        os.makedirs(directory)
    if index is None:
        index = get_current_index(directory)
    log_file_path = os.path.join(directory, f"modification_log_{datetime.now().strftime('%Y%m%d')}_{index}.txt")
    with open(log_file_path, 'w') as log_file:
        for message in modification_messages:
            log_file.write(message + '\n')
    return log_file_path

# Function to list parameters (for debugging)
def list_parameters(data):
    print("\nUpdated Data:", json.dumps(data, indent=2))