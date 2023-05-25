import os


def delete_file(file_path):
    os.remove(file_path)


file_path = input("Enter the file path: ")
delete_file(file_path)
