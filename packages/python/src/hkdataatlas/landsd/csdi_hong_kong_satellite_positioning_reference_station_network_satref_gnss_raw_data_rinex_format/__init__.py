"""A client library for accessing Lands Department — Hong Kong Satellite Positioning Reference Station Network (SatRef) GNSS Raw Data (RINEX Format)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
