from typing import List
import subprocess
import os
import time

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        temp = f'./_data/{str(time.time())[:10]}.txt'
        subprocess.call(['pdftotext', '-layout', path, temp])

        res = []

        try:
            with open(temp, 'r') as f:
                for line in f.readlines():
                    line = line.strip('\n\r').strip()
                    if len(line) > 0:
                        body, author = line.split(' - ')
                        res.append(QuoteModel(body, author))
        except Exception:
            raise Exception("PDF Parsing Failed.")
        finally:
            f.close()

        os.remove(temp)
        return res
