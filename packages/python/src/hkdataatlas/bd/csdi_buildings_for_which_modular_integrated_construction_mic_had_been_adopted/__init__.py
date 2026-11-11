"""A client library for accessing Buildings Department — Buildings for which Modular Integrated Construction (MiC) had been adopted"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
