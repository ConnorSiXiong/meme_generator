from abc import ABC, abstractmethod
from helper import dir_existence_checker


class MemeEngineInterface(ABC):
    def __init__(self, output_dir):
        dir_existence_checker(output_dir)
        self.output_dir = output_dir
        self.support_format = ['jpg', 'jpeg', 'png']

    def can_ingest(self, path: str):
        if not path.split('.')[-1] in self.support_format:
            raise Exception("cannot ingest exception")

    @abstractmethod
    def make_meme(self,img_path: str, text: str, author: str, width=500) -> str:
        pass
