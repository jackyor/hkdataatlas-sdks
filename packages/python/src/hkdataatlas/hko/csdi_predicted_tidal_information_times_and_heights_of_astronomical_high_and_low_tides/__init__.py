"""A client library for accessing Hong Kong Observatory — Predicted tidal information (Times and heights of astronomical high and low tides)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
