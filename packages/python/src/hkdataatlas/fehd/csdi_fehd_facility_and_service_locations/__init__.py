"""A client library for accessing Food and Environmental Hygiene Department — FEHD facility and service locations"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
