import random
import os
import requests
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes
from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.IngestorManager import IngestorManager

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []

    for quote_file in quote_files:
        quotes.extend(IngestorManager.parse(quote_file))


    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for file in os.listdir(images_path):
        if file.endswith(".jpg"):
            imgs.append(os.path.join(images_path, file))

    return quotes, imgs


quotes, imgs = setup()

@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')

class CreateTemp:
    """Temporarily create a file with a rnadom name in your chosen directory."""

    def __init__(self, dir='tmp'):
        """Save down the temp file and location."""
        self.file = None
        self.dir = dir

    def mkfile(self, extension):
        """Make a temporary file which will soon be deleted."""
        if not os.path.isdir(self.dir):
            os.mkdir(self.dir)
        file = f'./{self.dir}/{random.randint(0,1000000)}.{extension}'
        self.file = file
        return file

    def rmfile(self):
        """Remove the file you've made."""
        if self.file:
            os.remove(self.file)

@ app.route('/create', methods = ['POST'])
def meme_post():
    """Create a user defined meme."""
    print('hahah')
    image_url=request.form.get('image_url')
    print('image_url', image_url)
    body=request.form.get('body')
    print('body',body)
    author=request.form.get('author')
    print('author',author)
    req=requests.get(image_url)
    if not req:
        abort(404, description = 'Unable to download an image from the supplied URL.')
    tmp=CreateTemp()
    file_name=tmp.mkfile('jpg')
    open(file_name, 'wb').write(req.content)
    path=meme.make_meme(file_name, body, author)
    tmp.rmfile()
    return render_template('meme.html', path = path)


if __name__ == "__main__":
    app.run()
