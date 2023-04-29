import os
import json

# Save raw weather data as a JSON file in the specified folder.
def save_data(data, filename, folder='raw', data_type='raw'):
    folder_path = os.path.join(folder, data_type)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, filename)

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
