import enum


class ExceptionType(enum.Enum):
    INCORRECT_HEADER_EXCEPTION = "headers Not found"
    INCORRECT_DELIMITER_EXCEPTION = "incorrect delimiter"
    INCORRECT_EXTENSION__EXCEPTION = "Sorry! CSV file does not exist"
    INCORRECT_FILE_TYPE_EXCEPTION = "Sorry file does not exist"
    


class InvalidTypeException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return f"{self.message}"