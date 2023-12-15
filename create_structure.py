import json
import sys
import os

if len(sys.argv) != 2:
    print("Correct format: python create_structure.py <structure_json_file_path>")
    sys.exit(1)

structure_json_file_path = sys.argv[1]

try:
    data = json.load(open(structure_json_file_path, "rt"))
    print("JSON data: ", data)
except FileNotFoundError:
    print(f"Error: File not found for path {structure_json_file_path}")
except PermissionError as e:
    print(f"Permission error: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except Exception as e:
    print(f"Error: {e}")





