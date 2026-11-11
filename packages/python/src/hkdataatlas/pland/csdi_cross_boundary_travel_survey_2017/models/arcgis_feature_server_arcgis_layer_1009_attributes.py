from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1009Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1009Attributes:
    """
    Attributes:
        objectid_1 (int | Unset): Publisher field type: esriFieldTypeOID
        objectid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        cp_en (None | str | Unset): Publisher field type: esriFieldTypeString
        y2013_14_general_individual_visit_endorsement (None | str | Unset): Publisher field type: esriFieldTypeString
        y2013_14_one_year_multiple_entry_individual_visit_endorsement (None | str | Unset): Publisher field type:
            esriFieldTypeString
        y2013_14_non_individual_visit_endorsement (None | str | Unset): Publisher field type: esriFieldTypeString
        y2015_general_individual_visit_endorsement (None | str | Unset): Publisher field type: esriFieldTypeString
        y2015_one_year_multiple_entry_individual_visit_endorsement (None | str | Unset): Publisher field type:
            esriFieldTypeString
        y2015_one_trip_per_week_individual_visit_endorsement (None | str | Unset): Publisher field type:
            esriFieldTypeString
        y2015_non_individual_visit_endorsement (None | str | Unset): Publisher field type: esriFieldTypeString
        y2017_general_individual_visit_endorsement (None | str | Unset): Publisher field type: esriFieldTypeString
        y2017_one_trip_per_week_individual_visit_endorsement (None | str | Unset): Publisher field type:
            esriFieldTypeString
        y2017_non_individual_visit_endorsement (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid_1: int | Unset = UNSET
    objectid: int | None | Unset = UNSET
    cp_en: None | str | Unset = UNSET
    y2013_14_general_individual_visit_endorsement: None | str | Unset = UNSET
    y2013_14_one_year_multiple_entry_individual_visit_endorsement: (
        None | str | Unset
    ) = UNSET
    y2013_14_non_individual_visit_endorsement: None | str | Unset = UNSET
    y2015_general_individual_visit_endorsement: None | str | Unset = UNSET
    y2015_one_year_multiple_entry_individual_visit_endorsement: None | str | Unset = (
        UNSET
    )
    y2015_one_trip_per_week_individual_visit_endorsement: None | str | Unset = UNSET
    y2015_non_individual_visit_endorsement: None | str | Unset = UNSET
    y2017_general_individual_visit_endorsement: None | str | Unset = UNSET
    y2017_one_trip_per_week_individual_visit_endorsement: None | str | Unset = UNSET
    y2017_non_individual_visit_endorsement: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid_1 = self.objectid_1

        objectid: int | None | Unset
        if isinstance(self.objectid, Unset):
            objectid = UNSET
        else:
            objectid = self.objectid

        cp_en: None | str | Unset
        if isinstance(self.cp_en, Unset):
            cp_en = UNSET
        else:
            cp_en = self.cp_en

        y2013_14_general_individual_visit_endorsement: None | str | Unset
        if isinstance(self.y2013_14_general_individual_visit_endorsement, Unset):
            y2013_14_general_individual_visit_endorsement = UNSET
        else:
            y2013_14_general_individual_visit_endorsement = (
                self.y2013_14_general_individual_visit_endorsement
            )

        y2013_14_one_year_multiple_entry_individual_visit_endorsement: (
            None | str | Unset
        )
        if isinstance(
            self.y2013_14_one_year_multiple_entry_individual_visit_endorsement, Unset
        ):
            y2013_14_one_year_multiple_entry_individual_visit_endorsement = UNSET
        else:
            y2013_14_one_year_multiple_entry_individual_visit_endorsement = (
                self.y2013_14_one_year_multiple_entry_individual_visit_endorsement
            )

        y2013_14_non_individual_visit_endorsement: None | str | Unset
        if isinstance(self.y2013_14_non_individual_visit_endorsement, Unset):
            y2013_14_non_individual_visit_endorsement = UNSET
        else:
            y2013_14_non_individual_visit_endorsement = (
                self.y2013_14_non_individual_visit_endorsement
            )

        y2015_general_individual_visit_endorsement: None | str | Unset
        if isinstance(self.y2015_general_individual_visit_endorsement, Unset):
            y2015_general_individual_visit_endorsement = UNSET
        else:
            y2015_general_individual_visit_endorsement = (
                self.y2015_general_individual_visit_endorsement
            )

        y2015_one_year_multiple_entry_individual_visit_endorsement: None | str | Unset
        if isinstance(
            self.y2015_one_year_multiple_entry_individual_visit_endorsement, Unset
        ):
            y2015_one_year_multiple_entry_individual_visit_endorsement = UNSET
        else:
            y2015_one_year_multiple_entry_individual_visit_endorsement = (
                self.y2015_one_year_multiple_entry_individual_visit_endorsement
            )

        y2015_one_trip_per_week_individual_visit_endorsement: None | str | Unset
        if isinstance(self.y2015_one_trip_per_week_individual_visit_endorsement, Unset):
            y2015_one_trip_per_week_individual_visit_endorsement = UNSET
        else:
            y2015_one_trip_per_week_individual_visit_endorsement = (
                self.y2015_one_trip_per_week_individual_visit_endorsement
            )

        y2015_non_individual_visit_endorsement: None | str | Unset
        if isinstance(self.y2015_non_individual_visit_endorsement, Unset):
            y2015_non_individual_visit_endorsement = UNSET
        else:
            y2015_non_individual_visit_endorsement = (
                self.y2015_non_individual_visit_endorsement
            )

        y2017_general_individual_visit_endorsement: None | str | Unset
        if isinstance(self.y2017_general_individual_visit_endorsement, Unset):
            y2017_general_individual_visit_endorsement = UNSET
        else:
            y2017_general_individual_visit_endorsement = (
                self.y2017_general_individual_visit_endorsement
            )

        y2017_one_trip_per_week_individual_visit_endorsement: None | str | Unset
        if isinstance(self.y2017_one_trip_per_week_individual_visit_endorsement, Unset):
            y2017_one_trip_per_week_individual_visit_endorsement = UNSET
        else:
            y2017_one_trip_per_week_individual_visit_endorsement = (
                self.y2017_one_trip_per_week_individual_visit_endorsement
            )

        y2017_non_individual_visit_endorsement: None | str | Unset
        if isinstance(self.y2017_non_individual_visit_endorsement, Unset):
            y2017_non_individual_visit_endorsement = UNSET
        else:
            y2017_non_individual_visit_endorsement = (
                self.y2017_non_individual_visit_endorsement
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid_1 is not UNSET:
            field_dict["OBJECTID_1"] = objectid_1
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if cp_en is not UNSET:
            field_dict["CP_En"] = cp_en
        if y2013_14_general_individual_visit_endorsement is not UNSET:
            field_dict["Y2013_14_General_Individual_Visit_Endorsement"] = (
                y2013_14_general_individual_visit_endorsement
            )
        if y2013_14_one_year_multiple_entry_individual_visit_endorsement is not UNSET:
            field_dict[
                "Y2013_14_One_year_multiple_entry_Individual_Visit_Endorsement"
            ] = y2013_14_one_year_multiple_entry_individual_visit_endorsement
        if y2013_14_non_individual_visit_endorsement is not UNSET:
            field_dict["Y2013_14_Non_Individual_Visit_Endorsement"] = (
                y2013_14_non_individual_visit_endorsement
            )
        if y2015_general_individual_visit_endorsement is not UNSET:
            field_dict["Y2015_General_Individual_Visit_Endorsement"] = (
                y2015_general_individual_visit_endorsement
            )
        if y2015_one_year_multiple_entry_individual_visit_endorsement is not UNSET:
            field_dict["Y2015_One_year_multiple_entry_Individual_Visit_Endorsement"] = (
                y2015_one_year_multiple_entry_individual_visit_endorsement
            )
        if y2015_one_trip_per_week_individual_visit_endorsement is not UNSET:
            field_dict["Y2015_One_trip_per_week_Individual_Visit_Endorsement"] = (
                y2015_one_trip_per_week_individual_visit_endorsement
            )
        if y2015_non_individual_visit_endorsement is not UNSET:
            field_dict["Y2015_Non_Individual_Visit_Endorsement"] = (
                y2015_non_individual_visit_endorsement
            )
        if y2017_general_individual_visit_endorsement is not UNSET:
            field_dict["Y2017_General_Individual_Visit_Endorsement"] = (
                y2017_general_individual_visit_endorsement
            )
        if y2017_one_trip_per_week_individual_visit_endorsement is not UNSET:
            field_dict["Y2017_One_trip_per_week_Individual_Visit_Endorsement"] = (
                y2017_one_trip_per_week_individual_visit_endorsement
            )
        if y2017_non_individual_visit_endorsement is not UNSET:
            field_dict["Y2017_Non_Individual_Visit_Endorsement"] = (
                y2017_non_individual_visit_endorsement
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid_1 = d.pop("OBJECTID_1", UNSET)

        def _parse_objectid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        objectid = _parse_objectid(d.pop("OBJECTID", UNSET))

        def _parse_cp_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cp_en = _parse_cp_en(d.pop("CP_En", UNSET))

        def _parse_y2013_14_general_individual_visit_endorsement(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2013_14_general_individual_visit_endorsement = (
            _parse_y2013_14_general_individual_visit_endorsement(
                d.pop("Y2013_14_General_Individual_Visit_Endorsement", UNSET)
            )
        )

        def _parse_y2013_14_one_year_multiple_entry_individual_visit_endorsement(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2013_14_one_year_multiple_entry_individual_visit_endorsement = (
            _parse_y2013_14_one_year_multiple_entry_individual_visit_endorsement(
                d.pop(
                    "Y2013_14_One_year_multiple_entry_Individual_Visit_Endorsement",
                    UNSET,
                )
            )
        )

        def _parse_y2013_14_non_individual_visit_endorsement(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2013_14_non_individual_visit_endorsement = (
            _parse_y2013_14_non_individual_visit_endorsement(
                d.pop("Y2013_14_Non_Individual_Visit_Endorsement", UNSET)
            )
        )

        def _parse_y2015_general_individual_visit_endorsement(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2015_general_individual_visit_endorsement = (
            _parse_y2015_general_individual_visit_endorsement(
                d.pop("Y2015_General_Individual_Visit_Endorsement", UNSET)
            )
        )

        def _parse_y2015_one_year_multiple_entry_individual_visit_endorsement(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2015_one_year_multiple_entry_individual_visit_endorsement = (
            _parse_y2015_one_year_multiple_entry_individual_visit_endorsement(
                d.pop(
                    "Y2015_One_year_multiple_entry_Individual_Visit_Endorsement", UNSET
                )
            )
        )

        def _parse_y2015_one_trip_per_week_individual_visit_endorsement(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2015_one_trip_per_week_individual_visit_endorsement = (
            _parse_y2015_one_trip_per_week_individual_visit_endorsement(
                d.pop("Y2015_One_trip_per_week_Individual_Visit_Endorsement", UNSET)
            )
        )

        def _parse_y2015_non_individual_visit_endorsement(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2015_non_individual_visit_endorsement = (
            _parse_y2015_non_individual_visit_endorsement(
                d.pop("Y2015_Non_Individual_Visit_Endorsement", UNSET)
            )
        )

        def _parse_y2017_general_individual_visit_endorsement(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2017_general_individual_visit_endorsement = (
            _parse_y2017_general_individual_visit_endorsement(
                d.pop("Y2017_General_Individual_Visit_Endorsement", UNSET)
            )
        )

        def _parse_y2017_one_trip_per_week_individual_visit_endorsement(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2017_one_trip_per_week_individual_visit_endorsement = (
            _parse_y2017_one_trip_per_week_individual_visit_endorsement(
                d.pop("Y2017_One_trip_per_week_Individual_Visit_Endorsement", UNSET)
            )
        )

        def _parse_y2017_non_individual_visit_endorsement(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2017_non_individual_visit_endorsement = (
            _parse_y2017_non_individual_visit_endorsement(
                d.pop("Y2017_Non_Individual_Visit_Endorsement", UNSET)
            )
        )

        arcgis_feature_server_arcgis_layer_1009_attributes = cls(
            objectid_1=objectid_1,
            objectid=objectid,
            cp_en=cp_en,
            y2013_14_general_individual_visit_endorsement=y2013_14_general_individual_visit_endorsement,
            y2013_14_one_year_multiple_entry_individual_visit_endorsement=y2013_14_one_year_multiple_entry_individual_visit_endorsement,
            y2013_14_non_individual_visit_endorsement=y2013_14_non_individual_visit_endorsement,
            y2015_general_individual_visit_endorsement=y2015_general_individual_visit_endorsement,
            y2015_one_year_multiple_entry_individual_visit_endorsement=y2015_one_year_multiple_entry_individual_visit_endorsement,
            y2015_one_trip_per_week_individual_visit_endorsement=y2015_one_trip_per_week_individual_visit_endorsement,
            y2015_non_individual_visit_endorsement=y2015_non_individual_visit_endorsement,
            y2017_general_individual_visit_endorsement=y2017_general_individual_visit_endorsement,
            y2017_one_trip_per_week_individual_visit_endorsement=y2017_one_trip_per_week_individual_visit_endorsement,
            y2017_non_individual_visit_endorsement=y2017_non_individual_visit_endorsement,
        )

        arcgis_feature_server_arcgis_layer_1009_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1009_attributes

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
