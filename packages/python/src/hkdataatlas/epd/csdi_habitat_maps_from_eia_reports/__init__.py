"""A client library for accessing Environmental Protection Department — Habitat Maps from EIA Reports"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
