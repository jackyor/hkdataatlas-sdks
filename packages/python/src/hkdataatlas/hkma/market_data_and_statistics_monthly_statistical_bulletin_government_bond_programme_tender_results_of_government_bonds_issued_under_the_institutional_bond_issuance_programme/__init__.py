"""A client library for accessing Tender results of Government Bonds issued under the Institutional Bond Issuance Programme"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
