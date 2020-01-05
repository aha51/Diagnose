#invalid response exception

class InvalidResponseError(Exception):

    def __init__(self, message):
        self.message = message
    