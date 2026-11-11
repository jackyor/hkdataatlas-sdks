"""A client library for accessing Electrical and Mechanical Services Department — Register of Distributors Approved by Registered Gas Supply Companies for Liquefied Petroleum Gas Cylinder Distribution in Hong Kong"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
