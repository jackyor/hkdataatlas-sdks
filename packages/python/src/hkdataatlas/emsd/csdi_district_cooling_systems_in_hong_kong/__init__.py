"""A client library for accessing Electrical and Mechanical Services Department — District Cooling Systems in Hong Kong"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
