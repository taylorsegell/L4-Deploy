class IbmWxdiError(Exception):
    """Base exception for all errors in the ibm-wxdi package."""
    pass


class InitializationError(IbmWxdiError):
    """Raised when the client fails to initialize."""
    pass


class AuthenticationError(IbmWxdiError):
    """Raised for authentication failures."""
    pass


class APIError(IbmWxdiError):
    """Raised for non-successful API responses."""
    pass


class NotFoundError(APIError):
    """Raised when an API resource is not found (404)."""
    pass
