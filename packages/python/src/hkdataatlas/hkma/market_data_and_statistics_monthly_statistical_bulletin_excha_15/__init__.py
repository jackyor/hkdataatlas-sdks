"""A client library for accessing Outstanding amount of CMU issues (remaining tenor) - All currencies"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
