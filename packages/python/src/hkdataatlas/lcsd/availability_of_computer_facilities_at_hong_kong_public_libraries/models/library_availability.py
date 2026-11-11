from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.session import Session


T = TypeVar("T", bound="LibraryAvailability")


@_attrs_define
class LibraryAvailability:
    """Library availability fields documented by the data dictionary. The sample illustrates a response but does not
    establish that every response has this exact structure.

        Attributes:
            address (str | Unset): The address of the library.
            district (str | Unset): The district of the library.
            email (str | Unset): The email of the library.
            is_open (bool | Unset): The current opening status of the library: true means the library is open and false
                means it is closed.
            last_update_date (str | Unset): The last updated time, in "YYYY-MM-DD hh24:mm:ss" format.
            library_code (str | Unset): The code of the library.
            library_display_name (str | Unset): The name of the library.
            session_list (list[Session] | Unset): An array of session objects. The first entry is the current session; the
                second is the next session, if one exists. If there are no more available sessions in the library, an empty
                array is returned.
            telephone (str | Unset): The contact phone number of the library. The documented format is "dddd dddd", where d
                is a numeric digit.
    """

    address: str | Unset = UNSET
    district: str | Unset = UNSET
    email: str | Unset = UNSET
    is_open: bool | Unset = UNSET
    last_update_date: str | Unset = UNSET
    library_code: str | Unset = UNSET
    library_display_name: str | Unset = UNSET
    session_list: list[Session] | Unset = UNSET
    telephone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        district = self.district

        email = self.email

        is_open = self.is_open

        last_update_date = self.last_update_date

        library_code = self.library_code

        library_display_name = self.library_display_name

        session_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.session_list, Unset):
            session_list = []
            for session_list_item_data in self.session_list:
                session_list_item = session_list_item_data.to_dict()
                session_list.append(session_list_item)

        telephone = self.telephone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if district is not UNSET:
            field_dict["district"] = district
        if email is not UNSET:
            field_dict["email"] = email
        if is_open is not UNSET:
            field_dict["isOpen"] = is_open
        if last_update_date is not UNSET:
            field_dict["lastUpdateDate"] = last_update_date
        if library_code is not UNSET:
            field_dict["libraryCode"] = library_code
        if library_display_name is not UNSET:
            field_dict["libraryDisplayName"] = library_display_name
        if session_list is not UNSET:
            field_dict["sessionList"] = session_list
        if telephone is not UNSET:
            field_dict["telephone"] = telephone

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.session import Session

        d = dict(src_dict)
        address = d.pop("address", UNSET)

        district = d.pop("district", UNSET)

        email = d.pop("email", UNSET)

        is_open = d.pop("isOpen", UNSET)

        last_update_date = d.pop("lastUpdateDate", UNSET)

        library_code = d.pop("libraryCode", UNSET)

        library_display_name = d.pop("libraryDisplayName", UNSET)

        _session_list = d.pop("sessionList", UNSET)
        session_list: list[Session] | Unset = UNSET
        if _session_list is not UNSET:
            session_list = []
            for session_list_item_data in _session_list:
                session_list_item = Session.from_dict(session_list_item_data)

                session_list.append(session_list_item)

        telephone = d.pop("telephone", UNSET)

        library_availability = cls(
            address=address,
            district=district,
            email=email,
            is_open=is_open,
            last_update_date=last_update_date,
            library_code=library_code,
            library_display_name=library_display_name,
            session_list=session_list,
            telephone=telephone,
        )

        library_availability.additional_properties = d
        return library_availability

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
