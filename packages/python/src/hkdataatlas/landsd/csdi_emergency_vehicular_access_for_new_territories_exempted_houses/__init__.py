"""A client library for accessing Lands Department — Emergency Vehicular Access (for New Territories Exempted Houses)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
