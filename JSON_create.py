import base64
import json


def read_binary_file(path_to_file):
    with open(path_to_file, "rb") as file:
        binary_data = file.read()
        return base64.b64encode(binary_data).decode("utf-8")


path_to_photo = 'C:\\Users\\Public\\Pictures\\wallpapers\\andrew-neel-jtsW--Z6bFw-unsplash.jpg'
path_to_pdf = 'C:\\Users\\gabri\\Downloads\\Configurare_Retea_Lab_11_SI.pdf'

json_data = {
    "documents": {
        "personal": {
            "file1.txt": {
                "content": "Personal document 1",
                "encoding": "utf-8"
            },
            "file2.txt": {
                "content": "Personal document 2",
                "encoding": "utf-8"
            }
        },
        "school": {
            "projects": {
                "project1": {
                    "file3.txt": {
                        "content": "Content1 for project 1.",
                        "encoding": "utf-8"
                    },
                    "file4.txt": {
                        "content": "Content2 for project 1.",
                        "encoding": "utf-8"
                    }
                },
                "project2": {
                    "file5.txt": {
                        "content": "Content1 for project 2.",
                        "encoding": "utf-8"
                    },
                    "file6.txt": {
                        "content": "Content2 for project 2.",
                        "encoding": "utf-8"
                    }
                }
            },
            "homework": {
                "file7.txt": {
                    "content": "Homework1.",
                    "encoding": "utf-8"
                },
                "file8.txt": {
                    "content": "Homework2.",
                    "encoding": "utf-8"
                }
            }
        },
        "file_document.pdf": {
            "content": read_binary_file(path_to_pdf),
            "encoding": "base64"
        }
    },
    "images": {
        "old": {
            "2010": {
                "photo1.jpg": {
                    "content": read_binary_file(path_to_photo),
                    "encoding": "base64"
                }
            },
            "2015": {
                "photo3.png": {
                    "content": read_binary_file(path_to_photo),
                    "encoding": "base64"
                }
            }
        }
    }
}


try:
    s = json.dumps(json_data)
    open("C:\\Users\\gabri\\Desktop\\Generate-structure---Python-Project\\structure.json", "wt").write(s)
except IOError as e:
    print(f"Error writing to file: {e}")
except Exception as e:
    print(f"Error: {e}")
