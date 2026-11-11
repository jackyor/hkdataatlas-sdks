"""A client library for accessing Contact details of banks' hotline for review arrangements for credit decisions"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
