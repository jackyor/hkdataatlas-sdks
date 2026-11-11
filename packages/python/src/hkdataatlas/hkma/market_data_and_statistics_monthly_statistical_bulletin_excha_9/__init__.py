"""A client library for accessing Central Moneymarkets Unit (CMU) service"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
