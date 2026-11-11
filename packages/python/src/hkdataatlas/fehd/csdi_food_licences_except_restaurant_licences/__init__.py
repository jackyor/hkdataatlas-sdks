"""A client library for accessing Food and Environmental Hygiene Department — Food licences (except restaurant licences)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
