from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsFireSafetyComplaint18DistrictsAttributes")


@_attrs_define
class WfsMapServerWfsFireSafetyComplaint18DistrictsAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        district_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        from_ (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML occurrence into
            all JSON queries.
        to (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML occurrence into
            all JSON queries.
        building_type_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        building_type_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        building_type_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        obstruction_to_moe (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        locked_exit (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        smoke_stop_door_wedged (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        obstruction_to_eva (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        complaint_received (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        no_of_complaint_inspection (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected
            from XML occurrence into all JSON queries.
        fhan_issued (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        direct_prosecution_instituted (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected
            from XML occurrence into all JSON queries.
        prosecution_related_to_fhan (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected
            from XML occurrence into all JSON queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    from_: None | str | Unset = UNSET
    to: None | str | Unset = UNSET
    building_type_en: None | str | Unset = UNSET
    building_type_tc: None | str | Unset = UNSET
    building_type_sc: None | str | Unset = UNSET
    obstruction_to_moe: float | None | Unset = UNSET
    locked_exit: float | None | Unset = UNSET
    smoke_stop_door_wedged: float | None | Unset = UNSET
    obstruction_to_eva: float | None | Unset = UNSET
    complaint_received: float | None | Unset = UNSET
    no_of_complaint_inspection: float | None | Unset = UNSET
    fhan_issued: float | None | Unset = UNSET
    direct_prosecution_instituted: float | None | Unset = UNSET
    prosecution_related_to_fhan: float | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        district_sc: None | str | Unset
        if isinstance(self.district_sc, Unset):
            district_sc = UNSET
        else:
            district_sc = self.district_sc

        from_: None | str | Unset
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        to: None | str | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to

        building_type_en: None | str | Unset
        if isinstance(self.building_type_en, Unset):
            building_type_en = UNSET
        else:
            building_type_en = self.building_type_en

        building_type_tc: None | str | Unset
        if isinstance(self.building_type_tc, Unset):
            building_type_tc = UNSET
        else:
            building_type_tc = self.building_type_tc

        building_type_sc: None | str | Unset
        if isinstance(self.building_type_sc, Unset):
            building_type_sc = UNSET
        else:
            building_type_sc = self.building_type_sc

        obstruction_to_moe: float | None | Unset
        if isinstance(self.obstruction_to_moe, Unset):
            obstruction_to_moe = UNSET
        else:
            obstruction_to_moe = self.obstruction_to_moe

        locked_exit: float | None | Unset
        if isinstance(self.locked_exit, Unset):
            locked_exit = UNSET
        else:
            locked_exit = self.locked_exit

        smoke_stop_door_wedged: float | None | Unset
        if isinstance(self.smoke_stop_door_wedged, Unset):
            smoke_stop_door_wedged = UNSET
        else:
            smoke_stop_door_wedged = self.smoke_stop_door_wedged

        obstruction_to_eva: float | None | Unset
        if isinstance(self.obstruction_to_eva, Unset):
            obstruction_to_eva = UNSET
        else:
            obstruction_to_eva = self.obstruction_to_eva

        complaint_received: float | None | Unset
        if isinstance(self.complaint_received, Unset):
            complaint_received = UNSET
        else:
            complaint_received = self.complaint_received

        no_of_complaint_inspection: float | None | Unset
        if isinstance(self.no_of_complaint_inspection, Unset):
            no_of_complaint_inspection = UNSET
        else:
            no_of_complaint_inspection = self.no_of_complaint_inspection

        fhan_issued: float | None | Unset
        if isinstance(self.fhan_issued, Unset):
            fhan_issued = UNSET
        else:
            fhan_issued = self.fhan_issued

        direct_prosecution_instituted: float | None | Unset
        if isinstance(self.direct_prosecution_instituted, Unset):
            direct_prosecution_instituted = UNSET
        else:
            direct_prosecution_instituted = self.direct_prosecution_instituted

        prosecution_related_to_fhan: float | None | Unset
        if isinstance(self.prosecution_related_to_fhan, Unset):
            prosecution_related_to_fhan = UNSET
        else:
            prosecution_related_to_fhan = self.prosecution_related_to_fhan

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        shape_area: float | None | Unset
        if isinstance(self.shape_area, Unset):
            shape_area = UNSET
        else:
            shape_area = self.shape_area

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if district_en is not UNSET:
            field_dict["District_en"] = district_en
        if district_tc is not UNSET:
            field_dict["District_tc"] = district_tc
        if district_sc is not UNSET:
            field_dict["District_sc"] = district_sc
        if from_ is not UNSET:
            field_dict["From"] = from_
        if to is not UNSET:
            field_dict["To"] = to
        if building_type_en is not UNSET:
            field_dict["Building_Type_en"] = building_type_en
        if building_type_tc is not UNSET:
            field_dict["Building_Type_tc"] = building_type_tc
        if building_type_sc is not UNSET:
            field_dict["Building_Type_sc"] = building_type_sc
        if obstruction_to_moe is not UNSET:
            field_dict["Obstruction_to_MOE"] = obstruction_to_moe
        if locked_exit is not UNSET:
            field_dict["Locked_Exit"] = locked_exit
        if smoke_stop_door_wedged is not UNSET:
            field_dict["Smoke_Stop_Door_wedged"] = smoke_stop_door_wedged
        if obstruction_to_eva is not UNSET:
            field_dict["Obstruction_to_EVA"] = obstruction_to_eva
        if complaint_received is not UNSET:
            field_dict["Complaint_Received"] = complaint_received
        if no_of_complaint_inspection is not UNSET:
            field_dict["No_of_Complaint_Inspection"] = no_of_complaint_inspection
        if fhan_issued is not UNSET:
            field_dict["FHAN_Issued"] = fhan_issued
        if direct_prosecution_instituted is not UNSET:
            field_dict["Direct_Prosecution_Instituted"] = direct_prosecution_instituted
        if prosecution_related_to_fhan is not UNSET:
            field_dict["Prosecution_related_to_FHAN"] = prosecution_related_to_fhan
        if shape_length is not UNSET:
            field_dict["Shape_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("District_en", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("District_tc", UNSET))

        def _parse_district_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_sc = _parse_district_sc(d.pop("District_sc", UNSET))

        def _parse_from_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        from_ = _parse_from_(d.pop("From", UNSET))

        def _parse_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        to = _parse_to(d.pop("To", UNSET))

        def _parse_building_type_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_type_en = _parse_building_type_en(d.pop("Building_Type_en", UNSET))

        def _parse_building_type_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_type_tc = _parse_building_type_tc(d.pop("Building_Type_tc", UNSET))

        def _parse_building_type_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_type_sc = _parse_building_type_sc(d.pop("Building_Type_sc", UNSET))

        def _parse_obstruction_to_moe(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        obstruction_to_moe = _parse_obstruction_to_moe(
            d.pop("Obstruction_to_MOE", UNSET)
        )

        def _parse_locked_exit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        locked_exit = _parse_locked_exit(d.pop("Locked_Exit", UNSET))

        def _parse_smoke_stop_door_wedged(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        smoke_stop_door_wedged = _parse_smoke_stop_door_wedged(
            d.pop("Smoke_Stop_Door_wedged", UNSET)
        )

        def _parse_obstruction_to_eva(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        obstruction_to_eva = _parse_obstruction_to_eva(
            d.pop("Obstruction_to_EVA", UNSET)
        )

        def _parse_complaint_received(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        complaint_received = _parse_complaint_received(
            d.pop("Complaint_Received", UNSET)
        )

        def _parse_no_of_complaint_inspection(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        no_of_complaint_inspection = _parse_no_of_complaint_inspection(
            d.pop("No_of_Complaint_Inspection", UNSET)
        )

        def _parse_fhan_issued(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fhan_issued = _parse_fhan_issued(d.pop("FHAN_Issued", UNSET))

        def _parse_direct_prosecution_instituted(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        direct_prosecution_instituted = _parse_direct_prosecution_instituted(
            d.pop("Direct_Prosecution_Instituted", UNSET)
        )

        def _parse_prosecution_related_to_fhan(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        prosecution_related_to_fhan = _parse_prosecution_related_to_fhan(
            d.pop("Prosecution_related_to_FHAN", UNSET)
        )

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape_Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape_Area", UNSET))

        wfs_map_server_wfs_fire_safety_complaint_18_districts_attributes = cls(
            objectid=objectid,
            shape=shape,
            district_en=district_en,
            district_tc=district_tc,
            district_sc=district_sc,
            from_=from_,
            to=to,
            building_type_en=building_type_en,
            building_type_tc=building_type_tc,
            building_type_sc=building_type_sc,
            obstruction_to_moe=obstruction_to_moe,
            locked_exit=locked_exit,
            smoke_stop_door_wedged=smoke_stop_door_wedged,
            obstruction_to_eva=obstruction_to_eva,
            complaint_received=complaint_received,
            no_of_complaint_inspection=no_of_complaint_inspection,
            fhan_issued=fhan_issued,
            direct_prosecution_instituted=direct_prosecution_instituted,
            prosecution_related_to_fhan=prosecution_related_to_fhan,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_fire_safety_complaint_18_districts_attributes.additional_properties = d
        return wfs_map_server_wfs_fire_safety_complaint_18_districts_attributes

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
