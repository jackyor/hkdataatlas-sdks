"""A client library for accessing Hong Kong Observatory — Gridded rainfall nowcast in Hong Kong"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
