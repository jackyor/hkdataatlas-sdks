"""A client library for accessing Hong Kong Police Force — Self-service Kiosks"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
