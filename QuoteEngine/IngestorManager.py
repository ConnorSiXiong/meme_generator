from QuoteEngine.IngestorInterface import IngestorInterface

from QuoteEngine.Ingestor.TxtIngestor import TxtIngestor
from QuoteEngine.Ingestor.CSVIngestor import CSVIngestor
from QuoteEngine.Ingestor.DocxIngestor import DocxIngestor
from QuoteEngine.Ingestor.PDFIngestor import PDFIngestor

class IngestorErrorException(TypeError):
    pass


class IngestorManager(IngestorInterface):
    support_ingestors = [TxtIngestor, CSVIngestor, DocxIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path):
        for ingestor in cls.support_ingestors:
            print(ingestor)
            try:
                if ingestor.can_ingest(path):
                    return ingestor.parse(path)
            except IngestorErrorException:
                print(f'Cannot ingest {path}')

