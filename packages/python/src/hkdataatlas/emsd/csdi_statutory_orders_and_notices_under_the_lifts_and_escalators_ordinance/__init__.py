"""A client library for accessing Electrical and Mechanical Services Department — Statutory Orders and Notices under the Lifts and Escalators Ordinance"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
