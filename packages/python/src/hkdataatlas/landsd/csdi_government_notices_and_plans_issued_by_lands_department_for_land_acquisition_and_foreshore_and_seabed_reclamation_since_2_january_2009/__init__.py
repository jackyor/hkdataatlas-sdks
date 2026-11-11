"""A client library for accessing Lands Department — Government Notices and Plans Issued by Lands Department for Land Acquisition and Foreshore and Seabed Reclamation (Since 2 January 2009)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
