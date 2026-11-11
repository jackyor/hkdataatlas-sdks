"""A client library for accessing HKIMR - Early Post-war Retail Price Index"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
