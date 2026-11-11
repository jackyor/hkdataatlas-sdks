"""A client library for accessing Fire Services Department — Fire Safety Complaints for Operational Commands by 18 District Council districts (Provisional Figures)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
