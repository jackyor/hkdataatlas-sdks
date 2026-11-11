"""A client library for accessing Food and Environmental Hygiene Department — Registered Masons Permitted to Provide Services on Burial and Exhumation of Skeletal Remains, and Installation of Headstones and Grave Coverings Surfaces in Public Cemeteries"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
