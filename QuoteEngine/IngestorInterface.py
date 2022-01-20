"""The Ingestor Interface
"""
from abc import ABC, abstractmethod
from typing import List

from QuoteEngine.QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """The Ingestor Interface that contains two class functions

        can_ingest()
        parse()

    """
    support_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check the format of the file"""
        return path.split('.')[-1] in cls.support_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """The abstract method, which need to be implemented in children"""
