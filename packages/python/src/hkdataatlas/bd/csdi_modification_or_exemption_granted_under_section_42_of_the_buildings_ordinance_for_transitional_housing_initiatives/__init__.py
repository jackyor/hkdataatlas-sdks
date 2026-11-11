"""A client library for accessing Buildings Department — Modification or Exemption granted under Section 42 of the Buildings Ordinance for Transitional Housing Initiatives"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
