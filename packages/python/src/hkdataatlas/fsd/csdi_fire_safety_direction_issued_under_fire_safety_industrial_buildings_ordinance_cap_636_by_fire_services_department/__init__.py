"""A client library for accessing Fire Services Department — Fire Safety Direction issued under Fire Safety (Industrial Buildings) Ordinance (Cap. 636) by Fire Services Department"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
