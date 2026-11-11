"""A client library for accessing Outstanding amount of Government Bonds under the Infrastructure Bond Programme and Government Sustainable Bond Programme - Original maturity – Hong Kong dollar-denominated"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
