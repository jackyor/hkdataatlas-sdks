from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsRVD017Attributes")


@_attrs_define
class WfsMapServerWfsRVD017Attributes:
    """
    Attributes:
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        dataset (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dataset_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        district_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        comp_2024 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        comp_2024_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        forecast_comp_2025 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        forecast_comp_2025_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        forecast_comp_2026 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        forecast_comp_2026_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        last_update (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    shape: Any | Unset = UNSET
    objectid: int | Unset = UNSET
    dataset: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    comp_2024: None | str | Unset = UNSET
    comp_2024_tc: None | str | Unset = UNSET
    forecast_comp_2025: None | str | Unset = UNSET
    forecast_comp_2025_tc: None | str | Unset = UNSET
    forecast_comp_2026: None | str | Unset = UNSET
    forecast_comp_2026_tc: None | str | Unset = UNSET
    last_update: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shape = self.shape

        objectid = self.objectid

        dataset: None | str | Unset
        if isinstance(self.dataset, Unset):
            dataset = UNSET
        else:
            dataset = self.dataset

        dataset_tc: None | str | Unset
        if isinstance(self.dataset_tc, Unset):
            dataset_tc = UNSET
        else:
            dataset_tc = self.dataset_tc

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        comp_2024: None | str | Unset
        if isinstance(self.comp_2024, Unset):
            comp_2024 = UNSET
        else:
            comp_2024 = self.comp_2024

        comp_2024_tc: None | str | Unset
        if isinstance(self.comp_2024_tc, Unset):
            comp_2024_tc = UNSET
        else:
            comp_2024_tc = self.comp_2024_tc

        forecast_comp_2025: None | str | Unset
        if isinstance(self.forecast_comp_2025, Unset):
            forecast_comp_2025 = UNSET
        else:
            forecast_comp_2025 = self.forecast_comp_2025

        forecast_comp_2025_tc: None | str | Unset
        if isinstance(self.forecast_comp_2025_tc, Unset):
            forecast_comp_2025_tc = UNSET
        else:
            forecast_comp_2025_tc = self.forecast_comp_2025_tc

        forecast_comp_2026: None | str | Unset
        if isinstance(self.forecast_comp_2026, Unset):
            forecast_comp_2026 = UNSET
        else:
            forecast_comp_2026 = self.forecast_comp_2026

        forecast_comp_2026_tc: None | str | Unset
        if isinstance(self.forecast_comp_2026_tc, Unset):
            forecast_comp_2026_tc = UNSET
        else:
            forecast_comp_2026_tc = self.forecast_comp_2026_tc

        last_update: None | str | Unset
        if isinstance(self.last_update, Unset):
            last_update = UNSET
        else:
            last_update = self.last_update

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
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if dataset is not UNSET:
            field_dict["Dataset"] = dataset
        if dataset_tc is not UNSET:
            field_dict["Dataset_TC"] = dataset_tc
        if district is not UNSET:
            field_dict["District"] = district
        if district_tc is not UNSET:
            field_dict["District_TC"] = district_tc
        if comp_2024 is not UNSET:
            field_dict["Comp_2024"] = comp_2024
        if comp_2024_tc is not UNSET:
            field_dict["Comp_2024_TC"] = comp_2024_tc
        if forecast_comp_2025 is not UNSET:
            field_dict["Forecast_Comp_2025"] = forecast_comp_2025
        if forecast_comp_2025_tc is not UNSET:
            field_dict["Forecast_Comp_2025_TC"] = forecast_comp_2025_tc
        if forecast_comp_2026 is not UNSET:
            field_dict["Forecast_Comp_2026"] = forecast_comp_2026
        if forecast_comp_2026_tc is not UNSET:
            field_dict["Forecast_Comp_2026_TC"] = forecast_comp_2026_tc
        if last_update is not UNSET:
            field_dict["LastUpdate"] = last_update
        if shape_length is not UNSET:
            field_dict["SHAPE_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["SHAPE_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        shape = d.pop("SHAPE", UNSET)

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_dataset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset = _parse_dataset(d.pop("Dataset", UNSET))

        def _parse_dataset_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_tc = _parse_dataset_tc(d.pop("Dataset_TC", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("District", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("District_TC", UNSET))

        def _parse_comp_2024(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comp_2024 = _parse_comp_2024(d.pop("Comp_2024", UNSET))

        def _parse_comp_2024_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comp_2024_tc = _parse_comp_2024_tc(d.pop("Comp_2024_TC", UNSET))

        def _parse_forecast_comp_2025(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2025 = _parse_forecast_comp_2025(
            d.pop("Forecast_Comp_2025", UNSET)
        )

        def _parse_forecast_comp_2025_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2025_tc = _parse_forecast_comp_2025_tc(
            d.pop("Forecast_Comp_2025_TC", UNSET)
        )

        def _parse_forecast_comp_2026(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2026 = _parse_forecast_comp_2026(
            d.pop("Forecast_Comp_2026", UNSET)
        )

        def _parse_forecast_comp_2026_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2026_tc = _parse_forecast_comp_2026_tc(
            d.pop("Forecast_Comp_2026_TC", UNSET)
        )

        def _parse_last_update(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_update = _parse_last_update(d.pop("LastUpdate", UNSET))

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

        wfs_map_server_wfs_rvd017_attributes = cls(
            shape=shape,
            objectid=objectid,
            dataset=dataset,
            dataset_tc=dataset_tc,
            district=district,
            district_tc=district_tc,
            comp_2024=comp_2024,
            comp_2024_tc=comp_2024_tc,
            forecast_comp_2025=forecast_comp_2025,
            forecast_comp_2025_tc=forecast_comp_2025_tc,
            forecast_comp_2026=forecast_comp_2026,
            forecast_comp_2026_tc=forecast_comp_2026_tc,
            last_update=last_update,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_rvd017_attributes.additional_properties = d
        return wfs_map_server_wfs_rvd017_attributes

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
