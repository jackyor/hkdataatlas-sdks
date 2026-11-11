"""A client library for accessing Hong Kong Observatory — Regional weather in Hong Kong – the latest 1-minute mean grass temperature from 5:00 p.m. to 8:00 a.m. the following date Hong Kong time"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
