"""A client library for accessing Civil Engineering and Development Department — Ground Investigation (GI) and Laboratory Test (LT) Records"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
