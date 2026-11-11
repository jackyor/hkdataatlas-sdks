"""A client library for accessing Prices and yields of Government Bonds issued under the Institutional Bond Issuance Programme - Period average figures"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
