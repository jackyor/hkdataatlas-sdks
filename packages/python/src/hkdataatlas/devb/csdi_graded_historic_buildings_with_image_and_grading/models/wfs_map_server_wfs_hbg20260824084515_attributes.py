from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsHBG20260824084515Attributes")


@_attrs_define
class WfsMapServerWfsHBG20260824084515Attributes:
    """
    Attributes:
        file_ref (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        grade (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        address (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        data_owner (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        distric_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        grade_year (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        grade_y_tc (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        fileref_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        dataset (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dataset_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        grade_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        url_image (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    file_ref: None | str | Unset = UNSET
    grade: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    data_owner: None | str | Unset = UNSET
    distric_tc: None | str | Unset = UNSET
    grade_year: int | None | Unset = UNSET
    grade_y_tc: int | None | Unset = UNSET
    fileref_tc: None | str | Unset = UNSET
    dataset: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    grade_tc: None | str | Unset = UNSET
    url_image: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_ref: None | str | Unset
        if isinstance(self.file_ref, Unset):
            file_ref = UNSET
        else:
            file_ref = self.file_ref

        grade: None | str | Unset
        if isinstance(self.grade, Unset):
            grade = UNSET
        else:
            grade = self.grade

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        data_owner: None | str | Unset
        if isinstance(self.data_owner, Unset):
            data_owner = UNSET
        else:
            data_owner = self.data_owner

        distric_tc: None | str | Unset
        if isinstance(self.distric_tc, Unset):
            distric_tc = UNSET
        else:
            distric_tc = self.distric_tc

        grade_year: int | None | Unset
        if isinstance(self.grade_year, Unset):
            grade_year = UNSET
        else:
            grade_year = self.grade_year

        grade_y_tc: int | None | Unset
        if isinstance(self.grade_y_tc, Unset):
            grade_y_tc = UNSET
        else:
            grade_y_tc = self.grade_y_tc

        fileref_tc: None | str | Unset
        if isinstance(self.fileref_tc, Unset):
            fileref_tc = UNSET
        else:
            fileref_tc = self.fileref_tc

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

        grade_tc: None | str | Unset
        if isinstance(self.grade_tc, Unset):
            grade_tc = UNSET
        else:
            grade_tc = self.grade_tc

        url_image: None | str | Unset
        if isinstance(self.url_image, Unset):
            url_image = UNSET
        else:
            url_image = self.url_image

        objectid = self.objectid

        shape = self.shape

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
        if file_ref is not UNSET:
            field_dict["FILE_REF"] = file_ref
        if grade is not UNSET:
            field_dict["GRADE"] = grade
        if name is not UNSET:
            field_dict["NAME"] = name
        if name_tc is not UNSET:
            field_dict["NAME_TC"] = name_tc
        if address is not UNSET:
            field_dict["ADDRESS"] = address
        if address_tc is not UNSET:
            field_dict["ADDRESS_TC"] = address_tc
        if district is not UNSET:
            field_dict["DISTRICT"] = district
        if data_owner is not UNSET:
            field_dict["DATA_OWNER"] = data_owner
        if distric_tc is not UNSET:
            field_dict["DISTRIC_TC"] = distric_tc
        if grade_year is not UNSET:
            field_dict["GRADE_YEAR"] = grade_year
        if grade_y_tc is not UNSET:
            field_dict["GRADE_Y_TC"] = grade_y_tc
        if fileref_tc is not UNSET:
            field_dict["FILEREF_TC"] = fileref_tc
        if dataset is not UNSET:
            field_dict["DATASET"] = dataset
        if dataset_tc is not UNSET:
            field_dict["DATASET_TC"] = dataset_tc
        if grade_tc is not UNSET:
            field_dict["GRADE_TC"] = grade_tc
        if url_image is not UNSET:
            field_dict["URL_IMAGE"] = url_image
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if shape_length is not UNSET:
            field_dict["SHAPE_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["SHAPE_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_file_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_ref = _parse_file_ref(d.pop("FILE_REF", UNSET))

        def _parse_grade(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grade = _parse_grade(d.pop("GRADE", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("NAME", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("NAME_TC", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("ADDRESS", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("ADDRESS_TC", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("DISTRICT", UNSET))

        def _parse_data_owner(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_owner = _parse_data_owner(d.pop("DATA_OWNER", UNSET))

        def _parse_distric_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        distric_tc = _parse_distric_tc(d.pop("DISTRIC_TC", UNSET))

        def _parse_grade_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        grade_year = _parse_grade_year(d.pop("GRADE_YEAR", UNSET))

        def _parse_grade_y_tc(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        grade_y_tc = _parse_grade_y_tc(d.pop("GRADE_Y_TC", UNSET))

        def _parse_fileref_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fileref_tc = _parse_fileref_tc(d.pop("FILEREF_TC", UNSET))

        def _parse_dataset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset = _parse_dataset(d.pop("DATASET", UNSET))

        def _parse_dataset_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_tc = _parse_dataset_tc(d.pop("DATASET_TC", UNSET))

        def _parse_grade_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grade_tc = _parse_grade_tc(d.pop("GRADE_TC", UNSET))

        def _parse_url_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_image = _parse_url_image(d.pop("URL_IMAGE", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

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

        wfs_map_server_wfs_hbg20260824084515_attributes = cls(
            file_ref=file_ref,
            grade=grade,
            name=name,
            name_tc=name_tc,
            address=address,
            address_tc=address_tc,
            district=district,
            data_owner=data_owner,
            distric_tc=distric_tc,
            grade_year=grade_year,
            grade_y_tc=grade_y_tc,
            fileref_tc=fileref_tc,
            dataset=dataset,
            dataset_tc=dataset_tc,
            grade_tc=grade_tc,
            url_image=url_image,
            objectid=objectid,
            shape=shape,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_hbg20260824084515_attributes.additional_properties = d
        return wfs_map_server_wfs_hbg20260824084515_attributes

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
