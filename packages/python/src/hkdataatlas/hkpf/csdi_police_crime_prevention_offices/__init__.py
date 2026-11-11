"""A client library for accessing Hong Kong Police Force — Police Crime Prevention Offices"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
