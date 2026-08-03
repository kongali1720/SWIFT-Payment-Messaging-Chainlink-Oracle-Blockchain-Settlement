class SwiftParserError(Exception):
    """Raised when a SWIFT message cannot be parsed."""
    pass


class SwiftValidationError(Exception):
    """Raised when a SWIFT message is invalid."""
    pass
