"""The quotes and images are loaded here.

User can also write quote and load images.
"""
import argparse
import os
import random

from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine.IngestorManager import IngestorManager
from QuoteEngine.QuoteModel import QuoteModel


class InputLengthException(TypeError):
    """Customize exception handles with user CLI inputs."""


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, _, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(IngestorManager.parse(f))

        quote = random.choice(quotes)
    else:
        try:
            if author is None:
                raise InputLengthException('Author is missing')
            if len(author) > 20:
                raise Exception('The length of author is too long.')
            if len(body) > 100:
                raise Exception('The length of the text is too long.')
        except InputLengthException as e:
            print(e.args)

        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


def make_args():
    """Create an ArgumentParser.

    path - path to an image file
    body - quote body to add to the image
    author - quote author to add to the image
    """
    parser = argparse.ArgumentParser(
        description="Load an image and text to generate a meme."
    )
    parser.add_argument(
        "--path",
        type=str,
        help="The path for saving the meme generated.",
        default=None
    )
    parser.add_argument(
        "--body",
        type=str,
        help="The text of the quote",
        default=None
    )
    parser.add_argument(
        "--author",
        type=str,
        help="The author of the quote.",
        default=None
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = make_args()
    print(generate_meme(args.path, args.body, args.author))
