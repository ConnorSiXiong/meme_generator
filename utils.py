import os


def dir_existence_checker(file_directory):
    if not os.path.exists(file_directory):
        os.makedirs(file_directory)
