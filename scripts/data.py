import json
import os

output_directory = "scripts"


data = {"key": "value", "status": "processed"}


if not os.path.exists(output_directory):
    os.makedirs(output_directory)  # Creates the directory recursively if intermediate directories are missing

output_file = os.path.join(output_directory, "python-data.json")


with open(output_file, 'w') as f: 
    json.dump(data, f, indent=4)  

print(f"JSON file '{output_file}' created successfully.")
