"""A client library for accessing Hong Kong dollar interest rates - Period Average Figures"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
