"""A client library for accessing Home Affairs Department — Collection of Damaged, Defiled, Faded and Substandard National Flags/Emblems and Regional Flags/Emblems"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
