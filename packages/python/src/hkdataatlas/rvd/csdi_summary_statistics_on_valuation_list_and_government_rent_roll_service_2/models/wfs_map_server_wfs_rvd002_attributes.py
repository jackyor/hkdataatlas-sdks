from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsRVD002Attributes")


@_attrs_define
class WfsMapServerWfsRVD002Attributes:
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
        class_a_b_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        class_a_b_number_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        class_a_b_rv_hkd_in_thousand (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        class_a_b_rv_hkd_in_thousand_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        class_c_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        class_c_number_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        class_c_rv_hkd_in_thousand (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        class_c_rv_hkd_in_thousand_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        class_d_e_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        class_d_e_number_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        class_d_e_rv_hkd_in_thousand (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        class_d_e_rv_hkd_in_thousand_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        misc_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        misc_number_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        misc_rv_hkd_in_thousand (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        misc_rv_hkd_in_thousand_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        total_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        total_number_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        total_rv_hkd_in_thousand (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        total_rv_hkd_in_thousand_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
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
    class_a_b_number: None | str | Unset = UNSET
    class_a_b_number_tc: None | str | Unset = UNSET
    class_a_b_rv_hkd_in_thousand: None | str | Unset = UNSET
    class_a_b_rv_hkd_in_thousand_tc: None | str | Unset = UNSET
    class_c_number: None | str | Unset = UNSET
    class_c_number_tc: None | str | Unset = UNSET
    class_c_rv_hkd_in_thousand: None | str | Unset = UNSET
    class_c_rv_hkd_in_thousand_tc: None | str | Unset = UNSET
    class_d_e_number: None | str | Unset = UNSET
    class_d_e_number_tc: None | str | Unset = UNSET
    class_d_e_rv_hkd_in_thousand: None | str | Unset = UNSET
    class_d_e_rv_hkd_in_thousand_tc: None | str | Unset = UNSET
    misc_number: None | str | Unset = UNSET
    misc_number_tc: None | str | Unset = UNSET
    misc_rv_hkd_in_thousand: None | str | Unset = UNSET
    misc_rv_hkd_in_thousand_tc: None | str | Unset = UNSET
    total_number: None | str | Unset = UNSET
    total_number_tc: None | str | Unset = UNSET
    total_rv_hkd_in_thousand: None | str | Unset = UNSET
    total_rv_hkd_in_thousand_tc: None | str | Unset = UNSET
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

        class_a_b_number: None | str | Unset
        if isinstance(self.class_a_b_number, Unset):
            class_a_b_number = UNSET
        else:
            class_a_b_number = self.class_a_b_number

        class_a_b_number_tc: None | str | Unset
        if isinstance(self.class_a_b_number_tc, Unset):
            class_a_b_number_tc = UNSET
        else:
            class_a_b_number_tc = self.class_a_b_number_tc

        class_a_b_rv_hkd_in_thousand: None | str | Unset
        if isinstance(self.class_a_b_rv_hkd_in_thousand, Unset):
            class_a_b_rv_hkd_in_thousand = UNSET
        else:
            class_a_b_rv_hkd_in_thousand = self.class_a_b_rv_hkd_in_thousand

        class_a_b_rv_hkd_in_thousand_tc: None | str | Unset
        if isinstance(self.class_a_b_rv_hkd_in_thousand_tc, Unset):
            class_a_b_rv_hkd_in_thousand_tc = UNSET
        else:
            class_a_b_rv_hkd_in_thousand_tc = self.class_a_b_rv_hkd_in_thousand_tc

        class_c_number: None | str | Unset
        if isinstance(self.class_c_number, Unset):
            class_c_number = UNSET
        else:
            class_c_number = self.class_c_number

        class_c_number_tc: None | str | Unset
        if isinstance(self.class_c_number_tc, Unset):
            class_c_number_tc = UNSET
        else:
            class_c_number_tc = self.class_c_number_tc

        class_c_rv_hkd_in_thousand: None | str | Unset
        if isinstance(self.class_c_rv_hkd_in_thousand, Unset):
            class_c_rv_hkd_in_thousand = UNSET
        else:
            class_c_rv_hkd_in_thousand = self.class_c_rv_hkd_in_thousand

        class_c_rv_hkd_in_thousand_tc: None | str | Unset
        if isinstance(self.class_c_rv_hkd_in_thousand_tc, Unset):
            class_c_rv_hkd_in_thousand_tc = UNSET
        else:
            class_c_rv_hkd_in_thousand_tc = self.class_c_rv_hkd_in_thousand_tc

        class_d_e_number: None | str | Unset
        if isinstance(self.class_d_e_number, Unset):
            class_d_e_number = UNSET
        else:
            class_d_e_number = self.class_d_e_number

        class_d_e_number_tc: None | str | Unset
        if isinstance(self.class_d_e_number_tc, Unset):
            class_d_e_number_tc = UNSET
        else:
            class_d_e_number_tc = self.class_d_e_number_tc

        class_d_e_rv_hkd_in_thousand: None | str | Unset
        if isinstance(self.class_d_e_rv_hkd_in_thousand, Unset):
            class_d_e_rv_hkd_in_thousand = UNSET
        else:
            class_d_e_rv_hkd_in_thousand = self.class_d_e_rv_hkd_in_thousand

        class_d_e_rv_hkd_in_thousand_tc: None | str | Unset
        if isinstance(self.class_d_e_rv_hkd_in_thousand_tc, Unset):
            class_d_e_rv_hkd_in_thousand_tc = UNSET
        else:
            class_d_e_rv_hkd_in_thousand_tc = self.class_d_e_rv_hkd_in_thousand_tc

        misc_number: None | str | Unset
        if isinstance(self.misc_number, Unset):
            misc_number = UNSET
        else:
            misc_number = self.misc_number

        misc_number_tc: None | str | Unset
        if isinstance(self.misc_number_tc, Unset):
            misc_number_tc = UNSET
        else:
            misc_number_tc = self.misc_number_tc

        misc_rv_hkd_in_thousand: None | str | Unset
        if isinstance(self.misc_rv_hkd_in_thousand, Unset):
            misc_rv_hkd_in_thousand = UNSET
        else:
            misc_rv_hkd_in_thousand = self.misc_rv_hkd_in_thousand

        misc_rv_hkd_in_thousand_tc: None | str | Unset
        if isinstance(self.misc_rv_hkd_in_thousand_tc, Unset):
            misc_rv_hkd_in_thousand_tc = UNSET
        else:
            misc_rv_hkd_in_thousand_tc = self.misc_rv_hkd_in_thousand_tc

        total_number: None | str | Unset
        if isinstance(self.total_number, Unset):
            total_number = UNSET
        else:
            total_number = self.total_number

        total_number_tc: None | str | Unset
        if isinstance(self.total_number_tc, Unset):
            total_number_tc = UNSET
        else:
            total_number_tc = self.total_number_tc

        total_rv_hkd_in_thousand: None | str | Unset
        if isinstance(self.total_rv_hkd_in_thousand, Unset):
            total_rv_hkd_in_thousand = UNSET
        else:
            total_rv_hkd_in_thousand = self.total_rv_hkd_in_thousand

        total_rv_hkd_in_thousand_tc: None | str | Unset
        if isinstance(self.total_rv_hkd_in_thousand_tc, Unset):
            total_rv_hkd_in_thousand_tc = UNSET
        else:
            total_rv_hkd_in_thousand_tc = self.total_rv_hkd_in_thousand_tc

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
        if class_a_b_number is not UNSET:
            field_dict["Class_A_B_Number"] = class_a_b_number
        if class_a_b_number_tc is not UNSET:
            field_dict["Class_A_B_Number_TC"] = class_a_b_number_tc
        if class_a_b_rv_hkd_in_thousand is not UNSET:
            field_dict["Class_A_B_RV_HKD_In_Thousand"] = class_a_b_rv_hkd_in_thousand
        if class_a_b_rv_hkd_in_thousand_tc is not UNSET:
            field_dict["Class_A_B_RV_HKD_In_Thousand_TC"] = (
                class_a_b_rv_hkd_in_thousand_tc
            )
        if class_c_number is not UNSET:
            field_dict["Class_C_Number"] = class_c_number
        if class_c_number_tc is not UNSET:
            field_dict["Class_C_Number_TC"] = class_c_number_tc
        if class_c_rv_hkd_in_thousand is not UNSET:
            field_dict["Class_C_RV_HKD_In_Thousand"] = class_c_rv_hkd_in_thousand
        if class_c_rv_hkd_in_thousand_tc is not UNSET:
            field_dict["Class_C_RV_HKD_In_Thousand_TC"] = class_c_rv_hkd_in_thousand_tc
        if class_d_e_number is not UNSET:
            field_dict["Class_D_E_Number"] = class_d_e_number
        if class_d_e_number_tc is not UNSET:
            field_dict["Class_D_E_Number_TC"] = class_d_e_number_tc
        if class_d_e_rv_hkd_in_thousand is not UNSET:
            field_dict["Class_D_E_RV_HKD_In_Thousand"] = class_d_e_rv_hkd_in_thousand
        if class_d_e_rv_hkd_in_thousand_tc is not UNSET:
            field_dict["Class_D_E_RV_HKD_In_Thousand_TC"] = (
                class_d_e_rv_hkd_in_thousand_tc
            )
        if misc_number is not UNSET:
            field_dict["Misc_Number"] = misc_number
        if misc_number_tc is not UNSET:
            field_dict["Misc_Number_TC"] = misc_number_tc
        if misc_rv_hkd_in_thousand is not UNSET:
            field_dict["Misc_RV_HKD_In_Thousand"] = misc_rv_hkd_in_thousand
        if misc_rv_hkd_in_thousand_tc is not UNSET:
            field_dict["Misc_RV_HKD_In_Thousand_TC"] = misc_rv_hkd_in_thousand_tc
        if total_number is not UNSET:
            field_dict["Total_Number"] = total_number
        if total_number_tc is not UNSET:
            field_dict["Total_Number_TC"] = total_number_tc
        if total_rv_hkd_in_thousand is not UNSET:
            field_dict["Total_RV_HKD_In_Thousand"] = total_rv_hkd_in_thousand
        if total_rv_hkd_in_thousand_tc is not UNSET:
            field_dict["Total_RV_HKD_In_Thousand_TC"] = total_rv_hkd_in_thousand_tc
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

        def _parse_class_a_b_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_a_b_number = _parse_class_a_b_number(d.pop("Class_A_B_Number", UNSET))

        def _parse_class_a_b_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_a_b_number_tc = _parse_class_a_b_number_tc(
            d.pop("Class_A_B_Number_TC", UNSET)
        )

        def _parse_class_a_b_rv_hkd_in_thousand(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_a_b_rv_hkd_in_thousand = _parse_class_a_b_rv_hkd_in_thousand(
            d.pop("Class_A_B_RV_HKD_In_Thousand", UNSET)
        )

        def _parse_class_a_b_rv_hkd_in_thousand_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_a_b_rv_hkd_in_thousand_tc = _parse_class_a_b_rv_hkd_in_thousand_tc(
            d.pop("Class_A_B_RV_HKD_In_Thousand_TC", UNSET)
        )

        def _parse_class_c_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_c_number = _parse_class_c_number(d.pop("Class_C_Number", UNSET))

        def _parse_class_c_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_c_number_tc = _parse_class_c_number_tc(d.pop("Class_C_Number_TC", UNSET))

        def _parse_class_c_rv_hkd_in_thousand(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_c_rv_hkd_in_thousand = _parse_class_c_rv_hkd_in_thousand(
            d.pop("Class_C_RV_HKD_In_Thousand", UNSET)
        )

        def _parse_class_c_rv_hkd_in_thousand_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_c_rv_hkd_in_thousand_tc = _parse_class_c_rv_hkd_in_thousand_tc(
            d.pop("Class_C_RV_HKD_In_Thousand_TC", UNSET)
        )

        def _parse_class_d_e_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_d_e_number = _parse_class_d_e_number(d.pop("Class_D_E_Number", UNSET))

        def _parse_class_d_e_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_d_e_number_tc = _parse_class_d_e_number_tc(
            d.pop("Class_D_E_Number_TC", UNSET)
        )

        def _parse_class_d_e_rv_hkd_in_thousand(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_d_e_rv_hkd_in_thousand = _parse_class_d_e_rv_hkd_in_thousand(
            d.pop("Class_D_E_RV_HKD_In_Thousand", UNSET)
        )

        def _parse_class_d_e_rv_hkd_in_thousand_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_d_e_rv_hkd_in_thousand_tc = _parse_class_d_e_rv_hkd_in_thousand_tc(
            d.pop("Class_D_E_RV_HKD_In_Thousand_TC", UNSET)
        )

        def _parse_misc_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        misc_number = _parse_misc_number(d.pop("Misc_Number", UNSET))

        def _parse_misc_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        misc_number_tc = _parse_misc_number_tc(d.pop("Misc_Number_TC", UNSET))

        def _parse_misc_rv_hkd_in_thousand(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        misc_rv_hkd_in_thousand = _parse_misc_rv_hkd_in_thousand(
            d.pop("Misc_RV_HKD_In_Thousand", UNSET)
        )

        def _parse_misc_rv_hkd_in_thousand_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        misc_rv_hkd_in_thousand_tc = _parse_misc_rv_hkd_in_thousand_tc(
            d.pop("Misc_RV_HKD_In_Thousand_TC", UNSET)
        )

        def _parse_total_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_number = _parse_total_number(d.pop("Total_Number", UNSET))

        def _parse_total_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_number_tc = _parse_total_number_tc(d.pop("Total_Number_TC", UNSET))

        def _parse_total_rv_hkd_in_thousand(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_rv_hkd_in_thousand = _parse_total_rv_hkd_in_thousand(
            d.pop("Total_RV_HKD_In_Thousand", UNSET)
        )

        def _parse_total_rv_hkd_in_thousand_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_rv_hkd_in_thousand_tc = _parse_total_rv_hkd_in_thousand_tc(
            d.pop("Total_RV_HKD_In_Thousand_TC", UNSET)
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

        wfs_map_server_wfs_rvd002_attributes = cls(
            shape=shape,
            objectid=objectid,
            dataset=dataset,
            dataset_tc=dataset_tc,
            district=district,
            district_tc=district_tc,
            class_a_b_number=class_a_b_number,
            class_a_b_number_tc=class_a_b_number_tc,
            class_a_b_rv_hkd_in_thousand=class_a_b_rv_hkd_in_thousand,
            class_a_b_rv_hkd_in_thousand_tc=class_a_b_rv_hkd_in_thousand_tc,
            class_c_number=class_c_number,
            class_c_number_tc=class_c_number_tc,
            class_c_rv_hkd_in_thousand=class_c_rv_hkd_in_thousand,
            class_c_rv_hkd_in_thousand_tc=class_c_rv_hkd_in_thousand_tc,
            class_d_e_number=class_d_e_number,
            class_d_e_number_tc=class_d_e_number_tc,
            class_d_e_rv_hkd_in_thousand=class_d_e_rv_hkd_in_thousand,
            class_d_e_rv_hkd_in_thousand_tc=class_d_e_rv_hkd_in_thousand_tc,
            misc_number=misc_number,
            misc_number_tc=misc_number_tc,
            misc_rv_hkd_in_thousand=misc_rv_hkd_in_thousand,
            misc_rv_hkd_in_thousand_tc=misc_rv_hkd_in_thousand_tc,
            total_number=total_number,
            total_number_tc=total_number_tc,
            total_rv_hkd_in_thousand=total_rv_hkd_in_thousand,
            total_rv_hkd_in_thousand_tc=total_rv_hkd_in_thousand_tc,
            last_update=last_update,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_rvd002_attributes.additional_properties = d
        return wfs_map_server_wfs_rvd002_attributes

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
