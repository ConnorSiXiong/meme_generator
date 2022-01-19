from abc import ABC, abstractmethod
from utils import dir_existence_checker


class MemeEngineInterface(ABC):
    def __init__(self, output_dir):
        dir_existence_checker(output_dir)
        self.output_dir = output_dir

    @abstractmethod
    def make_meme(self,img_path: str, text: str, author: str, width=500) -> str:
        pass
