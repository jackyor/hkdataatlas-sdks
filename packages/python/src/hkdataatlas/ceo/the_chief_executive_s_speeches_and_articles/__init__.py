"""A client library for accessing The Chief Executive's speeches and articles"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
