class PayPayError(Exception):
    def __init__(self, message: str, code: int = 0):
        super().__init__(message)
        self.code = code

    def fire(self):
        raise self