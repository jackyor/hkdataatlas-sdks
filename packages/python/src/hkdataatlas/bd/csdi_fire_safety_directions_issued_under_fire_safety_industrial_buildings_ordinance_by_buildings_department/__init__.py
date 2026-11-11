"""A client library for accessing Buildings Department — Fire Safety Directions issued under Fire Safety (Industrial Buildings) Ordinance by Buildings Department"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
