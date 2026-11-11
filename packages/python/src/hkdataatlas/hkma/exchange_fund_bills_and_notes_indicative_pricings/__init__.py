"""A client library for accessing Exchange Fund Bills and Notes Indicative Pricings-IndicativePrice"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
