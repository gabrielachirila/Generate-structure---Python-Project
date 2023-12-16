import json
import sys
import os
from json import JSONDecodeError

if len(sys.argv) != 3:
    print("Correct format: python create_structure.py  <root_folder_path> <structure_json_file_path>")
    sys.exit(1)


root_folder_path = sys.argv[1]
structure_json_file_path = sys.argv[2]


def save_binary_photo(path, value):
    try:
        photo_file_path = value
        with open(photo_file_path, "rb") as photo_file:
            binary_data = photo_file.read()
        with open(path, "wb") as file:
            file.write(binary_data)
    except FileNotFoundError as e:
        print(f"Error: File not found: {e}")
    except IOError as e:
        print(f"Error I/O: {e}")
    except MemoryError as e:
        print(f"Error memory: {e}")
    except Exception as e:
        print(f"Error: {e}")


def create_structure(root_folder_path, structure):
    for key, value in structure.items():
        new_path = os.path.join(root_folder_path, key)
        if isinstance(value, dict):
            try:
                os.makedirs(new_path, exist_ok=True)
                create_structure(new_path, value)
            except FileNotFoundError as e:
                print(f"Error: File not found: {e}")
            except PermissionError as e:
                print(f"Permission error: {e}")
            except Exception as e:
                print(f"Error: {e}")
        elif isinstance(value, str) and key.endswith(".txt"):
            try:
                with open(new_path, "wt") as file:
                    file.write(value)
            except IOError as e:
                print(f"Error writing to file {new_path}: {e}")
            except Exception as e:
                print(f"Error: {e}")
        elif isinstance(value, str) and key.endswith(".jpg"):
            save_binary_photo(new_path, value)


try:
    data = json.load(open(structure_json_file_path, "rt"))
    print("JSON data: ", data)
    print(data.items())

    create_structure(root_folder_path, data)
except FileNotFoundError as e:
    print(f"Error: File not found: {e}")
except PermissionError as e:
    print(f"Permission error: {e}")
except JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except Exception as e:
    print(f"Error: {e}")
