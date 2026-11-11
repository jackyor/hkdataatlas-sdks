"""A client library for accessing Hong Kong Observatory — Predicted tidal information (Hourly heights of astronomical tides)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
