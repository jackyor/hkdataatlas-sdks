"""A client library for accessing Town Planning Board — Graphic Data of Town Planning Board Guidelines No. 13G for Application for Open Storage and Port Back-up Uses under Section 16 of the Town Planning Ordinance"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
