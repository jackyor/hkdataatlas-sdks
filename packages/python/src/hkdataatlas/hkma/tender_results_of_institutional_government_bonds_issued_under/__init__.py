"""A client library for accessing Tender results of institutional Government Bonds issued under the Infrastructure Bond Programme and Government Sustainable Bond Programme – Hong Kong dollar-denominated"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
