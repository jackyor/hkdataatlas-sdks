"""A client library for accessing Environmental Protection Department — Air Quality Monitoring Network of Hong Kong"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
