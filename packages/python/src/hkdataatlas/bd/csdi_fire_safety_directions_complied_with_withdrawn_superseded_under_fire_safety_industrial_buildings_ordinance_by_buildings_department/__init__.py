"""A client library for accessing Buildings Department — Fire Safety Directions complied with/withdrawn/superseded under Fire Safety (Industrial Buildings) Ordinance by Buildings Department"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
