"""A client library for accessing Lands Department — DOP1000-1982(Grid Line Version)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
