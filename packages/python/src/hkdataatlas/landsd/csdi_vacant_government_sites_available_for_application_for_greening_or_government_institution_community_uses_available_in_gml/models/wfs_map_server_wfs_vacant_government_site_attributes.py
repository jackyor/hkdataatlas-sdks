from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsVacantGovernmentSiteAttributes")


@_attrs_define
class WfsMapServerWfsVacantGovernmentSiteAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        area_in_square_metres (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        dlo_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        location_zh (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        location_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        estimated_available_period_zh (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        estimated_available_period_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        remarks_zh (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        remarks_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        others_structures_with_details_zh (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        others_structures_with_details_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        application_closing_date (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        district_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_zh (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        application_status_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        application_status_zh (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        topography_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        topography_zh (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        accessibility_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        accessibility_zh (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        vegetation_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        vegetation_zh (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        tree_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        tree_zh (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        structure_within_site_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        structure_within_site_zh (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    area_in_square_metres: float | None | Unset = UNSET
    dlo_number: None | str | Unset = UNSET
    location_zh: None | str | Unset = UNSET
    location_en: None | str | Unset = UNSET
    estimated_available_period_zh: None | str | Unset = UNSET
    estimated_available_period_en: None | str | Unset = UNSET
    remarks_zh: None | str | Unset = UNSET
    remarks_en: None | str | Unset = UNSET
    others_structures_with_details_zh: None | str | Unset = UNSET
    others_structures_with_details_en: None | str | Unset = UNSET
    application_closing_date: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_zh: None | str | Unset = UNSET
    application_status_en: None | str | Unset = UNSET
    application_status_zh: None | str | Unset = UNSET
    topography_en: None | str | Unset = UNSET
    topography_zh: None | str | Unset = UNSET
    accessibility_en: None | str | Unset = UNSET
    accessibility_zh: None | str | Unset = UNSET
    vegetation_en: None | str | Unset = UNSET
    vegetation_zh: None | str | Unset = UNSET
    tree_en: None | str | Unset = UNSET
    tree_zh: None | str | Unset = UNSET
    structure_within_site_en: None | str | Unset = UNSET
    structure_within_site_zh: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        area_in_square_metres: float | None | Unset
        if isinstance(self.area_in_square_metres, Unset):
            area_in_square_metres = UNSET
        else:
            area_in_square_metres = self.area_in_square_metres

        dlo_number: None | str | Unset
        if isinstance(self.dlo_number, Unset):
            dlo_number = UNSET
        else:
            dlo_number = self.dlo_number

        location_zh: None | str | Unset
        if isinstance(self.location_zh, Unset):
            location_zh = UNSET
        else:
            location_zh = self.location_zh

        location_en: None | str | Unset
        if isinstance(self.location_en, Unset):
            location_en = UNSET
        else:
            location_en = self.location_en

        estimated_available_period_zh: None | str | Unset
        if isinstance(self.estimated_available_period_zh, Unset):
            estimated_available_period_zh = UNSET
        else:
            estimated_available_period_zh = self.estimated_available_period_zh

        estimated_available_period_en: None | str | Unset
        if isinstance(self.estimated_available_period_en, Unset):
            estimated_available_period_en = UNSET
        else:
            estimated_available_period_en = self.estimated_available_period_en

        remarks_zh: None | str | Unset
        if isinstance(self.remarks_zh, Unset):
            remarks_zh = UNSET
        else:
            remarks_zh = self.remarks_zh

        remarks_en: None | str | Unset
        if isinstance(self.remarks_en, Unset):
            remarks_en = UNSET
        else:
            remarks_en = self.remarks_en

        others_structures_with_details_zh: None | str | Unset
        if isinstance(self.others_structures_with_details_zh, Unset):
            others_structures_with_details_zh = UNSET
        else:
            others_structures_with_details_zh = self.others_structures_with_details_zh

        others_structures_with_details_en: None | str | Unset
        if isinstance(self.others_structures_with_details_en, Unset):
            others_structures_with_details_en = UNSET
        else:
            others_structures_with_details_en = self.others_structures_with_details_en

        application_closing_date: None | str | Unset
        if isinstance(self.application_closing_date, Unset):
            application_closing_date = UNSET
        else:
            application_closing_date = self.application_closing_date

        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        district_zh: None | str | Unset
        if isinstance(self.district_zh, Unset):
            district_zh = UNSET
        else:
            district_zh = self.district_zh

        application_status_en: None | str | Unset
        if isinstance(self.application_status_en, Unset):
            application_status_en = UNSET
        else:
            application_status_en = self.application_status_en

        application_status_zh: None | str | Unset
        if isinstance(self.application_status_zh, Unset):
            application_status_zh = UNSET
        else:
            application_status_zh = self.application_status_zh

        topography_en: None | str | Unset
        if isinstance(self.topography_en, Unset):
            topography_en = UNSET
        else:
            topography_en = self.topography_en

        topography_zh: None | str | Unset
        if isinstance(self.topography_zh, Unset):
            topography_zh = UNSET
        else:
            topography_zh = self.topography_zh

        accessibility_en: None | str | Unset
        if isinstance(self.accessibility_en, Unset):
            accessibility_en = UNSET
        else:
            accessibility_en = self.accessibility_en

        accessibility_zh: None | str | Unset
        if isinstance(self.accessibility_zh, Unset):
            accessibility_zh = UNSET
        else:
            accessibility_zh = self.accessibility_zh

        vegetation_en: None | str | Unset
        if isinstance(self.vegetation_en, Unset):
            vegetation_en = UNSET
        else:
            vegetation_en = self.vegetation_en

        vegetation_zh: None | str | Unset
        if isinstance(self.vegetation_zh, Unset):
            vegetation_zh = UNSET
        else:
            vegetation_zh = self.vegetation_zh

        tree_en: None | str | Unset
        if isinstance(self.tree_en, Unset):
            tree_en = UNSET
        else:
            tree_en = self.tree_en

        tree_zh: None | str | Unset
        if isinstance(self.tree_zh, Unset):
            tree_zh = UNSET
        else:
            tree_zh = self.tree_zh

        structure_within_site_en: None | str | Unset
        if isinstance(self.structure_within_site_en, Unset):
            structure_within_site_en = UNSET
        else:
            structure_within_site_en = self.structure_within_site_en

        structure_within_site_zh: None | str | Unset
        if isinstance(self.structure_within_site_zh, Unset):
            structure_within_site_zh = UNSET
        else:
            structure_within_site_zh = self.structure_within_site_zh

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
            field_dict["SHAPE"] = shape
        if area_in_square_metres is not UNSET:
            field_dict["areaInSquareMetres"] = area_in_square_metres
        if dlo_number is not UNSET:
            field_dict["dloNumber"] = dlo_number
        if location_zh is not UNSET:
            field_dict["locationZH"] = location_zh
        if location_en is not UNSET:
            field_dict["locationEN"] = location_en
        if estimated_available_period_zh is not UNSET:
            field_dict["estimatedAvailablePeriodZH"] = estimated_available_period_zh
        if estimated_available_period_en is not UNSET:
            field_dict["estimatedAvailablePeriodEN"] = estimated_available_period_en
        if remarks_zh is not UNSET:
            field_dict["remarksZH"] = remarks_zh
        if remarks_en is not UNSET:
            field_dict["remarksEN"] = remarks_en
        if others_structures_with_details_zh is not UNSET:
            field_dict["othersStructuresWithDetailsZH"] = (
                others_structures_with_details_zh
            )
        if others_structures_with_details_en is not UNSET:
            field_dict["othersStructuresWithDetailsEN"] = (
                others_structures_with_details_en
            )
        if application_closing_date is not UNSET:
            field_dict["applicationClosingDate"] = application_closing_date
        if district_en is not UNSET:
            field_dict["districtEN"] = district_en
        if district_zh is not UNSET:
            field_dict["districtZH"] = district_zh
        if application_status_en is not UNSET:
            field_dict["applicationStatusEN"] = application_status_en
        if application_status_zh is not UNSET:
            field_dict["applicationStatusZH"] = application_status_zh
        if topography_en is not UNSET:
            field_dict["topographyEN"] = topography_en
        if topography_zh is not UNSET:
            field_dict["topographyZH"] = topography_zh
        if accessibility_en is not UNSET:
            field_dict["accessibilityEN"] = accessibility_en
        if accessibility_zh is not UNSET:
            field_dict["accessibilityZH"] = accessibility_zh
        if vegetation_en is not UNSET:
            field_dict["vegetationEN"] = vegetation_en
        if vegetation_zh is not UNSET:
            field_dict["vegetationZH"] = vegetation_zh
        if tree_en is not UNSET:
            field_dict["treeEN"] = tree_en
        if tree_zh is not UNSET:
            field_dict["treeZH"] = tree_zh
        if structure_within_site_en is not UNSET:
            field_dict["structureWithinSiteEN"] = structure_within_site_en
        if structure_within_site_zh is not UNSET:
            field_dict["structureWithinSiteZH"] = structure_within_site_zh
        if shape_length is not UNSET:
            field_dict["SHAPE_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["SHAPE_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        def _parse_area_in_square_metres(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        area_in_square_metres = _parse_area_in_square_metres(
            d.pop("areaInSquareMetres", UNSET)
        )

        def _parse_dlo_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dlo_number = _parse_dlo_number(d.pop("dloNumber", UNSET))

        def _parse_location_zh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_zh = _parse_location_zh(d.pop("locationZH", UNSET))

        def _parse_location_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_en = _parse_location_en(d.pop("locationEN", UNSET))

        def _parse_estimated_available_period_zh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estimated_available_period_zh = _parse_estimated_available_period_zh(
            d.pop("estimatedAvailablePeriodZH", UNSET)
        )

        def _parse_estimated_available_period_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estimated_available_period_en = _parse_estimated_available_period_en(
            d.pop("estimatedAvailablePeriodEN", UNSET)
        )

        def _parse_remarks_zh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_zh = _parse_remarks_zh(d.pop("remarksZH", UNSET))

        def _parse_remarks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_en = _parse_remarks_en(d.pop("remarksEN", UNSET))

        def _parse_others_structures_with_details_zh(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        others_structures_with_details_zh = _parse_others_structures_with_details_zh(
            d.pop("othersStructuresWithDetailsZH", UNSET)
        )

        def _parse_others_structures_with_details_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        others_structures_with_details_en = _parse_others_structures_with_details_en(
            d.pop("othersStructuresWithDetailsEN", UNSET)
        )

        def _parse_application_closing_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_closing_date = _parse_application_closing_date(
            d.pop("applicationClosingDate", UNSET)
        )

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("districtEN", UNSET))

        def _parse_district_zh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_zh = _parse_district_zh(d.pop("districtZH", UNSET))

        def _parse_application_status_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_status_en = _parse_application_status_en(
            d.pop("applicationStatusEN", UNSET)
        )

        def _parse_application_status_zh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_status_zh = _parse_application_status_zh(
            d.pop("applicationStatusZH", UNSET)
        )

        def _parse_topography_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        topography_en = _parse_topography_en(d.pop("topographyEN", UNSET))

        def _parse_topography_zh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        topography_zh = _parse_topography_zh(d.pop("topographyZH", UNSET))

        def _parse_accessibility_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessibility_en = _parse_accessibility_en(d.pop("accessibilityEN", UNSET))

        def _parse_accessibility_zh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessibility_zh = _parse_accessibility_zh(d.pop("accessibilityZH", UNSET))

        def _parse_vegetation_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vegetation_en = _parse_vegetation_en(d.pop("vegetationEN", UNSET))

        def _parse_vegetation_zh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vegetation_zh = _parse_vegetation_zh(d.pop("vegetationZH", UNSET))

        def _parse_tree_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tree_en = _parse_tree_en(d.pop("treeEN", UNSET))

        def _parse_tree_zh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tree_zh = _parse_tree_zh(d.pop("treeZH", UNSET))

        def _parse_structure_within_site_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        structure_within_site_en = _parse_structure_within_site_en(
            d.pop("structureWithinSiteEN", UNSET)
        )

        def _parse_structure_within_site_zh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        structure_within_site_zh = _parse_structure_within_site_zh(
            d.pop("structureWithinSiteZH", UNSET)
        )

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("SHAPE_Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("SHAPE_Area", UNSET))

        wfs_map_server_wfs_vacant_government_site_attributes = cls(
            objectid=objectid,
            shape=shape,
            area_in_square_metres=area_in_square_metres,
            dlo_number=dlo_number,
            location_zh=location_zh,
            location_en=location_en,
            estimated_available_period_zh=estimated_available_period_zh,
            estimated_available_period_en=estimated_available_period_en,
            remarks_zh=remarks_zh,
            remarks_en=remarks_en,
            others_structures_with_details_zh=others_structures_with_details_zh,
            others_structures_with_details_en=others_structures_with_details_en,
            application_closing_date=application_closing_date,
            district_en=district_en,
            district_zh=district_zh,
            application_status_en=application_status_en,
            application_status_zh=application_status_zh,
            topography_en=topography_en,
            topography_zh=topography_zh,
            accessibility_en=accessibility_en,
            accessibility_zh=accessibility_zh,
            vegetation_en=vegetation_en,
            vegetation_zh=vegetation_zh,
            tree_en=tree_en,
            tree_zh=tree_zh,
            structure_within_site_en=structure_within_site_en,
            structure_within_site_zh=structure_within_site_zh,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_vacant_government_site_attributes.additional_properties = d
        return wfs_map_server_wfs_vacant_government_site_attributes

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
