"""A client library for accessing Electrical and Mechanical Services Department — Register of Buildings issued with Certificate of Compliance Registration (COCR) under the Buildings Energy Efficiency Ordinance (BEEO)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
