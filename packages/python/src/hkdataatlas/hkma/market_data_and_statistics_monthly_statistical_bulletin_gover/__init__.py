"""A client library for accessing Secondary market turnover of Government Bonds issued under the Institutional Bond Issuance Programme - Original maturity"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
