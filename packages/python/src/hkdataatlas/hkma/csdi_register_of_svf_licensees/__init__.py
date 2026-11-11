"""A client library for accessing Hong Kong Monetary Authority — Register of SVF Licensees"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
