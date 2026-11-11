"""A client library for accessing Outstanding amount of CMU issues (remaining tenor) - Renminbi-denominated"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
