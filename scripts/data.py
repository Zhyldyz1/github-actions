import json
import os

# Define the directory path
output_directory = "scripts"

# Define the data to be written to the JSON file
data = {"key": "value", "status": "processed"}

# Create the directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)  # Creates the directory recursively if intermediate directories are missing

# Define the output file path
output_file = os.path.join(output_directory, "python-data.json")

# Write the data to the JSON file
with open(output_file, 'w') as f: # Opens the file in write mode ('w')
    json.dump(data, f, indent=4)  # Writes the JSON data to the file, with indentation for readability

print(f"JSON file '{output_file}' created successfully.")
