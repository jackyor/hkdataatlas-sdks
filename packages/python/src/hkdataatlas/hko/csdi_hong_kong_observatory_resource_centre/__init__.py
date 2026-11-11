"""A client library for accessing Hong Kong Observatory — Hong Kong Observatory
resource centre"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
