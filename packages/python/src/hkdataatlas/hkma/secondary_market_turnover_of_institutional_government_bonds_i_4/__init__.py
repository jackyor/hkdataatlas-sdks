"""A client library for accessing Secondary market turnover of institutional Government Bonds issued under the Infrastructure Bond Programme and Government Sustainable Bond Programme - Remaining tenor – Renminbi-denominated"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
