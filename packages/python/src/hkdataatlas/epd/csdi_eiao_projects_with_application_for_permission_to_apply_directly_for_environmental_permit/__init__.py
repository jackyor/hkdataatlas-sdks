"""A client library for accessing Environmental Protection Department — EIAO Projects with Application for Permission to Apply Directly for Environmental Permit"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
