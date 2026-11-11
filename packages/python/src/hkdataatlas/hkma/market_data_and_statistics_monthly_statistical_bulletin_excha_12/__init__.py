"""A client library for accessing Turnover of CMU issues in the secondary market (remaining tenor) - Renminbi-denominated"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
