"""A client library for accessing Electrical and Mechanical Services Department — Buildings issued with Energy Audit Form for the Buildings Energy Efficiency Ordinance"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
