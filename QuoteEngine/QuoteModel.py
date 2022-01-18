class QuoteModel:
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        """Return the string of this quote."""
        return '{}-{}'.format(self.body, self.author)