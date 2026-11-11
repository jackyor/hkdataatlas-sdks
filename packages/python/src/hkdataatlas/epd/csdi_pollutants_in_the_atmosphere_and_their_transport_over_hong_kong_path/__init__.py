"""A client library for accessing Environmental Protection Department — Pollutants in the Atmosphere and their Transport over Hong Kong (PATH)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
