"""A client library for accessing Department of Health — Baby-Friendly Maternal and Child Health Centre"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
