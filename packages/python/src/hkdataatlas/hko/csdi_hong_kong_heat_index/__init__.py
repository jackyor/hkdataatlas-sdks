"""A client library for accessing Hong Kong Observatory — Hong Kong Heat Index"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
