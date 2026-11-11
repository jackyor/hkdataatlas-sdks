"""A client library for accessing Census and Statistics Department — Land area, mid-year population and population density by District Council district"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
