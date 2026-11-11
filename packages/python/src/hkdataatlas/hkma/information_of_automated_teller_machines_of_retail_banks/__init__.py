"""A client library for accessing Information of Automated Teller Machines of retail banks"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
