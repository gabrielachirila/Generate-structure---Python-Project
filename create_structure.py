import json
import sys
import os
from json import JSONDecodeError
import base64

CHUNK_SIZE = 4096

if len(sys.argv) != 3:
    print("Correct format: python create_structure.py  <root_folder_path> <structure_json_file_path>")
    sys.exit(1)

root_folder_path = sys.argv[1]
structure_json_file_path = sys.argv[2]


def write_content_in_chunks(file, content):
    for i in range(0, len(content), CHUNK_SIZE):
        chunk = content[i:i + CHUNK_SIZE]
        file.write(chunk)


def create_structure(root_folder_path, structure):
    for key, value in structure.items():
        new_path = os.path.join(root_folder_path, key)
        if isinstance(value, dict) and "content" in value.keys() and "encoding" in value.keys():
            try:
                if os.path.exists(new_path):
                    user_input = input(f"The file {new_path} already exists. Do you want to overwrite it? (yes/no): ")
                    if user_input.lower() != 'yes':
                        continue

                if value["encoding"] == "base64":
                    decoded_content = base64.b64decode(value["content"])
                    with open(new_path, "wb") as file:
                        write_content_in_chunks(file, decoded_content)
                elif value["encoding"] in ["utf-8", "utf-16"]:
                    with open(new_path, "wt", encoding=value["encoding"]) as file:
                        write_content_in_chunks(file, value["content"])
                else:
                    raise Exception(f"Error: Unknown encoding: {value['encoding']}")
            except IOError as e:
                print(f"Error writing to file {new_path}: {e}")
            except MemoryError as e:
                print(f"Error memory: {e}")
            except Exception as e:
                print(f"Error: {e}")
        elif isinstance(value, dict):
            try:
                os.makedirs(new_path, exist_ok=True)
                create_structure(new_path, value)
            except FileNotFoundError as e:
                print(f"Error: File not found: {e}")
            except PermissionError as e:
                print(f"Permission error: {e}")
            except Exception as e:
                print(f"Error: {e}")


def process_json_incrementally(json_file):
    decoder = json.JSONDecoder()
    buffer = ""

    while True:
        chunk = json_file.read(CHUNK_SIZE)
        if not chunk:
            break

        buffer += chunk
        try:
            while buffer:
                obj, idx = decoder.raw_decode(buffer)
                buffer = buffer[idx:]
                create_structure(root_folder_path, obj)
        except JSONDecodeError:
            pass


try:
    with open(structure_json_file_path, "rt") as json_file:
        process_json_incrementally(json_file)
except FileNotFoundError as e:
    print(f"Error: File not found: {e}")
except PermissionError as e:
    print(f"Permission error: {e}")
except JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except Exception as e:
    print(f"Error: {e}")
