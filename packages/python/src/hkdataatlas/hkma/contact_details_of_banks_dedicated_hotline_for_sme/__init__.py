"""A client library for accessing Contact details of banks' dedicated hotline for SME"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
