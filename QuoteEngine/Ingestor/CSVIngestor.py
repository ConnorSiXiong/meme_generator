from typing import List
import pandas as pd

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    support_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        data = pd.read_csv(path, header=0)
        return [QuoteModel(body, author) for body, author in zip(data['body'], data['author'])]