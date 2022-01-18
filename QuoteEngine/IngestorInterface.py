from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    allowed_file_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        return path.split('.')[-1] in cls.allowed_file_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path) -> List[QuoteModel]:
        pass

