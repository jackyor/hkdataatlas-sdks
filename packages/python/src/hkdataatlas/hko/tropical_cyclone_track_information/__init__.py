"""A client library for accessing Hong Kong Observatory Tropical Cyclone Track Information"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
