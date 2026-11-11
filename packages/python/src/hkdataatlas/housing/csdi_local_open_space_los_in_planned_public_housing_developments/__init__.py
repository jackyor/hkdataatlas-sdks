"""A client library for accessing Hong Kong Housing Authority — Local Open Space (LOS) in Planned Public Housing Developments"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
