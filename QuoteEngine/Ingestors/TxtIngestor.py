from typing import List
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel
import pandas as pd


class TxtIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')
        res = []
        df = pd.read_csv(path, sep=' - ', header=None)
        for index, row in df.iterrows():
            body, author = row[0], row[1]
            res.append(QuoteModel(body, author))
        return res
