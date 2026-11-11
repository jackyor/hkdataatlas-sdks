"""A client library for accessing Food and Environmental Hygiene Department — Sale of restricted food permits"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
