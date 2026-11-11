"""A client library for accessing Fire Services Department — Classification of Ambulance Calls for 18 District Council districts (Provisional Figures)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
