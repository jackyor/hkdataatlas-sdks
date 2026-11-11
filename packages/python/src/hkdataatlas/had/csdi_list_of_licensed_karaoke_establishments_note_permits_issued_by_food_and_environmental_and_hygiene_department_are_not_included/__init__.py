"""A client library for accessing Home Affairs Department — List of licensed karaoke establishments (Note: Permits issued by Food and Environmental and Hygiene
Department are not included)"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
