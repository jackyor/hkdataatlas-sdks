"""A client library for accessing Fire Services Department — Record of Target Mini-Storage Premises (MSP) without common fire hazards"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
