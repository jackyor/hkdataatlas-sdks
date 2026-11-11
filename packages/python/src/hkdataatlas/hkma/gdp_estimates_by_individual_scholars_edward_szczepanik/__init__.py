"""A client library for accessing HKIMR - GDP Estimates by Edward Szczepanik (Individual Scholars)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
