from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1010Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1010Attributes:
    """
    Attributes:
        objectid_1 (int | Unset): Publisher field type: esriFieldTypeOID
        objectid (float | None | Unset): Publisher field type: esriFieldTypeDouble
        cp_en (None | str | Unset): Publisher field type: esriFieldTypeString
        y2013_14_survey_proximity_to_trip_ends (None | str | Unset): Publisher field type: esriFieldTypeString
        y2013_14_survey_proximity_to_the_hubs_for_connecting_transport (None | str | Unset): Publisher field type:
            esriFieldTypeString
        y2013_14_survey_shortest_path_to_trip_ends (None | str | Unset): Publisher field type: esriFieldTypeString
        y2013_14_survey_shortest_travelling_time (None | str | Unset): Publisher field type: esriFieldTypeString
        y2013_14_survey_arranged_by_group_tours (None | str | Unset): Publisher field type: esriFieldTypeString
        y2013_14_survey_others (None | str | Unset): Publisher field type: esriFieldTypeString
        y2015_survey_proximity_to_trip_ends (None | str | Unset): Publisher field type: esriFieldTypeString
        y2015_survey_proximity_to_the_hubs_for_connecting_transport (None | str | Unset): Publisher field type:
            esriFieldTypeString
        y2015_survey_shortest_travelling_time (None | str | Unset): Publisher field type: esriFieldTypeString
        y2015_survey_shortest_path_to_trip_ends (None | str | Unset): Publisher field type: esriFieldTypeString
        y2015_survey_arranged_by_group_tours (None | str | Unset): Publisher field type: esriFieldTypeString
        y2015_survey_others (None | str | Unset): Publisher field type: esriFieldTypeString
        y2017_survey_proximity_to_trip_ends (None | str | Unset): Publisher field type: esriFieldTypeString
        y2017_survey_proximity_to_the_hubs_for_connecting_transport (None | str | Unset): Publisher field type:
            esriFieldTypeString
        y2017_survey_convenient_customs_immigration_and_quarantine_ciq (None | str | Unset): Publisher field type:
            esriFieldTypeString
        y2017_survey_shortest_path_to_trip_ends (None | str | Unset): Publisher field type: esriFieldTypeString
        y2017_survey_arranged_by_group_tours (None | str | Unset): Publisher field type: esriFieldTypeString
        y2017_survey_others (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid_1: int | Unset = UNSET
    objectid: float | None | Unset = UNSET
    cp_en: None | str | Unset = UNSET
    y2013_14_survey_proximity_to_trip_ends: None | str | Unset = UNSET
    y2013_14_survey_proximity_to_the_hubs_for_connecting_transport: (
        None | str | Unset
    ) = UNSET
    y2013_14_survey_shortest_path_to_trip_ends: None | str | Unset = UNSET
    y2013_14_survey_shortest_travelling_time: None | str | Unset = UNSET
    y2013_14_survey_arranged_by_group_tours: None | str | Unset = UNSET
    y2013_14_survey_others: None | str | Unset = UNSET
    y2015_survey_proximity_to_trip_ends: None | str | Unset = UNSET
    y2015_survey_proximity_to_the_hubs_for_connecting_transport: None | str | Unset = (
        UNSET
    )
    y2015_survey_shortest_travelling_time: None | str | Unset = UNSET
    y2015_survey_shortest_path_to_trip_ends: None | str | Unset = UNSET
    y2015_survey_arranged_by_group_tours: None | str | Unset = UNSET
    y2015_survey_others: None | str | Unset = UNSET
    y2017_survey_proximity_to_trip_ends: None | str | Unset = UNSET
    y2017_survey_proximity_to_the_hubs_for_connecting_transport: None | str | Unset = (
        UNSET
    )
    y2017_survey_convenient_customs_immigration_and_quarantine_ciq: (
        None | str | Unset
    ) = UNSET
    y2017_survey_shortest_path_to_trip_ends: None | str | Unset = UNSET
    y2017_survey_arranged_by_group_tours: None | str | Unset = UNSET
    y2017_survey_others: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid_1 = self.objectid_1

        objectid: float | None | Unset
        if isinstance(self.objectid, Unset):
            objectid = UNSET
        else:
            objectid = self.objectid

        cp_en: None | str | Unset
        if isinstance(self.cp_en, Unset):
            cp_en = UNSET
        else:
            cp_en = self.cp_en

        y2013_14_survey_proximity_to_trip_ends: None | str | Unset
        if isinstance(self.y2013_14_survey_proximity_to_trip_ends, Unset):
            y2013_14_survey_proximity_to_trip_ends = UNSET
        else:
            y2013_14_survey_proximity_to_trip_ends = (
                self.y2013_14_survey_proximity_to_trip_ends
            )

        y2013_14_survey_proximity_to_the_hubs_for_connecting_transport: (
            None | str | Unset
        )
        if isinstance(
            self.y2013_14_survey_proximity_to_the_hubs_for_connecting_transport, Unset
        ):
            y2013_14_survey_proximity_to_the_hubs_for_connecting_transport = UNSET
        else:
            y2013_14_survey_proximity_to_the_hubs_for_connecting_transport = (
                self.y2013_14_survey_proximity_to_the_hubs_for_connecting_transport
            )

        y2013_14_survey_shortest_path_to_trip_ends: None | str | Unset
        if isinstance(self.y2013_14_survey_shortest_path_to_trip_ends, Unset):
            y2013_14_survey_shortest_path_to_trip_ends = UNSET
        else:
            y2013_14_survey_shortest_path_to_trip_ends = (
                self.y2013_14_survey_shortest_path_to_trip_ends
            )

        y2013_14_survey_shortest_travelling_time: None | str | Unset
        if isinstance(self.y2013_14_survey_shortest_travelling_time, Unset):
            y2013_14_survey_shortest_travelling_time = UNSET
        else:
            y2013_14_survey_shortest_travelling_time = (
                self.y2013_14_survey_shortest_travelling_time
            )

        y2013_14_survey_arranged_by_group_tours: None | str | Unset
        if isinstance(self.y2013_14_survey_arranged_by_group_tours, Unset):
            y2013_14_survey_arranged_by_group_tours = UNSET
        else:
            y2013_14_survey_arranged_by_group_tours = (
                self.y2013_14_survey_arranged_by_group_tours
            )

        y2013_14_survey_others: None | str | Unset
        if isinstance(self.y2013_14_survey_others, Unset):
            y2013_14_survey_others = UNSET
        else:
            y2013_14_survey_others = self.y2013_14_survey_others

        y2015_survey_proximity_to_trip_ends: None | str | Unset
        if isinstance(self.y2015_survey_proximity_to_trip_ends, Unset):
            y2015_survey_proximity_to_trip_ends = UNSET
        else:
            y2015_survey_proximity_to_trip_ends = (
                self.y2015_survey_proximity_to_trip_ends
            )

        y2015_survey_proximity_to_the_hubs_for_connecting_transport: None | str | Unset
        if isinstance(
            self.y2015_survey_proximity_to_the_hubs_for_connecting_transport, Unset
        ):
            y2015_survey_proximity_to_the_hubs_for_connecting_transport = UNSET
        else:
            y2015_survey_proximity_to_the_hubs_for_connecting_transport = (
                self.y2015_survey_proximity_to_the_hubs_for_connecting_transport
            )

        y2015_survey_shortest_travelling_time: None | str | Unset
        if isinstance(self.y2015_survey_shortest_travelling_time, Unset):
            y2015_survey_shortest_travelling_time = UNSET
        else:
            y2015_survey_shortest_travelling_time = (
                self.y2015_survey_shortest_travelling_time
            )

        y2015_survey_shortest_path_to_trip_ends: None | str | Unset
        if isinstance(self.y2015_survey_shortest_path_to_trip_ends, Unset):
            y2015_survey_shortest_path_to_trip_ends = UNSET
        else:
            y2015_survey_shortest_path_to_trip_ends = (
                self.y2015_survey_shortest_path_to_trip_ends
            )

        y2015_survey_arranged_by_group_tours: None | str | Unset
        if isinstance(self.y2015_survey_arranged_by_group_tours, Unset):
            y2015_survey_arranged_by_group_tours = UNSET
        else:
            y2015_survey_arranged_by_group_tours = (
                self.y2015_survey_arranged_by_group_tours
            )

        y2015_survey_others: None | str | Unset
        if isinstance(self.y2015_survey_others, Unset):
            y2015_survey_others = UNSET
        else:
            y2015_survey_others = self.y2015_survey_others

        y2017_survey_proximity_to_trip_ends: None | str | Unset
        if isinstance(self.y2017_survey_proximity_to_trip_ends, Unset):
            y2017_survey_proximity_to_trip_ends = UNSET
        else:
            y2017_survey_proximity_to_trip_ends = (
                self.y2017_survey_proximity_to_trip_ends
            )

        y2017_survey_proximity_to_the_hubs_for_connecting_transport: None | str | Unset
        if isinstance(
            self.y2017_survey_proximity_to_the_hubs_for_connecting_transport, Unset
        ):
            y2017_survey_proximity_to_the_hubs_for_connecting_transport = UNSET
        else:
            y2017_survey_proximity_to_the_hubs_for_connecting_transport = (
                self.y2017_survey_proximity_to_the_hubs_for_connecting_transport
            )

        y2017_survey_convenient_customs_immigration_and_quarantine_ciq: (
            None | str | Unset
        )
        if isinstance(
            self.y2017_survey_convenient_customs_immigration_and_quarantine_ciq, Unset
        ):
            y2017_survey_convenient_customs_immigration_and_quarantine_ciq = UNSET
        else:
            y2017_survey_convenient_customs_immigration_and_quarantine_ciq = (
                self.y2017_survey_convenient_customs_immigration_and_quarantine_ciq
            )

        y2017_survey_shortest_path_to_trip_ends: None | str | Unset
        if isinstance(self.y2017_survey_shortest_path_to_trip_ends, Unset):
            y2017_survey_shortest_path_to_trip_ends = UNSET
        else:
            y2017_survey_shortest_path_to_trip_ends = (
                self.y2017_survey_shortest_path_to_trip_ends
            )

        y2017_survey_arranged_by_group_tours: None | str | Unset
        if isinstance(self.y2017_survey_arranged_by_group_tours, Unset):
            y2017_survey_arranged_by_group_tours = UNSET
        else:
            y2017_survey_arranged_by_group_tours = (
                self.y2017_survey_arranged_by_group_tours
            )

        y2017_survey_others: None | str | Unset
        if isinstance(self.y2017_survey_others, Unset):
            y2017_survey_others = UNSET
        else:
            y2017_survey_others = self.y2017_survey_others

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid_1 is not UNSET:
            field_dict["OBJECTID_1"] = objectid_1
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if cp_en is not UNSET:
            field_dict["CP_En"] = cp_en
        if y2013_14_survey_proximity_to_trip_ends is not UNSET:
            field_dict["Y2013_14_Survey_Proximity_to_trip_ends"] = (
                y2013_14_survey_proximity_to_trip_ends
            )
        if y2013_14_survey_proximity_to_the_hubs_for_connecting_transport is not UNSET:
            field_dict[
                "Y2013_14_Survey_Proximity_to_the_hubs_for_connecting_transport"
            ] = y2013_14_survey_proximity_to_the_hubs_for_connecting_transport
        if y2013_14_survey_shortest_path_to_trip_ends is not UNSET:
            field_dict["Y2013_14_Survey_Shortest_path_to_trip_ends"] = (
                y2013_14_survey_shortest_path_to_trip_ends
            )
        if y2013_14_survey_shortest_travelling_time is not UNSET:
            field_dict["Y2013_14_Survey_Shortest_travelling_time"] = (
                y2013_14_survey_shortest_travelling_time
            )
        if y2013_14_survey_arranged_by_group_tours is not UNSET:
            field_dict["Y2013_14_Survey_Arranged_by_group_tours"] = (
                y2013_14_survey_arranged_by_group_tours
            )
        if y2013_14_survey_others is not UNSET:
            field_dict["Y2013_14_Survey_Others"] = y2013_14_survey_others
        if y2015_survey_proximity_to_trip_ends is not UNSET:
            field_dict["Y2015_Survey_Proximity_to_trip_ends"] = (
                y2015_survey_proximity_to_trip_ends
            )
        if y2015_survey_proximity_to_the_hubs_for_connecting_transport is not UNSET:
            field_dict[
                "Y2015_Survey_Proximity_to_the_hubs_for_connecting_transport"
            ] = y2015_survey_proximity_to_the_hubs_for_connecting_transport
        if y2015_survey_shortest_travelling_time is not UNSET:
            field_dict["Y2015_Survey_Shortest_travelling_time"] = (
                y2015_survey_shortest_travelling_time
            )
        if y2015_survey_shortest_path_to_trip_ends is not UNSET:
            field_dict["Y2015_Survey_Shortest_path_to_trip_ends"] = (
                y2015_survey_shortest_path_to_trip_ends
            )
        if y2015_survey_arranged_by_group_tours is not UNSET:
            field_dict["Y2015_Survey_Arranged_by_group_tours"] = (
                y2015_survey_arranged_by_group_tours
            )
        if y2015_survey_others is not UNSET:
            field_dict["Y2015_Survey_Others"] = y2015_survey_others
        if y2017_survey_proximity_to_trip_ends is not UNSET:
            field_dict["Y2017_Survey_Proximity_to_trip_ends"] = (
                y2017_survey_proximity_to_trip_ends
            )
        if y2017_survey_proximity_to_the_hubs_for_connecting_transport is not UNSET:
            field_dict[
                "Y2017_Survey_Proximity_to_the_hubs_for_connecting_transport"
            ] = y2017_survey_proximity_to_the_hubs_for_connecting_transport
        if y2017_survey_convenient_customs_immigration_and_quarantine_ciq is not UNSET:
            field_dict[
                "Y2017_Survey_Convenient_customs_immigration_and_quarantine_CIQ"
            ] = y2017_survey_convenient_customs_immigration_and_quarantine_ciq
        if y2017_survey_shortest_path_to_trip_ends is not UNSET:
            field_dict["Y2017_Survey_Shortest_path_to_trip_ends"] = (
                y2017_survey_shortest_path_to_trip_ends
            )
        if y2017_survey_arranged_by_group_tours is not UNSET:
            field_dict["Y2017_Survey_Arranged_by_group_tours"] = (
                y2017_survey_arranged_by_group_tours
            )
        if y2017_survey_others is not UNSET:
            field_dict["Y2017_Survey_Others"] = y2017_survey_others

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid_1 = d.pop("OBJECTID_1", UNSET)

        def _parse_objectid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        objectid = _parse_objectid(d.pop("OBJECTID", UNSET))

        def _parse_cp_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cp_en = _parse_cp_en(d.pop("CP_En", UNSET))

        def _parse_y2013_14_survey_proximity_to_trip_ends(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2013_14_survey_proximity_to_trip_ends = (
            _parse_y2013_14_survey_proximity_to_trip_ends(
                d.pop("Y2013_14_Survey_Proximity_to_trip_ends", UNSET)
            )
        )

        def _parse_y2013_14_survey_proximity_to_the_hubs_for_connecting_transport(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2013_14_survey_proximity_to_the_hubs_for_connecting_transport = (
            _parse_y2013_14_survey_proximity_to_the_hubs_for_connecting_transport(
                d.pop(
                    "Y2013_14_Survey_Proximity_to_the_hubs_for_connecting_transport",
                    UNSET,
                )
            )
        )

        def _parse_y2013_14_survey_shortest_path_to_trip_ends(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2013_14_survey_shortest_path_to_trip_ends = (
            _parse_y2013_14_survey_shortest_path_to_trip_ends(
                d.pop("Y2013_14_Survey_Shortest_path_to_trip_ends", UNSET)
            )
        )

        def _parse_y2013_14_survey_shortest_travelling_time(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2013_14_survey_shortest_travelling_time = (
            _parse_y2013_14_survey_shortest_travelling_time(
                d.pop("Y2013_14_Survey_Shortest_travelling_time", UNSET)
            )
        )

        def _parse_y2013_14_survey_arranged_by_group_tours(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2013_14_survey_arranged_by_group_tours = (
            _parse_y2013_14_survey_arranged_by_group_tours(
                d.pop("Y2013_14_Survey_Arranged_by_group_tours", UNSET)
            )
        )

        def _parse_y2013_14_survey_others(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2013_14_survey_others = _parse_y2013_14_survey_others(
            d.pop("Y2013_14_Survey_Others", UNSET)
        )

        def _parse_y2015_survey_proximity_to_trip_ends(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2015_survey_proximity_to_trip_ends = (
            _parse_y2015_survey_proximity_to_trip_ends(
                d.pop("Y2015_Survey_Proximity_to_trip_ends", UNSET)
            )
        )

        def _parse_y2015_survey_proximity_to_the_hubs_for_connecting_transport(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2015_survey_proximity_to_the_hubs_for_connecting_transport = (
            _parse_y2015_survey_proximity_to_the_hubs_for_connecting_transport(
                d.pop(
                    "Y2015_Survey_Proximity_to_the_hubs_for_connecting_transport", UNSET
                )
            )
        )

        def _parse_y2015_survey_shortest_travelling_time(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2015_survey_shortest_travelling_time = (
            _parse_y2015_survey_shortest_travelling_time(
                d.pop("Y2015_Survey_Shortest_travelling_time", UNSET)
            )
        )

        def _parse_y2015_survey_shortest_path_to_trip_ends(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2015_survey_shortest_path_to_trip_ends = (
            _parse_y2015_survey_shortest_path_to_trip_ends(
                d.pop("Y2015_Survey_Shortest_path_to_trip_ends", UNSET)
            )
        )

        def _parse_y2015_survey_arranged_by_group_tours(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2015_survey_arranged_by_group_tours = (
            _parse_y2015_survey_arranged_by_group_tours(
                d.pop("Y2015_Survey_Arranged_by_group_tours", UNSET)
            )
        )

        def _parse_y2015_survey_others(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2015_survey_others = _parse_y2015_survey_others(
            d.pop("Y2015_Survey_Others", UNSET)
        )

        def _parse_y2017_survey_proximity_to_trip_ends(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2017_survey_proximity_to_trip_ends = (
            _parse_y2017_survey_proximity_to_trip_ends(
                d.pop("Y2017_Survey_Proximity_to_trip_ends", UNSET)
            )
        )

        def _parse_y2017_survey_proximity_to_the_hubs_for_connecting_transport(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2017_survey_proximity_to_the_hubs_for_connecting_transport = (
            _parse_y2017_survey_proximity_to_the_hubs_for_connecting_transport(
                d.pop(
                    "Y2017_Survey_Proximity_to_the_hubs_for_connecting_transport", UNSET
                )
            )
        )

        def _parse_y2017_survey_convenient_customs_immigration_and_quarantine_ciq(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2017_survey_convenient_customs_immigration_and_quarantine_ciq = (
            _parse_y2017_survey_convenient_customs_immigration_and_quarantine_ciq(
                d.pop(
                    "Y2017_Survey_Convenient_customs_immigration_and_quarantine_CIQ",
                    UNSET,
                )
            )
        )

        def _parse_y2017_survey_shortest_path_to_trip_ends(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2017_survey_shortest_path_to_trip_ends = (
            _parse_y2017_survey_shortest_path_to_trip_ends(
                d.pop("Y2017_Survey_Shortest_path_to_trip_ends", UNSET)
            )
        )

        def _parse_y2017_survey_arranged_by_group_tours(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2017_survey_arranged_by_group_tours = (
            _parse_y2017_survey_arranged_by_group_tours(
                d.pop("Y2017_Survey_Arranged_by_group_tours", UNSET)
            )
        )

        def _parse_y2017_survey_others(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y2017_survey_others = _parse_y2017_survey_others(
            d.pop("Y2017_Survey_Others", UNSET)
        )

        arcgis_feature_server_arcgis_layer_1010_attributes = cls(
            objectid_1=objectid_1,
            objectid=objectid,
            cp_en=cp_en,
            y2013_14_survey_proximity_to_trip_ends=y2013_14_survey_proximity_to_trip_ends,
            y2013_14_survey_proximity_to_the_hubs_for_connecting_transport=y2013_14_survey_proximity_to_the_hubs_for_connecting_transport,
            y2013_14_survey_shortest_path_to_trip_ends=y2013_14_survey_shortest_path_to_trip_ends,
            y2013_14_survey_shortest_travelling_time=y2013_14_survey_shortest_travelling_time,
            y2013_14_survey_arranged_by_group_tours=y2013_14_survey_arranged_by_group_tours,
            y2013_14_survey_others=y2013_14_survey_others,
            y2015_survey_proximity_to_trip_ends=y2015_survey_proximity_to_trip_ends,
            y2015_survey_proximity_to_the_hubs_for_connecting_transport=y2015_survey_proximity_to_the_hubs_for_connecting_transport,
            y2015_survey_shortest_travelling_time=y2015_survey_shortest_travelling_time,
            y2015_survey_shortest_path_to_trip_ends=y2015_survey_shortest_path_to_trip_ends,
            y2015_survey_arranged_by_group_tours=y2015_survey_arranged_by_group_tours,
            y2015_survey_others=y2015_survey_others,
            y2017_survey_proximity_to_trip_ends=y2017_survey_proximity_to_trip_ends,
            y2017_survey_proximity_to_the_hubs_for_connecting_transport=y2017_survey_proximity_to_the_hubs_for_connecting_transport,
            y2017_survey_convenient_customs_immigration_and_quarantine_ciq=y2017_survey_convenient_customs_immigration_and_quarantine_ciq,
            y2017_survey_shortest_path_to_trip_ends=y2017_survey_shortest_path_to_trip_ends,
            y2017_survey_arranged_by_group_tours=y2017_survey_arranged_by_group_tours,
            y2017_survey_others=y2017_survey_others,
        )

        arcgis_feature_server_arcgis_layer_1010_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1010_attributes

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
