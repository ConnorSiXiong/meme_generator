"""Some helper functions.

Check the directory existence.
Walk through directory to collect all the files.
Generate a color randomly.
"""

import os
import random
import textwrap


def dir_existence_checker(file_directory):
    """Check whether a directory is exist."""
    if not os.path.exists(file_directory):
        os.makedirs(file_directory)


def dir_walk(path):
    """Walk through a file directory.
    This automatically discover ingestible files in a directory.
    """
    return [os.path.join(root, name) for root, _, files in os.walk(path) for name in files]


def generate_color():
    """Generate a color randomly."""
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def warp_long_text(text):
    """Wrap (text) Wraps the single paragraph in text (a string) so every line is at most width characters long.
    It doesn't curtails the text."""
    if len(text) > 50:
        wrapper = textwrap.TextWrapper(width=30)
        dedent_text = textwrap.dedent(text=text)
        wrapper_text = wrapper.fill(text=dedent_text)
        print(wrapper_text)
        return wrapper_text
    else:
        return text
