"""Some helper functions"""

import os
import random


def dir_existence_checker(file_directory):
    """Check whether a directory is exist."""
    if not os.path.exists(file_directory):
        os.makedirs(file_directory)


def dir_walk(path):
    """Walk through a file directory"""
    return [os.path.join(root, name) for root, _, files in os.walk(path) for name in files]


def generate_color():
    """Generate a color randomly"""
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
