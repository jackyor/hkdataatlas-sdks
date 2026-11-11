"""A client library for accessing Electrical and Mechanical Services Department — Buildings with Stage One Declaration submitted for the Buildings Energy Efficiency Ordinance"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
