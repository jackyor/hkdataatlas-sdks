"""A client library for accessing Hong Kong Housing Authority — Open Space (OS) in Existing Public Housing Estates / Courts"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
