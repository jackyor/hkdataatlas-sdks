"""A client library for accessing University Grants Committee Secretariat — Staff Number (Headcount) in Academic Departments of UGC-funded Universities by Source of Salary Funding, University, Staff Grade and Mode of Employment"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
