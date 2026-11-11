"""A client library for accessing HKIMR - Clearing House Figures (Yearly)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
