"""A client library for accessing Education Bureau — Information on the Number and Academic Qualifications of Academic Staff by Institution"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
