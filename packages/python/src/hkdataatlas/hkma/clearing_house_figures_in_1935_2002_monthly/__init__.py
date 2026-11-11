"""A client library for accessing HKIMR - Clearing House Figures (Monthly)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
