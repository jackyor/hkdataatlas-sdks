"""A client library for accessing Electrical and Mechanical Services Department — Premises where the Improvement Notice (IN) In Force for the Buildings Energy Efficiency Ordinance"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
