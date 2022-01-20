"""The main entrance of the Flask app."""
import random
import os
import requests
from flask import Flask, render_template, abort, request

from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine.IngestorManager import IngestorManager

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # quote_files variable
    quotes_arr = []

    for quote_file in quote_files:
        quotes_arr.extend(IngestorManager.parse(quote_file))

    images_path = "./_data/photos/dog/"
    # images within the images images_path directory
    images_arr = []
    for file in os.listdir(images_path):
        if file.endswith(".jpg"):
            images_arr.append(os.path.join(images_path, file))

    return quotes_arr, images_arr


quotes, images = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # Use the random python standard library class to:
    # 1. select a random image from image array
    # 2. select a random quote from the quotes array
    img = random.choice(images)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


class BufferImage:
    """Temporarily create a file with a rnadom name in your chosen directory."""

    def __init__(self, directory='_temp'):
        """Save down the temp file and location."""
        self.file = None
        self.dir = directory

    def create_dir(self):
        """Make a temporary file which will soon be deleted."""
        if not os.path.isdir(self.dir):
            os.mkdir(self.dir)
        file = f'./{self.dir}/{random.randint(100)}.jpg'
        self.file = file
        return file

    def remove_temp_file(self):
        """Remove the file you've made."""
        if self.file:
            os.remove(self.file)


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""

    image_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    response_image = requests.get(image_url)
    if not response_image:
        abort(404, description='Unable to download an image from the supplied URL.')

    temp_image = BufferImage()
    file_name = temp_image.create_dir()
    open(file_name, 'wb').write(response_image.content)

    # make meme
    path = meme.make_meme(file_name, body, author)

    temp_image.remove_temp_file()
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
