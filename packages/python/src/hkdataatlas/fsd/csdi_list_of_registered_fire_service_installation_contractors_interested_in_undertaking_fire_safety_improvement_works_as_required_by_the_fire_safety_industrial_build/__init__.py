"""A client library for accessing Fire Services Department — List of Registered Fire Service Installation Contractors Interested in Undertaking Fire Safety Improvement Works as Required by the Fire Safety (Industrial Buildings) Ordinance (Cap. 636)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
