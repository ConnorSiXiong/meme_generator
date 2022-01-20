class QuoteModel(object):
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __str__(self):
        return f'"{self.body}" - {self.author}'.replace("'", "")

    def __repr__(self):
        """Return the string of this quote."""
        return '{}-{}'.format(self.body, self.author)


if __name__ == "__main__":
    a = QuoteModel('a', 'b')