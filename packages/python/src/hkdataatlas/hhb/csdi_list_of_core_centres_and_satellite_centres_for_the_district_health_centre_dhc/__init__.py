"""A client library for accessing Health Bureau — List of Core Centres and Satellite Centres for the District Health Centre (DHC)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
