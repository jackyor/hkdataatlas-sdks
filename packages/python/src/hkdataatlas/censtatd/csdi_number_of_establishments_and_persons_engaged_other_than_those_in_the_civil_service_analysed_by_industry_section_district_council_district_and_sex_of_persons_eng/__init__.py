"""A client library for accessing Census and Statistics Department — Number of establishments and persons engaged (other than those in the civil service) analysed by industry section, District Council district and sex of persons engaged"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
