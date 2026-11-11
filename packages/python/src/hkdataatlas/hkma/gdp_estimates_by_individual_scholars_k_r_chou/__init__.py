"""A client library for accessing HKIMR - GDP Estimates by K.R. Chou (Individual Scholars)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
