"""A client library for accessing Census and Statistics Department — Dataset on population and household statistics analysed by District Council district"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
