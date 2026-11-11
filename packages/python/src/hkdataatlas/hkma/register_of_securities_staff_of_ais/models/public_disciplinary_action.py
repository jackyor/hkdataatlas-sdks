from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rec_pub_dis_act_by_hkma import RecPubDisActByHkma
    from ..models.rec_pub_dis_act_by_sfc import RecPubDisActBySfc


T = TypeVar("T", bound="PublicDisciplinaryAction")


@_attrs_define
class PublicDisciplinaryAction:
    """
    Attributes:
        rec_pub_dis_act_by_sfc (list[RecPubDisActBySfc] | Unset):
        rec_pub_dis_act_by_hkma (list[RecPubDisActByHkma] | Unset):
    """

    rec_pub_dis_act_by_sfc: list[RecPubDisActBySfc] | Unset = UNSET
    rec_pub_dis_act_by_hkma: list[RecPubDisActByHkma] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rec_pub_dis_act_by_sfc: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rec_pub_dis_act_by_sfc, Unset):
            rec_pub_dis_act_by_sfc = []
            for rec_pub_dis_act_by_sfc_item_data in self.rec_pub_dis_act_by_sfc:
                rec_pub_dis_act_by_sfc_item = rec_pub_dis_act_by_sfc_item_data.to_dict()
                rec_pub_dis_act_by_sfc.append(rec_pub_dis_act_by_sfc_item)

        rec_pub_dis_act_by_hkma: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rec_pub_dis_act_by_hkma, Unset):
            rec_pub_dis_act_by_hkma = []
            for rec_pub_dis_act_by_hkma_item_data in self.rec_pub_dis_act_by_hkma:
                rec_pub_dis_act_by_hkma_item = (
                    rec_pub_dis_act_by_hkma_item_data.to_dict()
                )
                rec_pub_dis_act_by_hkma.append(rec_pub_dis_act_by_hkma_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rec_pub_dis_act_by_sfc is not UNSET:
            field_dict["rec_pub_dis_act_by_sfc"] = rec_pub_dis_act_by_sfc
        if rec_pub_dis_act_by_hkma is not UNSET:
            field_dict["rec_pub_dis_act_by_hkma"] = rec_pub_dis_act_by_hkma

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.rec_pub_dis_act_by_hkma import RecPubDisActByHkma
        from ..models.rec_pub_dis_act_by_sfc import RecPubDisActBySfc

        d = dict(src_dict)
        _rec_pub_dis_act_by_sfc = d.pop("rec_pub_dis_act_by_sfc", UNSET)
        rec_pub_dis_act_by_sfc: list[RecPubDisActBySfc] | Unset = UNSET
        if _rec_pub_dis_act_by_sfc is not UNSET:
            rec_pub_dis_act_by_sfc = []
            for rec_pub_dis_act_by_sfc_item_data in _rec_pub_dis_act_by_sfc:
                rec_pub_dis_act_by_sfc_item = RecPubDisActBySfc.from_dict(
                    rec_pub_dis_act_by_sfc_item_data
                )

                rec_pub_dis_act_by_sfc.append(rec_pub_dis_act_by_sfc_item)

        _rec_pub_dis_act_by_hkma = d.pop("rec_pub_dis_act_by_hkma", UNSET)
        rec_pub_dis_act_by_hkma: list[RecPubDisActByHkma] | Unset = UNSET
        if _rec_pub_dis_act_by_hkma is not UNSET:
            rec_pub_dis_act_by_hkma = []
            for rec_pub_dis_act_by_hkma_item_data in _rec_pub_dis_act_by_hkma:
                rec_pub_dis_act_by_hkma_item = RecPubDisActByHkma.from_dict(
                    rec_pub_dis_act_by_hkma_item_data
                )

                rec_pub_dis_act_by_hkma.append(rec_pub_dis_act_by_hkma_item)

        public_disciplinary_action = cls(
            rec_pub_dis_act_by_sfc=rec_pub_dis_act_by_sfc,
            rec_pub_dis_act_by_hkma=rec_pub_dis_act_by_hkma,
        )

        public_disciplinary_action.additional_properties = d
        return public_disciplinary_action

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
