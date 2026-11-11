"""A client library for accessing Town Planning Board — Graphic Data of Town Planning Board Planning Guidelines No. 12C for Application for Developments within Deep Bay Area under Section 16 of the Town Planning Ordinance"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
