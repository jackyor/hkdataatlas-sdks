"""A client library for accessing Hong Kong Police Force — Police Stations (Districts / Divisions)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
