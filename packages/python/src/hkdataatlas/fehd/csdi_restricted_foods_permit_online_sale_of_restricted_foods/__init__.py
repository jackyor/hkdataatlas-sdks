"""A client library for accessing Food and Environmental Hygiene Department — Restricted Foods Permit (Online Sale of Restricted Foods)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
