from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.localized_text import LocalizedText


T = TypeVar("T", bound="LocationProfileRecord")


@_attrs_define
class LocationProfileRecord:
    """A record may vary by selected resource. Dictionary field labels are represented using their documented label
    spellings; the API example instead uses underscore-separated spellings for several estate fields. The dictionary's
    multilingual text examples use en, zh-Hant, and zh-Hans keys. Language path values are documented as en, tc, and sc;
    the publisher does not explicitly define a mapping between those parameter values and dictionary keys.

        Attributes:
            CarparkManagement (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en, zh-
                Hant, and zh-Hans values. The examples do not establish that all three properties are always present.
            Carpark_Management (str | Unset): Key spelling appears in the API example; dictionary label is 'Carpark
                Management'.
            court_website (str | Unset): Website address of the court.
            DistrictName (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en, zh-Hant,
                and zh-Hans values. The examples do not establish that all three properties are always present.
            DistrictTenancyManagementOfficeEstateOffice (LocalizedText | Unset): Multilingual text object shown in
                dictionary examples with en, zh-Hant, and zh-Hans values. The examples do not establish that all three
                properties are always present.
            District_Name (str | Unset): Key spelling appears in the API example; dictionary label is 'District Name'.
            District_Tenancy_Management_Office_Estate_Office (str | Unset): Key spelling appears in the API example;
                dictionary label is 'District Tenancy Management Office/Estate Office'.
            EstateManagementAdvisoryCommitteeEMAC (LocalizedText | str | Unset): Whether an EMAC is established. The
                dictionary indicates a text value, and its examples show a localized object when formed; the example response
                uses an empty string under an underscore-separated key.
            estate_map_latitude (float | Unset): Latitude. The dictionary documents a numeric value with a precision pattern
                shown as <99.999999>. The API response example represents coordinates as strings, so either representation is
                allowed.
            estate_map_longitude (float | Unset): Longitude. The dictionary documents a numeric value with a precision
                pattern shown as <999.999999>. The API response example represents coordinates as strings, so either
                representation is allowed.
            EstateName (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en, zh-Hant, and
                zh-Hans values. The examples do not establish that all three properties are always present.
            EstateWebsite (str | Unset): Website address of the estate.
            Estate_Management_Advisory_Committee_EMAC (str | Unset): Key spelling and empty-string value appear in the API
                example; dictionary describes EMAC status as text and provides a localized formed value.
            Estate_Name (str | Unset): Key spelling appears in the API example; dictionary label is 'Estate Name'.
            Estate_Website (str | Unset): Key spelling appears in the API example; dictionary label is 'Estate Website'.
            factory_estate_office (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en,
                zh-Hant, and zh-Hans values. The examples do not establish that all three properties are always present.
            FlatSizem2 (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en, zh-Hant, and
                zh-Hans values. The examples do not establish that all three properties are always present.
            Flat_Size_m2 (str | Unset): Key spelling appears in the API example; dictionary label is 'Flat Size (m2)'.
            flatted_factories_website (str | Unset): Website address of the flatted factory estate.
            FurtherInformation (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en, zh-
                Hant, and zh-Hans values. The examples do not establish that all three properties are always present.
            Further_Information (str | Unset): Key spelling appears in the API example; dictionary label is 'Further
                Information'.
            gross_floor_area_of_flat_m_2 (str | Unset): Gross floor area range in square meters, documented in a text format
                like 'XXXXXXX - XXXXXXX'; each stated number may be from 0 to 9999999.
            initial_sale_price (str | Unset): Initial sale price range, documented in a text format like 'XXXXXXX -
                XXXXXXX'; each stated number may be from 0 to 9999999.
            name_of_blocks (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en, zh-Hant,
                and zh-Hans values. The examples do not establish that all three properties are always present.
            name_of_block (str | Unset): Key spelling appears in the API example; dictionary label is 'Name of Block(s)'.
            NoofBlocks (str | Unset): Block count as text in the dictionary; the example response also represents it as a
                string.
            no_of_flats (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en, zh-Hant, and
                zh-Hans values. The examples do not establish that all three properties are always present.
            no_of_floors (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en, zh-Hant,
                and zh-Hans values. The examples do not establish that all three properties are always present.
            NoofRentalFlats (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en, zh-Hant,
                and zh-Hans values. The examples do not establish that all three properties are always present.
            No_of_Blocks (str | Unset): Key spelling appears in the API example; dictionary describes the value as text.
            No_of_Rental_Flats (str | Unset): Key spelling appears in the API example; dictionary describes localized text.
            owners_corporation (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en, zh-
                Hant, and zh-Hans values. The examples do not establish that all three properties are always present.
            PropertyManagement (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en, zh-
                Hant, and zh-Hans values. The examples do not establish that all three properties are always present.
            Property_Management (str | Unset): Key spelling appears in the API example; dictionary label is 'Property
                Management'.
            RegionName (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en, zh-Hant, and
                zh-Hans values. The examples do not establish that all three properties are always present.
            Region_Name (str | Unset): Key spelling appears in the API example; dictionary label is 'Region Name'.
            regional_management_office_management_office_estate_office (LocalizedText | Unset): Multilingual text object
                shown in dictionary examples with en, zh-Hant, and zh-Hans values. The examples do not establish that all three
                properties are always present.
            saleable_area_of_flats_m_2 (str | Unset): Saleable area range in square meters, documented in a text format like
                'XXXXXXX - XXXXXXX'; each stated number may be from 0 to 9999999.
            shopping_centre_website (str | Unset): Website address of the shopping centre.
            sold_under (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en, zh-Hant, and
                zh-Hans values. The examples do not establish that all three properties are always present.
            storey (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en, zh-Hant, and zh-
                Hans values. The examples do not establish that all three properties are always present.
            total_lettable_area_m_2 (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en,
                zh-Hant, and zh-Hans values. The examples do not establish that all three properties are always present.
            TypeofEstate (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en, zh-Hant,
                and zh-Hans values. The examples do not establish that all three properties are always present.
            types_of_blocks (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en, zh-Hant,
                and zh-Hans values. The examples do not establish that all three properties are always present.
            type_of_block (str | Unset): Key spelling appears in the API example; dictionary label is 'Type(s) of Block(s)'.
            Type_of_Estate (str | Unset): Key spelling appears in the API example; dictionary label is 'Type of Estate'.
            year_of_completion (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en, zh-
                Hant, and zh-Hans values. The examples do not establish that all three properties are always present.
            YearofIntake (LocalizedText | Unset): Multilingual text object shown in dictionary examples with en, zh-Hant,
                and zh-Hans values. The examples do not establish that all three properties are always present.
            Year_of_Intake (str | Unset): Key spelling appears in the API example; dictionary describes localized text in
                yyyy format.
    """

    CarparkManagement: LocalizedText | Unset = UNSET
    Carpark_Management: str | Unset = UNSET
    court_website: str | Unset = UNSET
    DistrictName: LocalizedText | Unset = UNSET
    DistrictTenancyManagementOfficeEstateOffice: LocalizedText | Unset = UNSET
    District_Name: str | Unset = UNSET
    District_Tenancy_Management_Office_Estate_Office: str | Unset = UNSET
    EstateManagementAdvisoryCommitteeEMAC: LocalizedText | str | Unset = UNSET
    estate_map_latitude: float | Unset = UNSET
    estate_map_longitude: float | Unset = UNSET
    EstateName: LocalizedText | Unset = UNSET
    EstateWebsite: str | Unset = UNSET
    Estate_Management_Advisory_Committee_EMAC: str | Unset = UNSET
    Estate_Name: str | Unset = UNSET
    Estate_Website: str | Unset = UNSET
    factory_estate_office: LocalizedText | Unset = UNSET
    FlatSizem2: LocalizedText | Unset = UNSET
    Flat_Size_m2: str | Unset = UNSET
    flatted_factories_website: str | Unset = UNSET
    FurtherInformation: LocalizedText | Unset = UNSET
    Further_Information: str | Unset = UNSET
    gross_floor_area_of_flat_m_2: str | Unset = UNSET
    initial_sale_price: str | Unset = UNSET
    name_of_blocks: LocalizedText | Unset = UNSET
    name_of_block: str | Unset = UNSET
    NoofBlocks: str | Unset = UNSET
    no_of_flats: LocalizedText | Unset = UNSET
    no_of_floors: LocalizedText | Unset = UNSET
    NoofRentalFlats: LocalizedText | Unset = UNSET
    No_of_Blocks: str | Unset = UNSET
    No_of_Rental_Flats: str | Unset = UNSET
    owners_corporation: LocalizedText | Unset = UNSET
    PropertyManagement: LocalizedText | Unset = UNSET
    Property_Management: str | Unset = UNSET
    RegionName: LocalizedText | Unset = UNSET
    Region_Name: str | Unset = UNSET
    regional_management_office_management_office_estate_office: (
        LocalizedText | Unset
    ) = UNSET
    saleable_area_of_flats_m_2: str | Unset = UNSET
    shopping_centre_website: str | Unset = UNSET
    sold_under: LocalizedText | Unset = UNSET
    storey: LocalizedText | Unset = UNSET
    total_lettable_area_m_2: LocalizedText | Unset = UNSET
    TypeofEstate: LocalizedText | Unset = UNSET
    types_of_blocks: LocalizedText | Unset = UNSET
    type_of_block: str | Unset = UNSET
    Type_of_Estate: str | Unset = UNSET
    year_of_completion: LocalizedText | Unset = UNSET
    YearofIntake: LocalizedText | Unset = UNSET
    Year_of_Intake: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.localized_text import LocalizedText

        CarparkManagement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.CarparkManagement, Unset):
            CarparkManagement = self.CarparkManagement.to_dict()

        Carpark_Management = self.Carpark_Management

        court_website = self.court_website

        DistrictName: dict[str, Any] | Unset = UNSET
        if not isinstance(self.DistrictName, Unset):
            DistrictName = self.DistrictName.to_dict()

        DistrictTenancyManagementOfficeEstateOffice: dict[str, Any] | Unset = UNSET
        if not isinstance(self.DistrictTenancyManagementOfficeEstateOffice, Unset):
            DistrictTenancyManagementOfficeEstateOffice = (
                self.DistrictTenancyManagementOfficeEstateOffice.to_dict()
            )

        District_Name = self.District_Name

        District_Tenancy_Management_Office_Estate_Office = (
            self.District_Tenancy_Management_Office_Estate_Office
        )

        EstateManagementAdvisoryCommitteeEMAC: dict[str, Any] | str | Unset
        if isinstance(self.EstateManagementAdvisoryCommitteeEMAC, Unset):
            EstateManagementAdvisoryCommitteeEMAC = UNSET
        elif isinstance(self.EstateManagementAdvisoryCommitteeEMAC, LocalizedText):
            EstateManagementAdvisoryCommitteeEMAC = (
                self.EstateManagementAdvisoryCommitteeEMAC.to_dict()
            )
        else:
            EstateManagementAdvisoryCommitteeEMAC = (
                self.EstateManagementAdvisoryCommitteeEMAC
            )

        estate_map_latitude = self.estate_map_latitude

        estate_map_longitude = self.estate_map_longitude

        EstateName: dict[str, Any] | Unset = UNSET
        if not isinstance(self.EstateName, Unset):
            EstateName = self.EstateName.to_dict()

        EstateWebsite = self.EstateWebsite

        Estate_Management_Advisory_Committee_EMAC = (
            self.Estate_Management_Advisory_Committee_EMAC
        )

        Estate_Name = self.Estate_Name

        Estate_Website = self.Estate_Website

        factory_estate_office: dict[str, Any] | Unset = UNSET
        if not isinstance(self.factory_estate_office, Unset):
            factory_estate_office = self.factory_estate_office.to_dict()

        FlatSizem2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.FlatSizem2, Unset):
            FlatSizem2 = self.FlatSizem2.to_dict()

        Flat_Size_m2 = self.Flat_Size_m2

        flatted_factories_website = self.flatted_factories_website

        FurtherInformation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.FurtherInformation, Unset):
            FurtherInformation = self.FurtherInformation.to_dict()

        Further_Information = self.Further_Information

        gross_floor_area_of_flat_m_2 = self.gross_floor_area_of_flat_m_2

        initial_sale_price = self.initial_sale_price

        name_of_blocks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name_of_blocks, Unset):
            name_of_blocks = self.name_of_blocks.to_dict()

        name_of_block = self.name_of_block

        NoofBlocks = self.NoofBlocks

        no_of_flats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.no_of_flats, Unset):
            no_of_flats = self.no_of_flats.to_dict()

        no_of_floors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.no_of_floors, Unset):
            no_of_floors = self.no_of_floors.to_dict()

        NoofRentalFlats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.NoofRentalFlats, Unset):
            NoofRentalFlats = self.NoofRentalFlats.to_dict()

        No_of_Blocks = self.No_of_Blocks

        No_of_Rental_Flats = self.No_of_Rental_Flats

        owners_corporation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.owners_corporation, Unset):
            owners_corporation = self.owners_corporation.to_dict()

        PropertyManagement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.PropertyManagement, Unset):
            PropertyManagement = self.PropertyManagement.to_dict()

        Property_Management = self.Property_Management

        RegionName: dict[str, Any] | Unset = UNSET
        if not isinstance(self.RegionName, Unset):
            RegionName = self.RegionName.to_dict()

        Region_Name = self.Region_Name

        regional_management_office_management_office_estate_office: (
            dict[str, Any] | Unset
        ) = UNSET
        if not isinstance(
            self.regional_management_office_management_office_estate_office, Unset
        ):
            regional_management_office_management_office_estate_office = self.regional_management_office_management_office_estate_office.to_dict()

        saleable_area_of_flats_m_2 = self.saleable_area_of_flats_m_2

        shopping_centre_website = self.shopping_centre_website

        sold_under: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sold_under, Unset):
            sold_under = self.sold_under.to_dict()

        storey: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storey, Unset):
            storey = self.storey.to_dict()

        total_lettable_area_m_2: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_lettable_area_m_2, Unset):
            total_lettable_area_m_2 = self.total_lettable_area_m_2.to_dict()

        TypeofEstate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.TypeofEstate, Unset):
            TypeofEstate = self.TypeofEstate.to_dict()

        types_of_blocks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.types_of_blocks, Unset):
            types_of_blocks = self.types_of_blocks.to_dict()

        type_of_block = self.type_of_block

        Type_of_Estate = self.Type_of_Estate

        year_of_completion: dict[str, Any] | Unset = UNSET
        if not isinstance(self.year_of_completion, Unset):
            year_of_completion = self.year_of_completion.to_dict()

        YearofIntake: dict[str, Any] | Unset = UNSET
        if not isinstance(self.YearofIntake, Unset):
            YearofIntake = self.YearofIntake.to_dict()

        Year_of_Intake = self.Year_of_Intake

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if CarparkManagement is not UNSET:
            field_dict["Carpark Management"] = CarparkManagement
        if Carpark_Management is not UNSET:
            field_dict["Carpark_Management"] = Carpark_Management
        if court_website is not UNSET:
            field_dict["Court Website"] = court_website
        if DistrictName is not UNSET:
            field_dict["District Name"] = DistrictName
        if DistrictTenancyManagementOfficeEstateOffice is not UNSET:
            field_dict["District Tenancy Management Office/Estate Office"] = (
                DistrictTenancyManagementOfficeEstateOffice
            )
        if District_Name is not UNSET:
            field_dict["District_Name"] = District_Name
        if District_Tenancy_Management_Office_Estate_Office is not UNSET:
            field_dict["District_Tenancy_Management_Office_Estate_Office"] = (
                District_Tenancy_Management_Office_Estate_Office
            )
        if EstateManagementAdvisoryCommitteeEMAC is not UNSET:
            field_dict["Estate Management Advisory Committee (EMAC)"] = (
                EstateManagementAdvisoryCommitteeEMAC
            )
        if estate_map_latitude is not UNSET:
            field_dict["Estate Map Latitude"] = estate_map_latitude
        if estate_map_longitude is not UNSET:
            field_dict["Estate Map Longitude"] = estate_map_longitude
        if EstateName is not UNSET:
            field_dict["Estate Name"] = EstateName
        if EstateWebsite is not UNSET:
            field_dict["Estate Website"] = EstateWebsite
        if Estate_Management_Advisory_Committee_EMAC is not UNSET:
            field_dict["Estate_Management_Advisory_Committee_EMAC"] = (
                Estate_Management_Advisory_Committee_EMAC
            )
        if Estate_Name is not UNSET:
            field_dict["Estate_Name"] = Estate_Name
        if Estate_Website is not UNSET:
            field_dict["Estate_Website"] = Estate_Website
        if factory_estate_office is not UNSET:
            field_dict["Factory Estate Office"] = factory_estate_office
        if FlatSizem2 is not UNSET:
            field_dict["Flat Size (m2)"] = FlatSizem2
        if Flat_Size_m2 is not UNSET:
            field_dict["Flat_Size_m2"] = Flat_Size_m2
        if flatted_factories_website is not UNSET:
            field_dict["Flatted Factories Website"] = flatted_factories_website
        if FurtherInformation is not UNSET:
            field_dict["Further Information"] = FurtherInformation
        if Further_Information is not UNSET:
            field_dict["Further_Information"] = Further_Information
        if gross_floor_area_of_flat_m_2 is not UNSET:
            field_dict["Gross Floor Area of Flat (m2)"] = gross_floor_area_of_flat_m_2
        if initial_sale_price is not UNSET:
            field_dict["Initial Sale Price($)"] = initial_sale_price
        if name_of_blocks is not UNSET:
            field_dict["Name of Block(s)"] = name_of_blocks
        if name_of_block is not UNSET:
            field_dict["Name_of_Block"] = name_of_block
        if NoofBlocks is not UNSET:
            field_dict["No. of Blocks"] = NoofBlocks
        if no_of_flats is not UNSET:
            field_dict["No. of Flats"] = no_of_flats
        if no_of_floors is not UNSET:
            field_dict["No. of Floor(s)"] = no_of_floors
        if NoofRentalFlats is not UNSET:
            field_dict["No. of Rental Flats"] = NoofRentalFlats
        if No_of_Blocks is not UNSET:
            field_dict["No_of_Blocks"] = No_of_Blocks
        if No_of_Rental_Flats is not UNSET:
            field_dict["No_of_Rental_Flats"] = No_of_Rental_Flats
        if owners_corporation is not UNSET:
            field_dict["Owners' Corporation"] = owners_corporation
        if PropertyManagement is not UNSET:
            field_dict["Property Management"] = PropertyManagement
        if Property_Management is not UNSET:
            field_dict["Property_Management"] = Property_Management
        if RegionName is not UNSET:
            field_dict["Region Name"] = RegionName
        if Region_Name is not UNSET:
            field_dict["Region_Name"] = Region_Name
        if regional_management_office_management_office_estate_office is not UNSET:
            field_dict[
                "Regional Management Office / Management Office / Estate Office"
            ] = regional_management_office_management_office_estate_office
        if saleable_area_of_flats_m_2 is not UNSET:
            field_dict["Saleable Area of Flats (m2)"] = saleable_area_of_flats_m_2
        if shopping_centre_website is not UNSET:
            field_dict["Shopping Centre Website"] = shopping_centre_website
        if sold_under is not UNSET:
            field_dict["Sold Under"] = sold_under
        if storey is not UNSET:
            field_dict["Storey"] = storey
        if total_lettable_area_m_2 is not UNSET:
            field_dict["Total Lettable Area (m2)"] = total_lettable_area_m_2
        if TypeofEstate is not UNSET:
            field_dict["Type of Estate"] = TypeofEstate
        if types_of_blocks is not UNSET:
            field_dict["Type(s) of Block(s)"] = types_of_blocks
        if type_of_block is not UNSET:
            field_dict["Type_of_Block"] = type_of_block
        if Type_of_Estate is not UNSET:
            field_dict["Type_of_Estate"] = Type_of_Estate
        if year_of_completion is not UNSET:
            field_dict["Year of Completion"] = year_of_completion
        if YearofIntake is not UNSET:
            field_dict["Year of Intake"] = YearofIntake
        if Year_of_Intake is not UNSET:
            field_dict["Year_of_Intake"] = Year_of_Intake

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.localized_text import LocalizedText

        d = dict(src_dict)
        _CarparkManagement = d.pop("Carpark Management", UNSET)
        CarparkManagement: LocalizedText | Unset
        if isinstance(_CarparkManagement, Unset):
            CarparkManagement = UNSET
        else:
            CarparkManagement = LocalizedText.from_dict(_CarparkManagement)

        Carpark_Management = d.pop("Carpark_Management", UNSET)

        court_website = d.pop("Court Website", UNSET)

        _DistrictName = d.pop("District Name", UNSET)
        DistrictName: LocalizedText | Unset
        if isinstance(_DistrictName, Unset):
            DistrictName = UNSET
        else:
            DistrictName = LocalizedText.from_dict(_DistrictName)

        _DistrictTenancyManagementOfficeEstateOffice = d.pop(
            "District Tenancy Management Office/Estate Office", UNSET
        )
        DistrictTenancyManagementOfficeEstateOffice: LocalizedText | Unset
        if isinstance(_DistrictTenancyManagementOfficeEstateOffice, Unset):
            DistrictTenancyManagementOfficeEstateOffice = UNSET
        else:
            DistrictTenancyManagementOfficeEstateOffice = LocalizedText.from_dict(
                _DistrictTenancyManagementOfficeEstateOffice
            )

        District_Name = d.pop("District_Name", UNSET)

        District_Tenancy_Management_Office_Estate_Office = d.pop(
            "District_Tenancy_Management_Office_Estate_Office", UNSET
        )

        def _parse_EstateManagementAdvisoryCommitteeEMAC(
            data: object,
        ) -> LocalizedText | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                estate_management_advisory_committee_emac_type_0 = (
                    LocalizedText.from_dict(data)
                )

                return estate_management_advisory_committee_emac_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LocalizedText | str | Unset, data)

        EstateManagementAdvisoryCommitteeEMAC = (
            _parse_EstateManagementAdvisoryCommitteeEMAC(
                d.pop("Estate Management Advisory Committee (EMAC)", UNSET)
            )
        )

        estate_map_latitude = d.pop("Estate Map Latitude", UNSET)

        estate_map_longitude = d.pop("Estate Map Longitude", UNSET)

        _EstateName = d.pop("Estate Name", UNSET)
        EstateName: LocalizedText | Unset
        if isinstance(_EstateName, Unset):
            EstateName = UNSET
        else:
            EstateName = LocalizedText.from_dict(_EstateName)

        EstateWebsite = d.pop("Estate Website", UNSET)

        Estate_Management_Advisory_Committee_EMAC = d.pop(
            "Estate_Management_Advisory_Committee_EMAC", UNSET
        )

        Estate_Name = d.pop("Estate_Name", UNSET)

        Estate_Website = d.pop("Estate_Website", UNSET)

        _factory_estate_office = d.pop("Factory Estate Office", UNSET)
        factory_estate_office: LocalizedText | Unset
        if isinstance(_factory_estate_office, Unset):
            factory_estate_office = UNSET
        else:
            factory_estate_office = LocalizedText.from_dict(_factory_estate_office)

        _FlatSizem2 = d.pop("Flat Size (m2)", UNSET)
        FlatSizem2: LocalizedText | Unset
        if isinstance(_FlatSizem2, Unset):
            FlatSizem2 = UNSET
        else:
            FlatSizem2 = LocalizedText.from_dict(_FlatSizem2)

        Flat_Size_m2 = d.pop("Flat_Size_m2", UNSET)

        flatted_factories_website = d.pop("Flatted Factories Website", UNSET)

        _FurtherInformation = d.pop("Further Information", UNSET)
        FurtherInformation: LocalizedText | Unset
        if isinstance(_FurtherInformation, Unset):
            FurtherInformation = UNSET
        else:
            FurtherInformation = LocalizedText.from_dict(_FurtherInformation)

        Further_Information = d.pop("Further_Information", UNSET)

        gross_floor_area_of_flat_m_2 = d.pop("Gross Floor Area of Flat (m2)", UNSET)

        initial_sale_price = d.pop("Initial Sale Price($)", UNSET)

        _name_of_blocks = d.pop("Name of Block(s)", UNSET)
        name_of_blocks: LocalizedText | Unset
        if isinstance(_name_of_blocks, Unset):
            name_of_blocks = UNSET
        else:
            name_of_blocks = LocalizedText.from_dict(_name_of_blocks)

        name_of_block = d.pop("Name_of_Block", UNSET)

        NoofBlocks = d.pop("No. of Blocks", UNSET)

        _no_of_flats = d.pop("No. of Flats", UNSET)
        no_of_flats: LocalizedText | Unset
        if isinstance(_no_of_flats, Unset):
            no_of_flats = UNSET
        else:
            no_of_flats = LocalizedText.from_dict(_no_of_flats)

        _no_of_floors = d.pop("No. of Floor(s)", UNSET)
        no_of_floors: LocalizedText | Unset
        if isinstance(_no_of_floors, Unset):
            no_of_floors = UNSET
        else:
            no_of_floors = LocalizedText.from_dict(_no_of_floors)

        _NoofRentalFlats = d.pop("No. of Rental Flats", UNSET)
        NoofRentalFlats: LocalizedText | Unset
        if isinstance(_NoofRentalFlats, Unset):
            NoofRentalFlats = UNSET
        else:
            NoofRentalFlats = LocalizedText.from_dict(_NoofRentalFlats)

        No_of_Blocks = d.pop("No_of_Blocks", UNSET)

        No_of_Rental_Flats = d.pop("No_of_Rental_Flats", UNSET)

        _owners_corporation = d.pop("Owners' Corporation", UNSET)
        owners_corporation: LocalizedText | Unset
        if isinstance(_owners_corporation, Unset):
            owners_corporation = UNSET
        else:
            owners_corporation = LocalizedText.from_dict(_owners_corporation)

        _PropertyManagement = d.pop("Property Management", UNSET)
        PropertyManagement: LocalizedText | Unset
        if isinstance(_PropertyManagement, Unset):
            PropertyManagement = UNSET
        else:
            PropertyManagement = LocalizedText.from_dict(_PropertyManagement)

        Property_Management = d.pop("Property_Management", UNSET)

        _RegionName = d.pop("Region Name", UNSET)
        RegionName: LocalizedText | Unset
        if isinstance(_RegionName, Unset):
            RegionName = UNSET
        else:
            RegionName = LocalizedText.from_dict(_RegionName)

        Region_Name = d.pop("Region_Name", UNSET)

        _regional_management_office_management_office_estate_office = d.pop(
            "Regional Management Office / Management Office / Estate Office", UNSET
        )
        regional_management_office_management_office_estate_office: (
            LocalizedText | Unset
        )
        if isinstance(
            _regional_management_office_management_office_estate_office, Unset
        ):
            regional_management_office_management_office_estate_office = UNSET
        else:
            regional_management_office_management_office_estate_office = (
                LocalizedText.from_dict(
                    _regional_management_office_management_office_estate_office
                )
            )

        saleable_area_of_flats_m_2 = d.pop("Saleable Area of Flats (m2)", UNSET)

        shopping_centre_website = d.pop("Shopping Centre Website", UNSET)

        _sold_under = d.pop("Sold Under", UNSET)
        sold_under: LocalizedText | Unset
        if isinstance(_sold_under, Unset):
            sold_under = UNSET
        else:
            sold_under = LocalizedText.from_dict(_sold_under)

        _storey = d.pop("Storey", UNSET)
        storey: LocalizedText | Unset
        if isinstance(_storey, Unset):
            storey = UNSET
        else:
            storey = LocalizedText.from_dict(_storey)

        _total_lettable_area_m_2 = d.pop("Total Lettable Area (m2)", UNSET)
        total_lettable_area_m_2: LocalizedText | Unset
        if isinstance(_total_lettable_area_m_2, Unset):
            total_lettable_area_m_2 = UNSET
        else:
            total_lettable_area_m_2 = LocalizedText.from_dict(_total_lettable_area_m_2)

        _TypeofEstate = d.pop("Type of Estate", UNSET)
        TypeofEstate: LocalizedText | Unset
        if isinstance(_TypeofEstate, Unset):
            TypeofEstate = UNSET
        else:
            TypeofEstate = LocalizedText.from_dict(_TypeofEstate)

        _types_of_blocks = d.pop("Type(s) of Block(s)", UNSET)
        types_of_blocks: LocalizedText | Unset
        if isinstance(_types_of_blocks, Unset):
            types_of_blocks = UNSET
        else:
            types_of_blocks = LocalizedText.from_dict(_types_of_blocks)

        type_of_block = d.pop("Type_of_Block", UNSET)

        Type_of_Estate = d.pop("Type_of_Estate", UNSET)

        _year_of_completion = d.pop("Year of Completion", UNSET)
        year_of_completion: LocalizedText | Unset
        if isinstance(_year_of_completion, Unset):
            year_of_completion = UNSET
        else:
            year_of_completion = LocalizedText.from_dict(_year_of_completion)

        _YearofIntake = d.pop("Year of Intake", UNSET)
        YearofIntake: LocalizedText | Unset
        if isinstance(_YearofIntake, Unset):
            YearofIntake = UNSET
        else:
            YearofIntake = LocalizedText.from_dict(_YearofIntake)

        Year_of_Intake = d.pop("Year_of_Intake", UNSET)

        location_profile_record = cls(
            CarparkManagement=CarparkManagement,
            Carpark_Management=Carpark_Management,
            court_website=court_website,
            DistrictName=DistrictName,
            DistrictTenancyManagementOfficeEstateOffice=DistrictTenancyManagementOfficeEstateOffice,
            District_Name=District_Name,
            District_Tenancy_Management_Office_Estate_Office=District_Tenancy_Management_Office_Estate_Office,
            EstateManagementAdvisoryCommitteeEMAC=EstateManagementAdvisoryCommitteeEMAC,
            estate_map_latitude=estate_map_latitude,
            estate_map_longitude=estate_map_longitude,
            EstateName=EstateName,
            EstateWebsite=EstateWebsite,
            Estate_Management_Advisory_Committee_EMAC=Estate_Management_Advisory_Committee_EMAC,
            Estate_Name=Estate_Name,
            Estate_Website=Estate_Website,
            factory_estate_office=factory_estate_office,
            FlatSizem2=FlatSizem2,
            Flat_Size_m2=Flat_Size_m2,
            flatted_factories_website=flatted_factories_website,
            FurtherInformation=FurtherInformation,
            Further_Information=Further_Information,
            gross_floor_area_of_flat_m_2=gross_floor_area_of_flat_m_2,
            initial_sale_price=initial_sale_price,
            name_of_blocks=name_of_blocks,
            name_of_block=name_of_block,
            NoofBlocks=NoofBlocks,
            no_of_flats=no_of_flats,
            no_of_floors=no_of_floors,
            NoofRentalFlats=NoofRentalFlats,
            No_of_Blocks=No_of_Blocks,
            No_of_Rental_Flats=No_of_Rental_Flats,
            owners_corporation=owners_corporation,
            PropertyManagement=PropertyManagement,
            Property_Management=Property_Management,
            RegionName=RegionName,
            Region_Name=Region_Name,
            regional_management_office_management_office_estate_office=regional_management_office_management_office_estate_office,
            saleable_area_of_flats_m_2=saleable_area_of_flats_m_2,
            shopping_centre_website=shopping_centre_website,
            sold_under=sold_under,
            storey=storey,
            total_lettable_area_m_2=total_lettable_area_m_2,
            TypeofEstate=TypeofEstate,
            types_of_blocks=types_of_blocks,
            type_of_block=type_of_block,
            Type_of_Estate=Type_of_Estate,
            year_of_completion=year_of_completion,
            YearofIntake=YearofIntake,
            Year_of_Intake=Year_of_Intake,
        )

        location_profile_record.additional_properties = d
        return location_profile_record

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
