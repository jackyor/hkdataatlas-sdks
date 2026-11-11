from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsgeotaggingAttributes")


@_attrs_define
class WfsMapServerWfsgeotaggingAttributes:
    """
    Attributes:
        bbr (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        condition_chs (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        condition_cht (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        condition_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        department_ref_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        district_chs (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_cht (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        last_inspection_date (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        location_chs (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        location_cht (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        location_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        mitigation_measure_chs (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        mitigation_measure_cht (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        mitigation_measure_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        ovt_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        responsible_department_chs (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        responsible_department_cht (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        responsible_department_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        species_chs (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        species_cht (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        species_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        tr_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        type_ (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        x_coordinate (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        y_coordinate (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    bbr: None | str | Unset = UNSET
    condition_chs: None | str | Unset = UNSET
    condition_cht: None | str | Unset = UNSET
    condition_en: None | str | Unset = UNSET
    department_ref_no: None | str | Unset = UNSET
    district_chs: None | str | Unset = UNSET
    district_cht: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    last_inspection_date: None | str | Unset = UNSET
    location_chs: None | str | Unset = UNSET
    location_cht: None | str | Unset = UNSET
    location_en: None | str | Unset = UNSET
    mitigation_measure_chs: None | str | Unset = UNSET
    mitigation_measure_cht: None | str | Unset = UNSET
    mitigation_measure_en: None | str | Unset = UNSET
    ovt_no: None | str | Unset = UNSET
    responsible_department_chs: None | str | Unset = UNSET
    responsible_department_cht: None | str | Unset = UNSET
    responsible_department_en: None | str | Unset = UNSET
    species_chs: None | str | Unset = UNSET
    species_cht: None | str | Unset = UNSET
    species_en: None | str | Unset = UNSET
    tr_no: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    x_coordinate: float | None | Unset = UNSET
    y_coordinate: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bbr: None | str | Unset
        if isinstance(self.bbr, Unset):
            bbr = UNSET
        else:
            bbr = self.bbr

        condition_chs: None | str | Unset
        if isinstance(self.condition_chs, Unset):
            condition_chs = UNSET
        else:
            condition_chs = self.condition_chs

        condition_cht: None | str | Unset
        if isinstance(self.condition_cht, Unset):
            condition_cht = UNSET
        else:
            condition_cht = self.condition_cht

        condition_en: None | str | Unset
        if isinstance(self.condition_en, Unset):
            condition_en = UNSET
        else:
            condition_en = self.condition_en

        department_ref_no: None | str | Unset
        if isinstance(self.department_ref_no, Unset):
            department_ref_no = UNSET
        else:
            department_ref_no = self.department_ref_no

        district_chs: None | str | Unset
        if isinstance(self.district_chs, Unset):
            district_chs = UNSET
        else:
            district_chs = self.district_chs

        district_cht: None | str | Unset
        if isinstance(self.district_cht, Unset):
            district_cht = UNSET
        else:
            district_cht = self.district_cht

        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        last_inspection_date: None | str | Unset
        if isinstance(self.last_inspection_date, Unset):
            last_inspection_date = UNSET
        else:
            last_inspection_date = self.last_inspection_date

        location_chs: None | str | Unset
        if isinstance(self.location_chs, Unset):
            location_chs = UNSET
        else:
            location_chs = self.location_chs

        location_cht: None | str | Unset
        if isinstance(self.location_cht, Unset):
            location_cht = UNSET
        else:
            location_cht = self.location_cht

        location_en: None | str | Unset
        if isinstance(self.location_en, Unset):
            location_en = UNSET
        else:
            location_en = self.location_en

        mitigation_measure_chs: None | str | Unset
        if isinstance(self.mitigation_measure_chs, Unset):
            mitigation_measure_chs = UNSET
        else:
            mitigation_measure_chs = self.mitigation_measure_chs

        mitigation_measure_cht: None | str | Unset
        if isinstance(self.mitigation_measure_cht, Unset):
            mitigation_measure_cht = UNSET
        else:
            mitigation_measure_cht = self.mitigation_measure_cht

        mitigation_measure_en: None | str | Unset
        if isinstance(self.mitigation_measure_en, Unset):
            mitigation_measure_en = UNSET
        else:
            mitigation_measure_en = self.mitigation_measure_en

        ovt_no: None | str | Unset
        if isinstance(self.ovt_no, Unset):
            ovt_no = UNSET
        else:
            ovt_no = self.ovt_no

        responsible_department_chs: None | str | Unset
        if isinstance(self.responsible_department_chs, Unset):
            responsible_department_chs = UNSET
        else:
            responsible_department_chs = self.responsible_department_chs

        responsible_department_cht: None | str | Unset
        if isinstance(self.responsible_department_cht, Unset):
            responsible_department_cht = UNSET
        else:
            responsible_department_cht = self.responsible_department_cht

        responsible_department_en: None | str | Unset
        if isinstance(self.responsible_department_en, Unset):
            responsible_department_en = UNSET
        else:
            responsible_department_en = self.responsible_department_en

        species_chs: None | str | Unset
        if isinstance(self.species_chs, Unset):
            species_chs = UNSET
        else:
            species_chs = self.species_chs

        species_cht: None | str | Unset
        if isinstance(self.species_cht, Unset):
            species_cht = UNSET
        else:
            species_cht = self.species_cht

        species_en: None | str | Unset
        if isinstance(self.species_en, Unset):
            species_en = UNSET
        else:
            species_en = self.species_en

        tr_no: None | str | Unset
        if isinstance(self.tr_no, Unset):
            tr_no = UNSET
        else:
            tr_no = self.tr_no

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        x_coordinate: float | None | Unset
        if isinstance(self.x_coordinate, Unset):
            x_coordinate = UNSET
        else:
            x_coordinate = self.x_coordinate

        y_coordinate: float | None | Unset
        if isinstance(self.y_coordinate, Unset):
            y_coordinate = UNSET
        else:
            y_coordinate = self.y_coordinate

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bbr is not UNSET:
            field_dict["BBR"] = bbr
        if condition_chs is not UNSET:
            field_dict["Condition_CHS"] = condition_chs
        if condition_cht is not UNSET:
            field_dict["Condition_CHT"] = condition_cht
        if condition_en is not UNSET:
            field_dict["Condition_EN"] = condition_en
        if department_ref_no is not UNSET:
            field_dict["Department_Ref__No_"] = department_ref_no
        if district_chs is not UNSET:
            field_dict["District_CHS"] = district_chs
        if district_cht is not UNSET:
            field_dict["District_CHT"] = district_cht
        if district_en is not UNSET:
            field_dict["District_EN"] = district_en
        if last_inspection_date is not UNSET:
            field_dict["Last_Inspection_Date"] = last_inspection_date
        if location_chs is not UNSET:
            field_dict["Location_CHS"] = location_chs
        if location_cht is not UNSET:
            field_dict["Location_CHT"] = location_cht
        if location_en is not UNSET:
            field_dict["Location_EN"] = location_en
        if mitigation_measure_chs is not UNSET:
            field_dict["MitigationMeasure_CHS"] = mitigation_measure_chs
        if mitigation_measure_cht is not UNSET:
            field_dict["MitigationMeasure_CHT"] = mitigation_measure_cht
        if mitigation_measure_en is not UNSET:
            field_dict["MitigationMeasure_EN"] = mitigation_measure_en
        if ovt_no is not UNSET:
            field_dict["OVTNo"] = ovt_no
        if responsible_department_chs is not UNSET:
            field_dict["Responsible_Department_CHS"] = responsible_department_chs
        if responsible_department_cht is not UNSET:
            field_dict["Responsible_Department_CHT"] = responsible_department_cht
        if responsible_department_en is not UNSET:
            field_dict["Responsible_Department_EN"] = responsible_department_en
        if species_chs is not UNSET:
            field_dict["Species_CHS"] = species_chs
        if species_cht is not UNSET:
            field_dict["Species_CHT"] = species_cht
        if species_en is not UNSET:
            field_dict["Species_EN"] = species_en
        if tr_no is not UNSET:
            field_dict["TR_no_"] = tr_no
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if x_coordinate is not UNSET:
            field_dict["XCoordinate"] = x_coordinate
        if y_coordinate is not UNSET:
            field_dict["YCoordinate"] = y_coordinate
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_bbr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bbr = _parse_bbr(d.pop("BBR", UNSET))

        def _parse_condition_chs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        condition_chs = _parse_condition_chs(d.pop("Condition_CHS", UNSET))

        def _parse_condition_cht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        condition_cht = _parse_condition_cht(d.pop("Condition_CHT", UNSET))

        def _parse_condition_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        condition_en = _parse_condition_en(d.pop("Condition_EN", UNSET))

        def _parse_department_ref_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department_ref_no = _parse_department_ref_no(
            d.pop("Department_Ref__No_", UNSET)
        )

        def _parse_district_chs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_chs = _parse_district_chs(d.pop("District_CHS", UNSET))

        def _parse_district_cht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_cht = _parse_district_cht(d.pop("District_CHT", UNSET))

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("District_EN", UNSET))

        def _parse_last_inspection_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_inspection_date = _parse_last_inspection_date(
            d.pop("Last_Inspection_Date", UNSET)
        )

        def _parse_location_chs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_chs = _parse_location_chs(d.pop("Location_CHS", UNSET))

        def _parse_location_cht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_cht = _parse_location_cht(d.pop("Location_CHT", UNSET))

        def _parse_location_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_en = _parse_location_en(d.pop("Location_EN", UNSET))

        def _parse_mitigation_measure_chs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mitigation_measure_chs = _parse_mitigation_measure_chs(
            d.pop("MitigationMeasure_CHS", UNSET)
        )

        def _parse_mitigation_measure_cht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mitigation_measure_cht = _parse_mitigation_measure_cht(
            d.pop("MitigationMeasure_CHT", UNSET)
        )

        def _parse_mitigation_measure_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mitigation_measure_en = _parse_mitigation_measure_en(
            d.pop("MitigationMeasure_EN", UNSET)
        )

        def _parse_ovt_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ovt_no = _parse_ovt_no(d.pop("OVTNo", UNSET))

        def _parse_responsible_department_chs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        responsible_department_chs = _parse_responsible_department_chs(
            d.pop("Responsible_Department_CHS", UNSET)
        )

        def _parse_responsible_department_cht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        responsible_department_cht = _parse_responsible_department_cht(
            d.pop("Responsible_Department_CHT", UNSET)
        )

        def _parse_responsible_department_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        responsible_department_en = _parse_responsible_department_en(
            d.pop("Responsible_Department_EN", UNSET)
        )

        def _parse_species_chs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        species_chs = _parse_species_chs(d.pop("Species_CHS", UNSET))

        def _parse_species_cht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        species_cht = _parse_species_cht(d.pop("Species_CHT", UNSET))

        def _parse_species_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        species_en = _parse_species_en(d.pop("Species_EN", UNSET))

        def _parse_tr_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tr_no = _parse_tr_no(d.pop("TR_no_", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("Type", UNSET))

        def _parse_x_coordinate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        x_coordinate = _parse_x_coordinate(d.pop("XCoordinate", UNSET))

        def _parse_y_coordinate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        y_coordinate = _parse_y_coordinate(d.pop("YCoordinate", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            bbr=bbr,
            condition_chs=condition_chs,
            condition_cht=condition_cht,
            condition_en=condition_en,
            department_ref_no=department_ref_no,
            district_chs=district_chs,
            district_cht=district_cht,
            district_en=district_en,
            last_inspection_date=last_inspection_date,
            location_chs=location_chs,
            location_cht=location_cht,
            location_en=location_en,
            mitigation_measure_chs=mitigation_measure_chs,
            mitigation_measure_cht=mitigation_measure_cht,
            mitigation_measure_en=mitigation_measure_en,
            ovt_no=ovt_no,
            responsible_department_chs=responsible_department_chs,
            responsible_department_cht=responsible_department_cht,
            responsible_department_en=responsible_department_en,
            species_chs=species_chs,
            species_cht=species_cht,
            species_en=species_en,
            tr_no=tr_no,
            type_=type_,
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsgeotagging_attributes.additional_properties = d
        return wfs_map_server_wfsgeotagging_attributes

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
