"""A client library for accessing Hong Kong Housing Society Housing Archive and Commercial Leasing Data"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
