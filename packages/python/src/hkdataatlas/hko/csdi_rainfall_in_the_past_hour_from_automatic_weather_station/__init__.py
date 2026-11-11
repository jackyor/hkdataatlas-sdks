"""A client library for accessing Hong Kong Observatory — Rainfall in the past hour from Automatic Weather Station"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
