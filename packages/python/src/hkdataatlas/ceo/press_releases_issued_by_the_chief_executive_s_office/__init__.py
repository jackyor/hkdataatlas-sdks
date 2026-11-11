"""A client library for accessing Press releases issued by the Chief Executive's Office"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
