"""A client library for accessing Food and Environmental Hygiene Department — Trade licences for places of public entertainment, commercial bathhouses, swimming pools, slaughterhouses, offensive trades, funeral parlours and undertakers"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
