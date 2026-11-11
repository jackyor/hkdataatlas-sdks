"""A client library for accessing Transport Department — Traffic Data collected by Traffic Detectors Installed at Smart Lampposts"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
