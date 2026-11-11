"""A client library for accessing Hong Kong Housing Authority — Sale transactions under the Tenants Purchase Scheme"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
