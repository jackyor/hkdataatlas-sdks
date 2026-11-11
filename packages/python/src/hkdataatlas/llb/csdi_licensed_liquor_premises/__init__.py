"""A client library for accessing Liquor Licensing Board — Licensed Liquor Premises"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
