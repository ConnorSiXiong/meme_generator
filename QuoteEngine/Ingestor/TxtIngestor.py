from typing import List
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel



class TxtIngestor(IngestorInterface):
    support_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            file_type = path.split(".")[-1]
            raise Exception(f"Documents of file type {file_type} cannot be ingested")

        bodies = []
        authors = []
        with open(path, "r") as f:
            lines = f.readlines()

        for line in lines:
            bodies.append(line.split(" - ")[0])
            authors.append(line.split(" - ")[1])

        return [QuoteModel(body, author) for body, author in zip(bodies, authors)]
        # if not cls.can_ingest(path):
        #     raise Exception('Cannot Ingest Exception')
        #
        # res = []
        #
        # with open(path, "r") as f:
        #     lines = f.readlines()
        #
        # for line in lines:
        #     res.append(QuoteModel(line.split(" - ")[0], line.split(" - ")[1]))
        #
        #
        # return res
