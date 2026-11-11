"""A client library for accessing Home Affairs Department — Data of Amusement Game Centres and premises with annual Amusements with Prizes Licence"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
