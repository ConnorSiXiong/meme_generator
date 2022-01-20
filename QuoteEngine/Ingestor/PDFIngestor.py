from typing import List
import subprocess
import os
import time

from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    support_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        text_file = f'./_data/{str(time.time())[:10]}.txt'

        with open(text_file, "a") as f:
            f.close()
        cmd = f"./pdftotext -layout -nopgbrk {path} {text_file}"
        subprocess.call(cmd, shell=True, stderr=subprocess.STDOUT)
        res = []

        try:
            with open(text_file, 'r') as f:

                for line in f.readlines():
                    line = line.strip('\n\r').strip()
                    if len(line) > 0:
                        body, author = line.split(' - ')
                        res.append(QuoteModel(body, author))
                f.close()
        except Exception:
            raise Exception("PDF Parsing Failed.")


        os.remove(text_file)
        return res
