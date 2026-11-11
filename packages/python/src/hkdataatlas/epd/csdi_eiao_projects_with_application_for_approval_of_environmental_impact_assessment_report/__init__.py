"""A client library for accessing Environmental Protection Department — EIAO Projects with Application for Approval of Environmental Impact Assessment Report"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
