class WordleError(Exception):
    pass


class LenError(WordleError):
    """

    Raised when the lenght of the word is different from 5

    """
    pass


class InvalidWordError(WordleError):

    """

    Raised when the input word is not a string,or it can be interpreted as one

    """
    pass


class NotFoundWordError(WordleError):

    """

    Raised when the input word is not in the word list

    """
    pass
