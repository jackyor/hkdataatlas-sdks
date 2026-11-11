"""A client library for accessing Education Bureau — Information of Designated Centres under Financial Assistance Scheme for Designated Evening Adult Education Courses"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
