"""A client library for accessing Office of the Communications Authority — Location of Registered WiFi Access Points"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
