"""A client library for accessing Electrical and Mechanical Services Department — Register of Hong Kong Energy Efficiency Registration Scheme for Buildings (on or after 2018)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
