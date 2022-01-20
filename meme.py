import os
import random
import argparse

from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.IngestorManager import IngestorManager

# @TODO Import your Ingestor and MemeEngine classes


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

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
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


def make_args():
    """Create an ArgumentParser

    """
    parser = argparse.ArgumentParser(
        description="Load an image and text to generate a meme."
    )
    parser.add_argument(
        "--path",
        type=str,
        help="path for saving the meme generated.",
        default=None
    )
    parser.add_argument(
        "--body",
        type=str,
        help="The main text to be put on the image",
        default=None
    )
    parser.add_argument(
        "--author",
        type=str,
        help="The author of the main text to be put on the image",
        default=None
    )
    return parser.parse_args()


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    args = make_args()
    print(generate_meme(args.path, args.body, args.author))
