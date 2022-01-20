import docx
from typing import List

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    support_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("cannot ingest exception")

        res = []
        document = docx.Document(path)

        for i in document.paragraphs:
            if i.text:
                body, author = i.text.split(' - ')
                res.append(QuoteModel(body, author))
        return res
