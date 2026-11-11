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
        location (None | str | Unset): Publisher field type: esriFieldTypeString
        limit_name (None | str | Unset): Publisher field type: esriFieldTypeString
        material (None | str | Unset): Publisher field type: esriFieldTypeString
        descriptio (None | str | Unset): Publisher field type: esriFieldTypeString
        marine_par (None | str | Unset): Publisher field type: esriFieldTypeString
        research_m (None | str | Unset): Publisher field type: esriFieldTypeString
        species (None | str | Unset): Publisher field type: esriFieldTypeString
        ref (None | str | Unset): Publisher field type: esriFieldTypeString
        last_updat (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        shape_st_ar (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_st_le (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    location: None | str | Unset = UNSET
    limit_name: None | str | Unset = UNSET
    material: None | str | Unset = UNSET
    descriptio: None | str | Unset = UNSET
    marine_par: None | str | Unset = UNSET
    research_m: None | str | Unset = UNSET
    species: None | str | Unset = UNSET
    ref: None | str | Unset = UNSET
    last_updat: Any | Unset = UNSET
    shape_st_ar: float | None | Unset = UNSET
    shape_st_le: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        limit_name: None | str | Unset
        if isinstance(self.limit_name, Unset):
            limit_name = UNSET
        else:
            limit_name = self.limit_name

        material: None | str | Unset
        if isinstance(self.material, Unset):
            material = UNSET
        else:
            material = self.material

        descriptio: None | str | Unset
        if isinstance(self.descriptio, Unset):
            descriptio = UNSET
        else:
            descriptio = self.descriptio

        marine_par: None | str | Unset
        if isinstance(self.marine_par, Unset):
            marine_par = UNSET
        else:
            marine_par = self.marine_par

        research_m: None | str | Unset
        if isinstance(self.research_m, Unset):
            research_m = UNSET
        else:
            research_m = self.research_m

        species: None | str | Unset
        if isinstance(self.species, Unset):
            species = UNSET
        else:
            species = self.species

        ref: None | str | Unset
        if isinstance(self.ref, Unset):
            ref = UNSET
        else:
            ref = self.ref

        last_updat = self.last_updat

        shape_st_ar: float | None | Unset
        if isinstance(self.shape_st_ar, Unset):
            shape_st_ar = UNSET
        else:
            shape_st_ar = self.shape_st_ar

        shape_st_le: float | None | Unset
        if isinstance(self.shape_st_le, Unset):
            shape_st_le = UNSET
        else:
            shape_st_le = self.shape_st_le

        objectid = self.objectid

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
        if location is not UNSET:
            field_dict["LOCATION"] = location
        if limit_name is not UNSET:
            field_dict["LIMIT_NAME"] = limit_name
        if material is not UNSET:
            field_dict["MATERIAL"] = material
        if descriptio is not UNSET:
            field_dict["DESCRIPTIO"] = descriptio
        if marine_par is not UNSET:
            field_dict["MARINE_PAR"] = marine_par
        if research_m is not UNSET:
            field_dict["RESEARCH_M"] = research_m
        if species is not UNSET:
            field_dict["SPECIES"] = species
        if ref is not UNSET:
            field_dict["REF"] = ref
        if last_updat is not UNSET:
            field_dict["LAST_UPDAT"] = last_updat
        if shape_st_ar is not UNSET:
            field_dict["Shape_STAr"] = shape_st_ar
        if shape_st_le is not UNSET:
            field_dict["Shape_STLe"] = shape_st_le
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("LOCATION", UNSET))

        def _parse_limit_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        limit_name = _parse_limit_name(d.pop("LIMIT_NAME", UNSET))

        def _parse_material(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        material = _parse_material(d.pop("MATERIAL", UNSET))

        def _parse_descriptio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        descriptio = _parse_descriptio(d.pop("DESCRIPTIO", UNSET))

        def _parse_marine_par(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        marine_par = _parse_marine_par(d.pop("MARINE_PAR", UNSET))

        def _parse_research_m(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        research_m = _parse_research_m(d.pop("RESEARCH_M", UNSET))

        def _parse_species(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        species = _parse_species(d.pop("SPECIES", UNSET))

        def _parse_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ref = _parse_ref(d.pop("REF", UNSET))

        last_updat = d.pop("LAST_UPDAT", UNSET)

        def _parse_shape_st_ar(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_st_ar = _parse_shape_st_ar(d.pop("Shape_STAr", UNSET))

        def _parse_shape_st_le(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_st_le = _parse_shape_st_le(d.pop("Shape_STLe", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape__Area", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            location=location,
            limit_name=limit_name,
            material=material,
            descriptio=descriptio,
            marine_par=marine_par,
            research_m=research_m,
            species=species,
            ref=ref,
            last_updat=last_updat,
            shape_st_ar=shape_st_ar,
            shape_st_le=shape_st_le,
            objectid=objectid,
            shape_length=shape_length,
            shape_area=shape_area,
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
