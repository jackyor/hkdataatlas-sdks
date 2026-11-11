"""A client library for accessing Labour Department — Information of Occupational Safety and Health (OSH) Centre"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
