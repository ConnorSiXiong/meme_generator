from abc import ABC, abstractmethod
import os


class MemeEngineInterface(ABC):
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self._check_output_dir()

    def _check_output_dir(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    @abstractmethod
    def make_meme(self,img_path: str, text: str, author: str, width=500) -> str:
        pass
