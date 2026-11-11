"""A client library for accessing Electrical and Mechanical Services Department — Overall Registered Gas Contractor List: List of Registered Gas Contractors employing Registered Gas Installers of different classes of Gas Installation Work"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
