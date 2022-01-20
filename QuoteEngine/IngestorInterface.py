from abc import ABC, abstractmethod
from typing import List

from QuoteEngine.QuoteModel import QuoteModel


class IngestorInterface(ABC):
    support_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return path.split('.')[-1] in cls.support_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass

