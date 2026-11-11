from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business_address import BusinessAddress
    from ..models.conditions import Conditions
    from ..models.current_registration import CurrentRegistration
    from ..models.public_disciplinary_action import PublicDisciplinaryAction
    from ..models.registration_history import RegistrationHistory


T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        name (str | Unset):
        name_tc (str | Unset):
        reg_code (str | Unset):
        current_registration (list[CurrentRegistration] | Unset):
        business_address (list[BusinessAddress] | Unset):
        conditions (list[Conditions] | Unset):
        registration_history (list[RegistrationHistory] | Unset):
        public_disciplinary_action (list[PublicDisciplinaryAction] | Unset):
    """

    name: str | Unset = UNSET
    name_tc: str | Unset = UNSET
    reg_code: str | Unset = UNSET
    current_registration: list[CurrentRegistration] | Unset = UNSET
    business_address: list[BusinessAddress] | Unset = UNSET
    conditions: list[Conditions] | Unset = UNSET
    registration_history: list[RegistrationHistory] | Unset = UNSET
    public_disciplinary_action: list[PublicDisciplinaryAction] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        name_tc = self.name_tc

        reg_code = self.reg_code

        current_registration: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.current_registration, Unset):
            current_registration = []
            for current_registration_item_data in self.current_registration:
                current_registration_item = current_registration_item_data.to_dict()
                current_registration.append(current_registration_item)

        business_address: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.business_address, Unset):
            business_address = []
            for business_address_item_data in self.business_address:
                business_address_item = business_address_item_data.to_dict()
                business_address.append(business_address_item)

        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        registration_history: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.registration_history, Unset):
            registration_history = []
            for registration_history_item_data in self.registration_history:
                registration_history_item = registration_history_item_data.to_dict()
                registration_history.append(registration_history_item)

        public_disciplinary_action: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.public_disciplinary_action, Unset):
            public_disciplinary_action = []
            for public_disciplinary_action_item_data in self.public_disciplinary_action:
                public_disciplinary_action_item = (
                    public_disciplinary_action_item_data.to_dict()
                )
                public_disciplinary_action.append(public_disciplinary_action_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if name_tc is not UNSET:
            field_dict["name_tc"] = name_tc
        if reg_code is not UNSET:
            field_dict["reg_code"] = reg_code
        if current_registration is not UNSET:
            field_dict["current_registration"] = current_registration
        if business_address is not UNSET:
            field_dict["business_address"] = business_address
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if registration_history is not UNSET:
            field_dict["registration_history"] = registration_history
        if public_disciplinary_action is not UNSET:
            field_dict["public_disciplinary_action"] = public_disciplinary_action

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.business_address import BusinessAddress
        from ..models.conditions import Conditions
        from ..models.current_registration import CurrentRegistration
        from ..models.public_disciplinary_action import PublicDisciplinaryAction
        from ..models.registration_history import RegistrationHistory

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        name_tc = d.pop("name_tc", UNSET)

        reg_code = d.pop("reg_code", UNSET)

        _current_registration = d.pop("current_registration", UNSET)
        current_registration: list[CurrentRegistration] | Unset = UNSET
        if _current_registration is not UNSET:
            current_registration = []
            for current_registration_item_data in _current_registration:
                current_registration_item = CurrentRegistration.from_dict(
                    current_registration_item_data
                )

                current_registration.append(current_registration_item)

        _business_address = d.pop("business_address", UNSET)
        business_address: list[BusinessAddress] | Unset = UNSET
        if _business_address is not UNSET:
            business_address = []
            for business_address_item_data in _business_address:
                business_address_item = BusinessAddress.from_dict(
                    business_address_item_data
                )

                business_address.append(business_address_item)

        _conditions = d.pop("conditions", UNSET)
        conditions: list[Conditions] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = Conditions.from_dict(conditions_item_data)

                conditions.append(conditions_item)

        _registration_history = d.pop("registration_history", UNSET)
        registration_history: list[RegistrationHistory] | Unset = UNSET
        if _registration_history is not UNSET:
            registration_history = []
            for registration_history_item_data in _registration_history:
                registration_history_item = RegistrationHistory.from_dict(
                    registration_history_item_data
                )

                registration_history.append(registration_history_item)

        _public_disciplinary_action = d.pop("public_disciplinary_action", UNSET)
        public_disciplinary_action: list[PublicDisciplinaryAction] | Unset = UNSET
        if _public_disciplinary_action is not UNSET:
            public_disciplinary_action = []
            for public_disciplinary_action_item_data in _public_disciplinary_action:
                public_disciplinary_action_item = PublicDisciplinaryAction.from_dict(
                    public_disciplinary_action_item_data
                )

                public_disciplinary_action.append(public_disciplinary_action_item)

        record = cls(
            name=name,
            name_tc=name_tc,
            reg_code=reg_code,
            current_registration=current_registration,
            business_address=business_address,
            conditions=conditions,
            registration_history=registration_history,
            public_disciplinary_action=public_disciplinary_action,
        )

        record.additional_properties = d
        return record

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
