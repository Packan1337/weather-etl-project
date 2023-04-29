import os
import json

# Save raw weather data as a JSON file in the specified folder.
def save_raw_data(data, filename, folder='raw'):
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, filename)

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
