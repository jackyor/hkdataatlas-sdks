"""A client library for accessing Outstanding amount of Hong Kong dollar debt instruments, other than Exchange Fund Bills and Notes"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
