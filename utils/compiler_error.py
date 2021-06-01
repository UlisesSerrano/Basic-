class CompilerError(Exception):
    """Exception raised for errors in the parser.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message="Parser Error"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message