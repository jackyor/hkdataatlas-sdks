from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTable220Attributes")


@_attrs_define
class WfsMapServerWfsTable220Attributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        area_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        area_100 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        area_100_199 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        area_200_299 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        area_300_399 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        area_400_499 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        area_500_599 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        area_600_699 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        area_700_799 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        area_800_899 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        area_900_999 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        area_1000 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        information_cannot_be_provided (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    area_en: None | str | Unset = UNSET
    area_100: int | None | Unset = UNSET
    area_100_199: int | None | Unset = UNSET
    area_200_299: int | None | Unset = UNSET
    area_300_399: int | None | Unset = UNSET
    area_400_499: int | None | Unset = UNSET
    area_500_599: int | None | Unset = UNSET
    area_600_699: int | None | Unset = UNSET
    area_700_799: int | None | Unset = UNSET
    area_800_899: int | None | Unset = UNSET
    area_900_999: int | None | Unset = UNSET
    area_1000: int | None | Unset = UNSET
    information_cannot_be_provided: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        area_en: None | str | Unset
        if isinstance(self.area_en, Unset):
            area_en = UNSET
        else:
            area_en = self.area_en

        area_100: int | None | Unset
        if isinstance(self.area_100, Unset):
            area_100 = UNSET
        else:
            area_100 = self.area_100

        area_100_199: int | None | Unset
        if isinstance(self.area_100_199, Unset):
            area_100_199 = UNSET
        else:
            area_100_199 = self.area_100_199

        area_200_299: int | None | Unset
        if isinstance(self.area_200_299, Unset):
            area_200_299 = UNSET
        else:
            area_200_299 = self.area_200_299

        area_300_399: int | None | Unset
        if isinstance(self.area_300_399, Unset):
            area_300_399 = UNSET
        else:
            area_300_399 = self.area_300_399

        area_400_499: int | None | Unset
        if isinstance(self.area_400_499, Unset):
            area_400_499 = UNSET
        else:
            area_400_499 = self.area_400_499

        area_500_599: int | None | Unset
        if isinstance(self.area_500_599, Unset):
            area_500_599 = UNSET
        else:
            area_500_599 = self.area_500_599

        area_600_699: int | None | Unset
        if isinstance(self.area_600_699, Unset):
            area_600_699 = UNSET
        else:
            area_600_699 = self.area_600_699

        area_700_799: int | None | Unset
        if isinstance(self.area_700_799, Unset):
            area_700_799 = UNSET
        else:
            area_700_799 = self.area_700_799

        area_800_899: int | None | Unset
        if isinstance(self.area_800_899, Unset):
            area_800_899 = UNSET
        else:
            area_800_899 = self.area_800_899

        area_900_999: int | None | Unset
        if isinstance(self.area_900_999, Unset):
            area_900_999 = UNSET
        else:
            area_900_999 = self.area_900_999

        area_1000: int | None | Unset
        if isinstance(self.area_1000, Unset):
            area_1000 = UNSET
        else:
            area_1000 = self.area_1000

        information_cannot_be_provided: None | str | Unset
        if isinstance(self.information_cannot_be_provided, Unset):
            information_cannot_be_provided = UNSET
        else:
            information_cannot_be_provided = self.information_cannot_be_provided

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if area_en is not UNSET:
            field_dict["Area_En"] = area_en
        if area_100 is not UNSET:
            field_dict["Area_100"] = area_100
        if area_100_199 is not UNSET:
            field_dict["Area_100_199"] = area_100_199
        if area_200_299 is not UNSET:
            field_dict["Area_200_299"] = area_200_299
        if area_300_399 is not UNSET:
            field_dict["Area_300_399"] = area_300_399
        if area_400_499 is not UNSET:
            field_dict["Area_400_499"] = area_400_499
        if area_500_599 is not UNSET:
            field_dict["Area_500_599"] = area_500_599
        if area_600_699 is not UNSET:
            field_dict["Area_600_699"] = area_600_699
        if area_700_799 is not UNSET:
            field_dict["Area_700_799"] = area_700_799
        if area_800_899 is not UNSET:
            field_dict["Area_800_899"] = area_800_899
        if area_900_999 is not UNSET:
            field_dict["Area_900_999"] = area_900_999
        if area_1000 is not UNSET:
            field_dict["Area_1000"] = area_1000
        if information_cannot_be_provided is not UNSET:
            field_dict["Information_cannot_be_provided"] = (
                information_cannot_be_provided
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_area_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_en = _parse_area_en(d.pop("Area_En", UNSET))

        def _parse_area_100(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_100 = _parse_area_100(d.pop("Area_100", UNSET))

        def _parse_area_100_199(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_100_199 = _parse_area_100_199(d.pop("Area_100_199", UNSET))

        def _parse_area_200_299(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_200_299 = _parse_area_200_299(d.pop("Area_200_299", UNSET))

        def _parse_area_300_399(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_300_399 = _parse_area_300_399(d.pop("Area_300_399", UNSET))

        def _parse_area_400_499(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_400_499 = _parse_area_400_499(d.pop("Area_400_499", UNSET))

        def _parse_area_500_599(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_500_599 = _parse_area_500_599(d.pop("Area_500_599", UNSET))

        def _parse_area_600_699(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_600_699 = _parse_area_600_699(d.pop("Area_600_699", UNSET))

        def _parse_area_700_799(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_700_799 = _parse_area_700_799(d.pop("Area_700_799", UNSET))

        def _parse_area_800_899(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_800_899 = _parse_area_800_899(d.pop("Area_800_899", UNSET))

        def _parse_area_900_999(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_900_999 = _parse_area_900_999(d.pop("Area_900_999", UNSET))

        def _parse_area_1000(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        area_1000 = _parse_area_1000(d.pop("Area_1000", UNSET))

        def _parse_information_cannot_be_provided(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        information_cannot_be_provided = _parse_information_cannot_be_provided(
            d.pop("Information_cannot_be_provided", UNSET)
        )

        wfs_map_server_wfs_table_220_attributes = cls(
            objectid=objectid,
            area_en=area_en,
            area_100=area_100,
            area_100_199=area_100_199,
            area_200_299=area_200_299,
            area_300_399=area_300_399,
            area_400_499=area_400_499,
            area_500_599=area_500_599,
            area_600_699=area_600_699,
            area_700_799=area_700_799,
            area_800_899=area_800_899,
            area_900_999=area_900_999,
            area_1000=area_1000,
            information_cannot_be_provided=information_cannot_be_provided,
        )

        wfs_map_server_wfs_table_220_attributes.additional_properties = d
        return wfs_map_server_wfs_table_220_attributes

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
