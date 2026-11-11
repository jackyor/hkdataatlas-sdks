from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        permitted_accommodation (float | None | Unset): Publisher field type: esriFieldTypeDouble
        permitted_accommodation_nil (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        permitted_accommodation_kgwd (float | None | Unset): Publisher field type: esriFieldTypeDouble
        permitted_accommodation_kgwd_nil (None | str | Unset): Publisher field type: esriFieldTypeString
        premises_code (float | None | Unset): Publisher field type: esriFieldTypeDouble
        premises_desc_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        premises_desc_chi_nil (None | str | Unset): Publisher field type: esriFieldTypeString
        premises_desc_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_chi_nil (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_eng_nil (None | str | Unset): Publisher field type: esriFieldTypeString
        room_no (None | str | Unset): Publisher field type: esriFieldTypeString
        room_no_nil (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        room_type (None | str | Unset): Publisher field type: esriFieldTypeString
        school_name_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        school_name_chi_nil (None | str | Unset): Publisher field type: esriFieldTypeString
        school_name_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        school_number (float | None | Unset): Publisher field type: esriFieldTypeDouble
        sub_premises_code (float | None | Unset): Publisher field type: esriFieldTypeDouble
        sub_premises_desc_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        sub_premises_desc_chi_nil (None | str | Unset): Publisher field type: esriFieldTypeString
        sub_premises_desc_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    permitted_accommodation: float | None | Unset = UNSET
    permitted_accommodation_nil: int | None | Unset = UNSET
    permitted_accommodation_kgwd: float | None | Unset = UNSET
    permitted_accommodation_kgwd_nil: None | str | Unset = UNSET
    premises_code: float | None | Unset = UNSET
    premises_desc_chi: None | str | Unset = UNSET
    premises_desc_chi_nil: None | str | Unset = UNSET
    premises_desc_eng: None | str | Unset = UNSET
    remarks_chi: None | str | Unset = UNSET
    remarks_chi_nil: None | str | Unset = UNSET
    remarks_eng: None | str | Unset = UNSET
    remarks_eng_nil: None | str | Unset = UNSET
    room_no: None | str | Unset = UNSET
    room_no_nil: int | None | Unset = UNSET
    room_type: None | str | Unset = UNSET
    school_name_chi: None | str | Unset = UNSET
    school_name_chi_nil: None | str | Unset = UNSET
    school_name_eng: None | str | Unset = UNSET
    school_number: float | None | Unset = UNSET
    sub_premises_code: float | None | Unset = UNSET
    sub_premises_desc_chi: None | str | Unset = UNSET
    sub_premises_desc_chi_nil: None | str | Unset = UNSET
    sub_premises_desc_eng: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    northing: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permitted_accommodation: float | None | Unset
        if isinstance(self.permitted_accommodation, Unset):
            permitted_accommodation = UNSET
        else:
            permitted_accommodation = self.permitted_accommodation

        permitted_accommodation_nil: int | None | Unset
        if isinstance(self.permitted_accommodation_nil, Unset):
            permitted_accommodation_nil = UNSET
        else:
            permitted_accommodation_nil = self.permitted_accommodation_nil

        permitted_accommodation_kgwd: float | None | Unset
        if isinstance(self.permitted_accommodation_kgwd, Unset):
            permitted_accommodation_kgwd = UNSET
        else:
            permitted_accommodation_kgwd = self.permitted_accommodation_kgwd

        permitted_accommodation_kgwd_nil: None | str | Unset
        if isinstance(self.permitted_accommodation_kgwd_nil, Unset):
            permitted_accommodation_kgwd_nil = UNSET
        else:
            permitted_accommodation_kgwd_nil = self.permitted_accommodation_kgwd_nil

        premises_code: float | None | Unset
        if isinstance(self.premises_code, Unset):
            premises_code = UNSET
        else:
            premises_code = self.premises_code

        premises_desc_chi: None | str | Unset
        if isinstance(self.premises_desc_chi, Unset):
            premises_desc_chi = UNSET
        else:
            premises_desc_chi = self.premises_desc_chi

        premises_desc_chi_nil: None | str | Unset
        if isinstance(self.premises_desc_chi_nil, Unset):
            premises_desc_chi_nil = UNSET
        else:
            premises_desc_chi_nil = self.premises_desc_chi_nil

        premises_desc_eng: None | str | Unset
        if isinstance(self.premises_desc_eng, Unset):
            premises_desc_eng = UNSET
        else:
            premises_desc_eng = self.premises_desc_eng

        remarks_chi: None | str | Unset
        if isinstance(self.remarks_chi, Unset):
            remarks_chi = UNSET
        else:
            remarks_chi = self.remarks_chi

        remarks_chi_nil: None | str | Unset
        if isinstance(self.remarks_chi_nil, Unset):
            remarks_chi_nil = UNSET
        else:
            remarks_chi_nil = self.remarks_chi_nil

        remarks_eng: None | str | Unset
        if isinstance(self.remarks_eng, Unset):
            remarks_eng = UNSET
        else:
            remarks_eng = self.remarks_eng

        remarks_eng_nil: None | str | Unset
        if isinstance(self.remarks_eng_nil, Unset):
            remarks_eng_nil = UNSET
        else:
            remarks_eng_nil = self.remarks_eng_nil

        room_no: None | str | Unset
        if isinstance(self.room_no, Unset):
            room_no = UNSET
        else:
            room_no = self.room_no

        room_no_nil: int | None | Unset
        if isinstance(self.room_no_nil, Unset):
            room_no_nil = UNSET
        else:
            room_no_nil = self.room_no_nil

        room_type: None | str | Unset
        if isinstance(self.room_type, Unset):
            room_type = UNSET
        else:
            room_type = self.room_type

        school_name_chi: None | str | Unset
        if isinstance(self.school_name_chi, Unset):
            school_name_chi = UNSET
        else:
            school_name_chi = self.school_name_chi

        school_name_chi_nil: None | str | Unset
        if isinstance(self.school_name_chi_nil, Unset):
            school_name_chi_nil = UNSET
        else:
            school_name_chi_nil = self.school_name_chi_nil

        school_name_eng: None | str | Unset
        if isinstance(self.school_name_eng, Unset):
            school_name_eng = UNSET
        else:
            school_name_eng = self.school_name_eng

        school_number: float | None | Unset
        if isinstance(self.school_number, Unset):
            school_number = UNSET
        else:
            school_number = self.school_number

        sub_premises_code: float | None | Unset
        if isinstance(self.sub_premises_code, Unset):
            sub_premises_code = UNSET
        else:
            sub_premises_code = self.sub_premises_code

        sub_premises_desc_chi: None | str | Unset
        if isinstance(self.sub_premises_desc_chi, Unset):
            sub_premises_desc_chi = UNSET
        else:
            sub_premises_desc_chi = self.sub_premises_desc_chi

        sub_premises_desc_chi_nil: None | str | Unset
        if isinstance(self.sub_premises_desc_chi_nil, Unset):
            sub_premises_desc_chi_nil = UNSET
        else:
            sub_premises_desc_chi_nil = self.sub_premises_desc_chi_nil

        sub_premises_desc_eng: None | str | Unset
        if isinstance(self.sub_premises_desc_eng, Unset):
            sub_premises_desc_eng = UNSET
        else:
            sub_premises_desc_eng = self.sub_premises_desc_eng

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permitted_accommodation is not UNSET:
            field_dict["PermittedAccommodation"] = permitted_accommodation
        if permitted_accommodation_nil is not UNSET:
            field_dict["PermittedAccommodation_nil"] = permitted_accommodation_nil
        if permitted_accommodation_kgwd is not UNSET:
            field_dict["PermittedAccommodationKGWD"] = permitted_accommodation_kgwd
        if permitted_accommodation_kgwd_nil is not UNSET:
            field_dict["PermittedAccommodationKGWD_nil"] = (
                permitted_accommodation_kgwd_nil
            )
        if premises_code is not UNSET:
            field_dict["PremisesCode"] = premises_code
        if premises_desc_chi is not UNSET:
            field_dict["PremisesDescChi"] = premises_desc_chi
        if premises_desc_chi_nil is not UNSET:
            field_dict["PremisesDescChi_nil"] = premises_desc_chi_nil
        if premises_desc_eng is not UNSET:
            field_dict["PremisesDescEng"] = premises_desc_eng
        if remarks_chi is not UNSET:
            field_dict["RemarksChi"] = remarks_chi
        if remarks_chi_nil is not UNSET:
            field_dict["RemarksChi_nil"] = remarks_chi_nil
        if remarks_eng is not UNSET:
            field_dict["RemarksEng"] = remarks_eng
        if remarks_eng_nil is not UNSET:
            field_dict["RemarksEng_nil"] = remarks_eng_nil
        if room_no is not UNSET:
            field_dict["RoomNo"] = room_no
        if room_no_nil is not UNSET:
            field_dict["RoomNo_nil"] = room_no_nil
        if room_type is not UNSET:
            field_dict["RoomType"] = room_type
        if school_name_chi is not UNSET:
            field_dict["SchoolNameChi"] = school_name_chi
        if school_name_chi_nil is not UNSET:
            field_dict["SchoolNameChi_nil"] = school_name_chi_nil
        if school_name_eng is not UNSET:
            field_dict["SchoolNameEng"] = school_name_eng
        if school_number is not UNSET:
            field_dict["SchoolNumber"] = school_number
        if sub_premises_code is not UNSET:
            field_dict["SubPremisesCode"] = sub_premises_code
        if sub_premises_desc_chi is not UNSET:
            field_dict["SubPremisesDescChi"] = sub_premises_desc_chi
        if sub_premises_desc_chi_nil is not UNSET:
            field_dict["SubPremisesDescChi_nil"] = sub_premises_desc_chi_nil
        if sub_premises_desc_eng is not UNSET:
            field_dict["SubPremisesDescEng"] = sub_premises_desc_eng
        if easting is not UNSET:
            field_dict["easting"] = easting
        if northing is not UNSET:
            field_dict["northing"] = northing
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_permitted_accommodation(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        permitted_accommodation = _parse_permitted_accommodation(
            d.pop("PermittedAccommodation", UNSET)
        )

        def _parse_permitted_accommodation_nil(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        permitted_accommodation_nil = _parse_permitted_accommodation_nil(
            d.pop("PermittedAccommodation_nil", UNSET)
        )

        def _parse_permitted_accommodation_kgwd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        permitted_accommodation_kgwd = _parse_permitted_accommodation_kgwd(
            d.pop("PermittedAccommodationKGWD", UNSET)
        )

        def _parse_permitted_accommodation_kgwd_nil(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permitted_accommodation_kgwd_nil = _parse_permitted_accommodation_kgwd_nil(
            d.pop("PermittedAccommodationKGWD_nil", UNSET)
        )

        def _parse_premises_code(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        premises_code = _parse_premises_code(d.pop("PremisesCode", UNSET))

        def _parse_premises_desc_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premises_desc_chi = _parse_premises_desc_chi(d.pop("PremisesDescChi", UNSET))

        def _parse_premises_desc_chi_nil(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premises_desc_chi_nil = _parse_premises_desc_chi_nil(
            d.pop("PremisesDescChi_nil", UNSET)
        )

        def _parse_premises_desc_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premises_desc_eng = _parse_premises_desc_eng(d.pop("PremisesDescEng", UNSET))

        def _parse_remarks_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_chi = _parse_remarks_chi(d.pop("RemarksChi", UNSET))

        def _parse_remarks_chi_nil(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_chi_nil = _parse_remarks_chi_nil(d.pop("RemarksChi_nil", UNSET))

        def _parse_remarks_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_eng = _parse_remarks_eng(d.pop("RemarksEng", UNSET))

        def _parse_remarks_eng_nil(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_eng_nil = _parse_remarks_eng_nil(d.pop("RemarksEng_nil", UNSET))

        def _parse_room_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_no = _parse_room_no(d.pop("RoomNo", UNSET))

        def _parse_room_no_nil(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        room_no_nil = _parse_room_no_nil(d.pop("RoomNo_nil", UNSET))

        def _parse_room_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        room_type = _parse_room_type(d.pop("RoomType", UNSET))

        def _parse_school_name_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_name_chi = _parse_school_name_chi(d.pop("SchoolNameChi", UNSET))

        def _parse_school_name_chi_nil(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_name_chi_nil = _parse_school_name_chi_nil(
            d.pop("SchoolNameChi_nil", UNSET)
        )

        def _parse_school_name_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_name_eng = _parse_school_name_eng(d.pop("SchoolNameEng", UNSET))

        def _parse_school_number(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        school_number = _parse_school_number(d.pop("SchoolNumber", UNSET))

        def _parse_sub_premises_code(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sub_premises_code = _parse_sub_premises_code(d.pop("SubPremisesCode", UNSET))

        def _parse_sub_premises_desc_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_premises_desc_chi = _parse_sub_premises_desc_chi(
            d.pop("SubPremisesDescChi", UNSET)
        )

        def _parse_sub_premises_desc_chi_nil(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_premises_desc_chi_nil = _parse_sub_premises_desc_chi_nil(
            d.pop("SubPremisesDescChi_nil", UNSET)
        )

        def _parse_sub_premises_desc_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_premises_desc_eng = _parse_sub_premises_desc_eng(
            d.pop("SubPremisesDescEng", UNSET)
        )

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("easting", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("northing", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            permitted_accommodation=permitted_accommodation,
            permitted_accommodation_nil=permitted_accommodation_nil,
            permitted_accommodation_kgwd=permitted_accommodation_kgwd,
            permitted_accommodation_kgwd_nil=permitted_accommodation_kgwd_nil,
            premises_code=premises_code,
            premises_desc_chi=premises_desc_chi,
            premises_desc_chi_nil=premises_desc_chi_nil,
            premises_desc_eng=premises_desc_eng,
            remarks_chi=remarks_chi,
            remarks_chi_nil=remarks_chi_nil,
            remarks_eng=remarks_eng,
            remarks_eng_nil=remarks_eng_nil,
            room_no=room_no,
            room_no_nil=room_no_nil,
            room_type=room_type,
            school_name_chi=school_name_chi,
            school_name_chi_nil=school_name_chi_nil,
            school_name_eng=school_name_eng,
            school_number=school_number,
            sub_premises_code=sub_premises_code,
            sub_premises_desc_chi=sub_premises_desc_chi,
            sub_premises_desc_chi_nil=sub_premises_desc_chi_nil,
            sub_premises_desc_eng=sub_premises_desc_eng,
            easting=easting,
            northing=northing,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
