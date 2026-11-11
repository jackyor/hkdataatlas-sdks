"""A client library for accessing Town Planning Board — Planning Applications under Sections 12A, 16 and 17 and planning appeals under Section 17B of the Town Planning Ordinance"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
