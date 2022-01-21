"""The Quote Template."""


class QuoteModel:
    """
    The quote model class.

    - contains a body and a author of a quote
    """

    def __init__(self, body, author):
        """Initiate the body and author of a quote."""
        self.body = body
        self.author = author

    def __str__(self):
        """Return the string of this quote."""
        return f'"{self.body}" - {self.author}'.replace("'", "")

    def __repr__(self):
        """Return the string of this quote."""
        return '{}-{}'.format(self.body, self.author)
