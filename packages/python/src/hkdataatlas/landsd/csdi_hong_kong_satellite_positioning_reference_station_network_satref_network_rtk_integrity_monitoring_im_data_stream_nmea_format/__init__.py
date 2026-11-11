"""A client library for accessing Lands Department — Hong Kong Satellite Positioning Reference Station Network (SatRef) Network RTK Integrity Monitoring (IM) Data Stream (NMEA Format)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
