"""The ingestor manager that controls all the ingestor."""
from QuoteEngine.IngestorInterface import IngestorInterface

from QuoteEngine.Ingestor.TxtIngestor import TxtIngestor
from QuoteEngine.Ingestor.CSVIngestor import CSVIngestor
from QuoteEngine.Ingestor.DocxIngestor import DocxIngestor
from QuoteEngine.Ingestor.PDFIngestor import PDFIngestor


class IngestorErrorException(TypeError):
    """Self-defined Ingestor Error."""


class IngestorManager(IngestorInterface):
    """
    The Ingestor manager contains 4 ingestors.

        - txt ingestor
        - csv ingestor
        - docx ingestor
        - pdf ingestor
    """

    support_ingestors = [TxtIngestor, CSVIngestor, DocxIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path):
        """Implement this inherited from its interface."""
        for ingestor in cls.support_ingestors:
            try:
                if ingestor.can_ingest(path):
                    return ingestor.parse(path)
            except IngestorErrorException:
                print(f'Cannot ingest {path}')
        return None
