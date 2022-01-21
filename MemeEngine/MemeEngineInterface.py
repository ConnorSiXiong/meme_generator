"""The Meme Engine Interface.

It contains the basic function the module requires.
"""
from abc import ABC, abstractmethod

from helper import dir_existence_checker


class MemeEngineInterface(ABC):
    """The Meme Engine interface entrance."""

    def __init__(self, output_dir):
        """Check the file directory and check the format legality."""
        dir_existence_checker(output_dir)
        self.output_dir = output_dir
        self.support_format = ['jpg', 'jpeg', 'png']

    def can_ingest(self, path: str):
        """Check if the file can be ingested."""
        if not path.split('.')[-1] in self.support_format:
            raise Exception("cannot ingest exception")

    @abstractmethod
    def make_meme(self, img_path: str, text: str, author: str, width=500):
        """Will be implemented by its child class."""
