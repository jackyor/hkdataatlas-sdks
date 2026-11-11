"""A client library for accessing Environmental Protection Department — Schools participating in the "Waste Separation and Recycling Scheme in Schools" """

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
