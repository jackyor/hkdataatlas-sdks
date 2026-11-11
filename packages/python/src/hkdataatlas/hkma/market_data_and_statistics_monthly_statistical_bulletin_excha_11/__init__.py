"""A client library for accessing Turnover of CMU issues in the secondary market (remaining tenor) - Hong Kong dollar-denominated"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
