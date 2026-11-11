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
        age_group (None | str | Unset): Publisher field type: esriFieldTypeString
        district (None | str | Unset): Publisher field type: esriFieldTypeString
        fid (float | None | Unset): Publisher field type: esriFieldTypeDouble
        percentage_of_statistics_of_1986 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_1987 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_1988 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_1989 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_1990 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_1991 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_1992 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_1993 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_1994 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_1995 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_1996 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_1997 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_1998 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_1999 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2000 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2001 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2002 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2003 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2004 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2005 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2006 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2007 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2008 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2009 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2010 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2011 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2012 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2013 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2014 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2015 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2016 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2017 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2018 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2019 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2020 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2021 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2022 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2023 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2024 (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_of_statistics_of_2025 (None | str | Unset): Publisher field type: esriFieldTypeString
        res_district (None | str | Unset): Publisher field type: esriFieldTypeString
        sex (None | str | Unset): Publisher field type: esriFieldTypeString
        type_of_reported_drug_abusers (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_1986 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_1987 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_1988 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_1989 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_1990 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_1991 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_1992 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_1993 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_1994 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_1995 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_1996 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_1997 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_1998 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_1999 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2000 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2001 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2002 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2003 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2004 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2005 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2006 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2007 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2008 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2009 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2010 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2011 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2012 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2013 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2014 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2015 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2016 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2017 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2018 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2019 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2020 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2021 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2022 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2023 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2024 (None | str | Unset): Publisher field type: esriFieldTypeString
        value_of_statistics_of_2025 (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    age_group: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    fid: float | None | Unset = UNSET
    percentage_of_statistics_of_1986: None | str | Unset = UNSET
    percentage_of_statistics_of_1987: None | str | Unset = UNSET
    percentage_of_statistics_of_1988: None | str | Unset = UNSET
    percentage_of_statistics_of_1989: None | str | Unset = UNSET
    percentage_of_statistics_of_1990: None | str | Unset = UNSET
    percentage_of_statistics_of_1991: None | str | Unset = UNSET
    percentage_of_statistics_of_1992: None | str | Unset = UNSET
    percentage_of_statistics_of_1993: None | str | Unset = UNSET
    percentage_of_statistics_of_1994: None | str | Unset = UNSET
    percentage_of_statistics_of_1995: None | str | Unset = UNSET
    percentage_of_statistics_of_1996: None | str | Unset = UNSET
    percentage_of_statistics_of_1997: None | str | Unset = UNSET
    percentage_of_statistics_of_1998: None | str | Unset = UNSET
    percentage_of_statistics_of_1999: None | str | Unset = UNSET
    percentage_of_statistics_of_2000: None | str | Unset = UNSET
    percentage_of_statistics_of_2001: None | str | Unset = UNSET
    percentage_of_statistics_of_2002: None | str | Unset = UNSET
    percentage_of_statistics_of_2003: None | str | Unset = UNSET
    percentage_of_statistics_of_2004: None | str | Unset = UNSET
    percentage_of_statistics_of_2005: None | str | Unset = UNSET
    percentage_of_statistics_of_2006: None | str | Unset = UNSET
    percentage_of_statistics_of_2007: None | str | Unset = UNSET
    percentage_of_statistics_of_2008: None | str | Unset = UNSET
    percentage_of_statistics_of_2009: None | str | Unset = UNSET
    percentage_of_statistics_of_2010: None | str | Unset = UNSET
    percentage_of_statistics_of_2011: None | str | Unset = UNSET
    percentage_of_statistics_of_2012: None | str | Unset = UNSET
    percentage_of_statistics_of_2013: None | str | Unset = UNSET
    percentage_of_statistics_of_2014: None | str | Unset = UNSET
    percentage_of_statistics_of_2015: None | str | Unset = UNSET
    percentage_of_statistics_of_2016: None | str | Unset = UNSET
    percentage_of_statistics_of_2017: None | str | Unset = UNSET
    percentage_of_statistics_of_2018: None | str | Unset = UNSET
    percentage_of_statistics_of_2019: None | str | Unset = UNSET
    percentage_of_statistics_of_2020: None | str | Unset = UNSET
    percentage_of_statistics_of_2021: None | str | Unset = UNSET
    percentage_of_statistics_of_2022: None | str | Unset = UNSET
    percentage_of_statistics_of_2023: None | str | Unset = UNSET
    percentage_of_statistics_of_2024: None | str | Unset = UNSET
    percentage_of_statistics_of_2025: None | str | Unset = UNSET
    res_district: None | str | Unset = UNSET
    sex: None | str | Unset = UNSET
    type_of_reported_drug_abusers: None | str | Unset = UNSET
    value_of_statistics_of_1986: None | str | Unset = UNSET
    value_of_statistics_of_1987: None | str | Unset = UNSET
    value_of_statistics_of_1988: None | str | Unset = UNSET
    value_of_statistics_of_1989: None | str | Unset = UNSET
    value_of_statistics_of_1990: None | str | Unset = UNSET
    value_of_statistics_of_1991: None | str | Unset = UNSET
    value_of_statistics_of_1992: None | str | Unset = UNSET
    value_of_statistics_of_1993: None | str | Unset = UNSET
    value_of_statistics_of_1994: None | str | Unset = UNSET
    value_of_statistics_of_1995: None | str | Unset = UNSET
    value_of_statistics_of_1996: None | str | Unset = UNSET
    value_of_statistics_of_1997: None | str | Unset = UNSET
    value_of_statistics_of_1998: None | str | Unset = UNSET
    value_of_statistics_of_1999: None | str | Unset = UNSET
    value_of_statistics_of_2000: None | str | Unset = UNSET
    value_of_statistics_of_2001: None | str | Unset = UNSET
    value_of_statistics_of_2002: None | str | Unset = UNSET
    value_of_statistics_of_2003: None | str | Unset = UNSET
    value_of_statistics_of_2004: None | str | Unset = UNSET
    value_of_statistics_of_2005: None | str | Unset = UNSET
    value_of_statistics_of_2006: None | str | Unset = UNSET
    value_of_statistics_of_2007: None | str | Unset = UNSET
    value_of_statistics_of_2008: None | str | Unset = UNSET
    value_of_statistics_of_2009: None | str | Unset = UNSET
    value_of_statistics_of_2010: None | str | Unset = UNSET
    value_of_statistics_of_2011: None | str | Unset = UNSET
    value_of_statistics_of_2012: None | str | Unset = UNSET
    value_of_statistics_of_2013: None | str | Unset = UNSET
    value_of_statistics_of_2014: None | str | Unset = UNSET
    value_of_statistics_of_2015: None | str | Unset = UNSET
    value_of_statistics_of_2016: None | str | Unset = UNSET
    value_of_statistics_of_2017: None | str | Unset = UNSET
    value_of_statistics_of_2018: None | str | Unset = UNSET
    value_of_statistics_of_2019: None | str | Unset = UNSET
    value_of_statistics_of_2020: None | str | Unset = UNSET
    value_of_statistics_of_2021: None | str | Unset = UNSET
    value_of_statistics_of_2022: None | str | Unset = UNSET
    value_of_statistics_of_2023: None | str | Unset = UNSET
    value_of_statistics_of_2024: None | str | Unset = UNSET
    value_of_statistics_of_2025: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        age_group: None | str | Unset
        if isinstance(self.age_group, Unset):
            age_group = UNSET
        else:
            age_group = self.age_group

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        fid: float | None | Unset
        if isinstance(self.fid, Unset):
            fid = UNSET
        else:
            fid = self.fid

        percentage_of_statistics_of_1986: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_1986, Unset):
            percentage_of_statistics_of_1986 = UNSET
        else:
            percentage_of_statistics_of_1986 = self.percentage_of_statistics_of_1986

        percentage_of_statistics_of_1987: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_1987, Unset):
            percentage_of_statistics_of_1987 = UNSET
        else:
            percentage_of_statistics_of_1987 = self.percentage_of_statistics_of_1987

        percentage_of_statistics_of_1988: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_1988, Unset):
            percentage_of_statistics_of_1988 = UNSET
        else:
            percentage_of_statistics_of_1988 = self.percentage_of_statistics_of_1988

        percentage_of_statistics_of_1989: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_1989, Unset):
            percentage_of_statistics_of_1989 = UNSET
        else:
            percentage_of_statistics_of_1989 = self.percentage_of_statistics_of_1989

        percentage_of_statistics_of_1990: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_1990, Unset):
            percentage_of_statistics_of_1990 = UNSET
        else:
            percentage_of_statistics_of_1990 = self.percentage_of_statistics_of_1990

        percentage_of_statistics_of_1991: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_1991, Unset):
            percentage_of_statistics_of_1991 = UNSET
        else:
            percentage_of_statistics_of_1991 = self.percentage_of_statistics_of_1991

        percentage_of_statistics_of_1992: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_1992, Unset):
            percentage_of_statistics_of_1992 = UNSET
        else:
            percentage_of_statistics_of_1992 = self.percentage_of_statistics_of_1992

        percentage_of_statistics_of_1993: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_1993, Unset):
            percentage_of_statistics_of_1993 = UNSET
        else:
            percentage_of_statistics_of_1993 = self.percentage_of_statistics_of_1993

        percentage_of_statistics_of_1994: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_1994, Unset):
            percentage_of_statistics_of_1994 = UNSET
        else:
            percentage_of_statistics_of_1994 = self.percentage_of_statistics_of_1994

        percentage_of_statistics_of_1995: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_1995, Unset):
            percentage_of_statistics_of_1995 = UNSET
        else:
            percentage_of_statistics_of_1995 = self.percentage_of_statistics_of_1995

        percentage_of_statistics_of_1996: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_1996, Unset):
            percentage_of_statistics_of_1996 = UNSET
        else:
            percentage_of_statistics_of_1996 = self.percentage_of_statistics_of_1996

        percentage_of_statistics_of_1997: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_1997, Unset):
            percentage_of_statistics_of_1997 = UNSET
        else:
            percentage_of_statistics_of_1997 = self.percentage_of_statistics_of_1997

        percentage_of_statistics_of_1998: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_1998, Unset):
            percentage_of_statistics_of_1998 = UNSET
        else:
            percentage_of_statistics_of_1998 = self.percentage_of_statistics_of_1998

        percentage_of_statistics_of_1999: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_1999, Unset):
            percentage_of_statistics_of_1999 = UNSET
        else:
            percentage_of_statistics_of_1999 = self.percentage_of_statistics_of_1999

        percentage_of_statistics_of_2000: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2000, Unset):
            percentage_of_statistics_of_2000 = UNSET
        else:
            percentage_of_statistics_of_2000 = self.percentage_of_statistics_of_2000

        percentage_of_statistics_of_2001: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2001, Unset):
            percentage_of_statistics_of_2001 = UNSET
        else:
            percentage_of_statistics_of_2001 = self.percentage_of_statistics_of_2001

        percentage_of_statistics_of_2002: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2002, Unset):
            percentage_of_statistics_of_2002 = UNSET
        else:
            percentage_of_statistics_of_2002 = self.percentage_of_statistics_of_2002

        percentage_of_statistics_of_2003: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2003, Unset):
            percentage_of_statistics_of_2003 = UNSET
        else:
            percentage_of_statistics_of_2003 = self.percentage_of_statistics_of_2003

        percentage_of_statistics_of_2004: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2004, Unset):
            percentage_of_statistics_of_2004 = UNSET
        else:
            percentage_of_statistics_of_2004 = self.percentage_of_statistics_of_2004

        percentage_of_statistics_of_2005: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2005, Unset):
            percentage_of_statistics_of_2005 = UNSET
        else:
            percentage_of_statistics_of_2005 = self.percentage_of_statistics_of_2005

        percentage_of_statistics_of_2006: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2006, Unset):
            percentage_of_statistics_of_2006 = UNSET
        else:
            percentage_of_statistics_of_2006 = self.percentage_of_statistics_of_2006

        percentage_of_statistics_of_2007: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2007, Unset):
            percentage_of_statistics_of_2007 = UNSET
        else:
            percentage_of_statistics_of_2007 = self.percentage_of_statistics_of_2007

        percentage_of_statistics_of_2008: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2008, Unset):
            percentage_of_statistics_of_2008 = UNSET
        else:
            percentage_of_statistics_of_2008 = self.percentage_of_statistics_of_2008

        percentage_of_statistics_of_2009: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2009, Unset):
            percentage_of_statistics_of_2009 = UNSET
        else:
            percentage_of_statistics_of_2009 = self.percentage_of_statistics_of_2009

        percentage_of_statistics_of_2010: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2010, Unset):
            percentage_of_statistics_of_2010 = UNSET
        else:
            percentage_of_statistics_of_2010 = self.percentage_of_statistics_of_2010

        percentage_of_statistics_of_2011: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2011, Unset):
            percentage_of_statistics_of_2011 = UNSET
        else:
            percentage_of_statistics_of_2011 = self.percentage_of_statistics_of_2011

        percentage_of_statistics_of_2012: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2012, Unset):
            percentage_of_statistics_of_2012 = UNSET
        else:
            percentage_of_statistics_of_2012 = self.percentage_of_statistics_of_2012

        percentage_of_statistics_of_2013: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2013, Unset):
            percentage_of_statistics_of_2013 = UNSET
        else:
            percentage_of_statistics_of_2013 = self.percentage_of_statistics_of_2013

        percentage_of_statistics_of_2014: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2014, Unset):
            percentage_of_statistics_of_2014 = UNSET
        else:
            percentage_of_statistics_of_2014 = self.percentage_of_statistics_of_2014

        percentage_of_statistics_of_2015: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2015, Unset):
            percentage_of_statistics_of_2015 = UNSET
        else:
            percentage_of_statistics_of_2015 = self.percentage_of_statistics_of_2015

        percentage_of_statistics_of_2016: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2016, Unset):
            percentage_of_statistics_of_2016 = UNSET
        else:
            percentage_of_statistics_of_2016 = self.percentage_of_statistics_of_2016

        percentage_of_statistics_of_2017: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2017, Unset):
            percentage_of_statistics_of_2017 = UNSET
        else:
            percentage_of_statistics_of_2017 = self.percentage_of_statistics_of_2017

        percentage_of_statistics_of_2018: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2018, Unset):
            percentage_of_statistics_of_2018 = UNSET
        else:
            percentage_of_statistics_of_2018 = self.percentage_of_statistics_of_2018

        percentage_of_statistics_of_2019: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2019, Unset):
            percentage_of_statistics_of_2019 = UNSET
        else:
            percentage_of_statistics_of_2019 = self.percentage_of_statistics_of_2019

        percentage_of_statistics_of_2020: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2020, Unset):
            percentage_of_statistics_of_2020 = UNSET
        else:
            percentage_of_statistics_of_2020 = self.percentage_of_statistics_of_2020

        percentage_of_statistics_of_2021: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2021, Unset):
            percentage_of_statistics_of_2021 = UNSET
        else:
            percentage_of_statistics_of_2021 = self.percentage_of_statistics_of_2021

        percentage_of_statistics_of_2022: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2022, Unset):
            percentage_of_statistics_of_2022 = UNSET
        else:
            percentage_of_statistics_of_2022 = self.percentage_of_statistics_of_2022

        percentage_of_statistics_of_2023: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2023, Unset):
            percentage_of_statistics_of_2023 = UNSET
        else:
            percentage_of_statistics_of_2023 = self.percentage_of_statistics_of_2023

        percentage_of_statistics_of_2024: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2024, Unset):
            percentage_of_statistics_of_2024 = UNSET
        else:
            percentage_of_statistics_of_2024 = self.percentage_of_statistics_of_2024

        percentage_of_statistics_of_2025: None | str | Unset
        if isinstance(self.percentage_of_statistics_of_2025, Unset):
            percentage_of_statistics_of_2025 = UNSET
        else:
            percentage_of_statistics_of_2025 = self.percentage_of_statistics_of_2025

        res_district: None | str | Unset
        if isinstance(self.res_district, Unset):
            res_district = UNSET
        else:
            res_district = self.res_district

        sex: None | str | Unset
        if isinstance(self.sex, Unset):
            sex = UNSET
        else:
            sex = self.sex

        type_of_reported_drug_abusers: None | str | Unset
        if isinstance(self.type_of_reported_drug_abusers, Unset):
            type_of_reported_drug_abusers = UNSET
        else:
            type_of_reported_drug_abusers = self.type_of_reported_drug_abusers

        value_of_statistics_of_1986: None | str | Unset
        if isinstance(self.value_of_statistics_of_1986, Unset):
            value_of_statistics_of_1986 = UNSET
        else:
            value_of_statistics_of_1986 = self.value_of_statistics_of_1986

        value_of_statistics_of_1987: None | str | Unset
        if isinstance(self.value_of_statistics_of_1987, Unset):
            value_of_statistics_of_1987 = UNSET
        else:
            value_of_statistics_of_1987 = self.value_of_statistics_of_1987

        value_of_statistics_of_1988: None | str | Unset
        if isinstance(self.value_of_statistics_of_1988, Unset):
            value_of_statistics_of_1988 = UNSET
        else:
            value_of_statistics_of_1988 = self.value_of_statistics_of_1988

        value_of_statistics_of_1989: None | str | Unset
        if isinstance(self.value_of_statistics_of_1989, Unset):
            value_of_statistics_of_1989 = UNSET
        else:
            value_of_statistics_of_1989 = self.value_of_statistics_of_1989

        value_of_statistics_of_1990: None | str | Unset
        if isinstance(self.value_of_statistics_of_1990, Unset):
            value_of_statistics_of_1990 = UNSET
        else:
            value_of_statistics_of_1990 = self.value_of_statistics_of_1990

        value_of_statistics_of_1991: None | str | Unset
        if isinstance(self.value_of_statistics_of_1991, Unset):
            value_of_statistics_of_1991 = UNSET
        else:
            value_of_statistics_of_1991 = self.value_of_statistics_of_1991

        value_of_statistics_of_1992: None | str | Unset
        if isinstance(self.value_of_statistics_of_1992, Unset):
            value_of_statistics_of_1992 = UNSET
        else:
            value_of_statistics_of_1992 = self.value_of_statistics_of_1992

        value_of_statistics_of_1993: None | str | Unset
        if isinstance(self.value_of_statistics_of_1993, Unset):
            value_of_statistics_of_1993 = UNSET
        else:
            value_of_statistics_of_1993 = self.value_of_statistics_of_1993

        value_of_statistics_of_1994: None | str | Unset
        if isinstance(self.value_of_statistics_of_1994, Unset):
            value_of_statistics_of_1994 = UNSET
        else:
            value_of_statistics_of_1994 = self.value_of_statistics_of_1994

        value_of_statistics_of_1995: None | str | Unset
        if isinstance(self.value_of_statistics_of_1995, Unset):
            value_of_statistics_of_1995 = UNSET
        else:
            value_of_statistics_of_1995 = self.value_of_statistics_of_1995

        value_of_statistics_of_1996: None | str | Unset
        if isinstance(self.value_of_statistics_of_1996, Unset):
            value_of_statistics_of_1996 = UNSET
        else:
            value_of_statistics_of_1996 = self.value_of_statistics_of_1996

        value_of_statistics_of_1997: None | str | Unset
        if isinstance(self.value_of_statistics_of_1997, Unset):
            value_of_statistics_of_1997 = UNSET
        else:
            value_of_statistics_of_1997 = self.value_of_statistics_of_1997

        value_of_statistics_of_1998: None | str | Unset
        if isinstance(self.value_of_statistics_of_1998, Unset):
            value_of_statistics_of_1998 = UNSET
        else:
            value_of_statistics_of_1998 = self.value_of_statistics_of_1998

        value_of_statistics_of_1999: None | str | Unset
        if isinstance(self.value_of_statistics_of_1999, Unset):
            value_of_statistics_of_1999 = UNSET
        else:
            value_of_statistics_of_1999 = self.value_of_statistics_of_1999

        value_of_statistics_of_2000: None | str | Unset
        if isinstance(self.value_of_statistics_of_2000, Unset):
            value_of_statistics_of_2000 = UNSET
        else:
            value_of_statistics_of_2000 = self.value_of_statistics_of_2000

        value_of_statistics_of_2001: None | str | Unset
        if isinstance(self.value_of_statistics_of_2001, Unset):
            value_of_statistics_of_2001 = UNSET
        else:
            value_of_statistics_of_2001 = self.value_of_statistics_of_2001

        value_of_statistics_of_2002: None | str | Unset
        if isinstance(self.value_of_statistics_of_2002, Unset):
            value_of_statistics_of_2002 = UNSET
        else:
            value_of_statistics_of_2002 = self.value_of_statistics_of_2002

        value_of_statistics_of_2003: None | str | Unset
        if isinstance(self.value_of_statistics_of_2003, Unset):
            value_of_statistics_of_2003 = UNSET
        else:
            value_of_statistics_of_2003 = self.value_of_statistics_of_2003

        value_of_statistics_of_2004: None | str | Unset
        if isinstance(self.value_of_statistics_of_2004, Unset):
            value_of_statistics_of_2004 = UNSET
        else:
            value_of_statistics_of_2004 = self.value_of_statistics_of_2004

        value_of_statistics_of_2005: None | str | Unset
        if isinstance(self.value_of_statistics_of_2005, Unset):
            value_of_statistics_of_2005 = UNSET
        else:
            value_of_statistics_of_2005 = self.value_of_statistics_of_2005

        value_of_statistics_of_2006: None | str | Unset
        if isinstance(self.value_of_statistics_of_2006, Unset):
            value_of_statistics_of_2006 = UNSET
        else:
            value_of_statistics_of_2006 = self.value_of_statistics_of_2006

        value_of_statistics_of_2007: None | str | Unset
        if isinstance(self.value_of_statistics_of_2007, Unset):
            value_of_statistics_of_2007 = UNSET
        else:
            value_of_statistics_of_2007 = self.value_of_statistics_of_2007

        value_of_statistics_of_2008: None | str | Unset
        if isinstance(self.value_of_statistics_of_2008, Unset):
            value_of_statistics_of_2008 = UNSET
        else:
            value_of_statistics_of_2008 = self.value_of_statistics_of_2008

        value_of_statistics_of_2009: None | str | Unset
        if isinstance(self.value_of_statistics_of_2009, Unset):
            value_of_statistics_of_2009 = UNSET
        else:
            value_of_statistics_of_2009 = self.value_of_statistics_of_2009

        value_of_statistics_of_2010: None | str | Unset
        if isinstance(self.value_of_statistics_of_2010, Unset):
            value_of_statistics_of_2010 = UNSET
        else:
            value_of_statistics_of_2010 = self.value_of_statistics_of_2010

        value_of_statistics_of_2011: None | str | Unset
        if isinstance(self.value_of_statistics_of_2011, Unset):
            value_of_statistics_of_2011 = UNSET
        else:
            value_of_statistics_of_2011 = self.value_of_statistics_of_2011

        value_of_statistics_of_2012: None | str | Unset
        if isinstance(self.value_of_statistics_of_2012, Unset):
            value_of_statistics_of_2012 = UNSET
        else:
            value_of_statistics_of_2012 = self.value_of_statistics_of_2012

        value_of_statistics_of_2013: None | str | Unset
        if isinstance(self.value_of_statistics_of_2013, Unset):
            value_of_statistics_of_2013 = UNSET
        else:
            value_of_statistics_of_2013 = self.value_of_statistics_of_2013

        value_of_statistics_of_2014: None | str | Unset
        if isinstance(self.value_of_statistics_of_2014, Unset):
            value_of_statistics_of_2014 = UNSET
        else:
            value_of_statistics_of_2014 = self.value_of_statistics_of_2014

        value_of_statistics_of_2015: None | str | Unset
        if isinstance(self.value_of_statistics_of_2015, Unset):
            value_of_statistics_of_2015 = UNSET
        else:
            value_of_statistics_of_2015 = self.value_of_statistics_of_2015

        value_of_statistics_of_2016: None | str | Unset
        if isinstance(self.value_of_statistics_of_2016, Unset):
            value_of_statistics_of_2016 = UNSET
        else:
            value_of_statistics_of_2016 = self.value_of_statistics_of_2016

        value_of_statistics_of_2017: None | str | Unset
        if isinstance(self.value_of_statistics_of_2017, Unset):
            value_of_statistics_of_2017 = UNSET
        else:
            value_of_statistics_of_2017 = self.value_of_statistics_of_2017

        value_of_statistics_of_2018: None | str | Unset
        if isinstance(self.value_of_statistics_of_2018, Unset):
            value_of_statistics_of_2018 = UNSET
        else:
            value_of_statistics_of_2018 = self.value_of_statistics_of_2018

        value_of_statistics_of_2019: None | str | Unset
        if isinstance(self.value_of_statistics_of_2019, Unset):
            value_of_statistics_of_2019 = UNSET
        else:
            value_of_statistics_of_2019 = self.value_of_statistics_of_2019

        value_of_statistics_of_2020: None | str | Unset
        if isinstance(self.value_of_statistics_of_2020, Unset):
            value_of_statistics_of_2020 = UNSET
        else:
            value_of_statistics_of_2020 = self.value_of_statistics_of_2020

        value_of_statistics_of_2021: None | str | Unset
        if isinstance(self.value_of_statistics_of_2021, Unset):
            value_of_statistics_of_2021 = UNSET
        else:
            value_of_statistics_of_2021 = self.value_of_statistics_of_2021

        value_of_statistics_of_2022: None | str | Unset
        if isinstance(self.value_of_statistics_of_2022, Unset):
            value_of_statistics_of_2022 = UNSET
        else:
            value_of_statistics_of_2022 = self.value_of_statistics_of_2022

        value_of_statistics_of_2023: None | str | Unset
        if isinstance(self.value_of_statistics_of_2023, Unset):
            value_of_statistics_of_2023 = UNSET
        else:
            value_of_statistics_of_2023 = self.value_of_statistics_of_2023

        value_of_statistics_of_2024: None | str | Unset
        if isinstance(self.value_of_statistics_of_2024, Unset):
            value_of_statistics_of_2024 = UNSET
        else:
            value_of_statistics_of_2024 = self.value_of_statistics_of_2024

        value_of_statistics_of_2025: None | str | Unset
        if isinstance(self.value_of_statistics_of_2025, Unset):
            value_of_statistics_of_2025 = UNSET
        else:
            value_of_statistics_of_2025 = self.value_of_statistics_of_2025

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
        if age_group is not UNSET:
            field_dict["age_group"] = age_group
        if district is not UNSET:
            field_dict["district"] = district
        if fid is not UNSET:
            field_dict["fid"] = fid
        if percentage_of_statistics_of_1986 is not UNSET:
            field_dict["percentage_of_statistics_of_1986"] = (
                percentage_of_statistics_of_1986
            )
        if percentage_of_statistics_of_1987 is not UNSET:
            field_dict["percentage_of_statistics_of_1987"] = (
                percentage_of_statistics_of_1987
            )
        if percentage_of_statistics_of_1988 is not UNSET:
            field_dict["percentage_of_statistics_of_1988"] = (
                percentage_of_statistics_of_1988
            )
        if percentage_of_statistics_of_1989 is not UNSET:
            field_dict["percentage_of_statistics_of_1989"] = (
                percentage_of_statistics_of_1989
            )
        if percentage_of_statistics_of_1990 is not UNSET:
            field_dict["percentage_of_statistics_of_1990"] = (
                percentage_of_statistics_of_1990
            )
        if percentage_of_statistics_of_1991 is not UNSET:
            field_dict["percentage_of_statistics_of_1991"] = (
                percentage_of_statistics_of_1991
            )
        if percentage_of_statistics_of_1992 is not UNSET:
            field_dict["percentage_of_statistics_of_1992"] = (
                percentage_of_statistics_of_1992
            )
        if percentage_of_statistics_of_1993 is not UNSET:
            field_dict["percentage_of_statistics_of_1993"] = (
                percentage_of_statistics_of_1993
            )
        if percentage_of_statistics_of_1994 is not UNSET:
            field_dict["percentage_of_statistics_of_1994"] = (
                percentage_of_statistics_of_1994
            )
        if percentage_of_statistics_of_1995 is not UNSET:
            field_dict["percentage_of_statistics_of_1995"] = (
                percentage_of_statistics_of_1995
            )
        if percentage_of_statistics_of_1996 is not UNSET:
            field_dict["percentage_of_statistics_of_1996"] = (
                percentage_of_statistics_of_1996
            )
        if percentage_of_statistics_of_1997 is not UNSET:
            field_dict["percentage_of_statistics_of_1997"] = (
                percentage_of_statistics_of_1997
            )
        if percentage_of_statistics_of_1998 is not UNSET:
            field_dict["percentage_of_statistics_of_1998"] = (
                percentage_of_statistics_of_1998
            )
        if percentage_of_statistics_of_1999 is not UNSET:
            field_dict["percentage_of_statistics_of_1999"] = (
                percentage_of_statistics_of_1999
            )
        if percentage_of_statistics_of_2000 is not UNSET:
            field_dict["percentage_of_statistics_of_2000"] = (
                percentage_of_statistics_of_2000
            )
        if percentage_of_statistics_of_2001 is not UNSET:
            field_dict["percentage_of_statistics_of_2001"] = (
                percentage_of_statistics_of_2001
            )
        if percentage_of_statistics_of_2002 is not UNSET:
            field_dict["percentage_of_statistics_of_2002"] = (
                percentage_of_statistics_of_2002
            )
        if percentage_of_statistics_of_2003 is not UNSET:
            field_dict["percentage_of_statistics_of_2003"] = (
                percentage_of_statistics_of_2003
            )
        if percentage_of_statistics_of_2004 is not UNSET:
            field_dict["percentage_of_statistics_of_2004"] = (
                percentage_of_statistics_of_2004
            )
        if percentage_of_statistics_of_2005 is not UNSET:
            field_dict["percentage_of_statistics_of_2005"] = (
                percentage_of_statistics_of_2005
            )
        if percentage_of_statistics_of_2006 is not UNSET:
            field_dict["percentage_of_statistics_of_2006"] = (
                percentage_of_statistics_of_2006
            )
        if percentage_of_statistics_of_2007 is not UNSET:
            field_dict["percentage_of_statistics_of_2007"] = (
                percentage_of_statistics_of_2007
            )
        if percentage_of_statistics_of_2008 is not UNSET:
            field_dict["percentage_of_statistics_of_2008"] = (
                percentage_of_statistics_of_2008
            )
        if percentage_of_statistics_of_2009 is not UNSET:
            field_dict["percentage_of_statistics_of_2009"] = (
                percentage_of_statistics_of_2009
            )
        if percentage_of_statistics_of_2010 is not UNSET:
            field_dict["percentage_of_statistics_of_2010"] = (
                percentage_of_statistics_of_2010
            )
        if percentage_of_statistics_of_2011 is not UNSET:
            field_dict["percentage_of_statistics_of_2011"] = (
                percentage_of_statistics_of_2011
            )
        if percentage_of_statistics_of_2012 is not UNSET:
            field_dict["percentage_of_statistics_of_2012"] = (
                percentage_of_statistics_of_2012
            )
        if percentage_of_statistics_of_2013 is not UNSET:
            field_dict["percentage_of_statistics_of_2013"] = (
                percentage_of_statistics_of_2013
            )
        if percentage_of_statistics_of_2014 is not UNSET:
            field_dict["percentage_of_statistics_of_2014"] = (
                percentage_of_statistics_of_2014
            )
        if percentage_of_statistics_of_2015 is not UNSET:
            field_dict["percentage_of_statistics_of_2015"] = (
                percentage_of_statistics_of_2015
            )
        if percentage_of_statistics_of_2016 is not UNSET:
            field_dict["percentage_of_statistics_of_2016"] = (
                percentage_of_statistics_of_2016
            )
        if percentage_of_statistics_of_2017 is not UNSET:
            field_dict["percentage_of_statistics_of_2017"] = (
                percentage_of_statistics_of_2017
            )
        if percentage_of_statistics_of_2018 is not UNSET:
            field_dict["percentage_of_statistics_of_2018"] = (
                percentage_of_statistics_of_2018
            )
        if percentage_of_statistics_of_2019 is not UNSET:
            field_dict["percentage_of_statistics_of_2019"] = (
                percentage_of_statistics_of_2019
            )
        if percentage_of_statistics_of_2020 is not UNSET:
            field_dict["percentage_of_statistics_of_2020"] = (
                percentage_of_statistics_of_2020
            )
        if percentage_of_statistics_of_2021 is not UNSET:
            field_dict["percentage_of_statistics_of_2021"] = (
                percentage_of_statistics_of_2021
            )
        if percentage_of_statistics_of_2022 is not UNSET:
            field_dict["percentage_of_statistics_of_2022"] = (
                percentage_of_statistics_of_2022
            )
        if percentage_of_statistics_of_2023 is not UNSET:
            field_dict["percentage_of_statistics_of_2023"] = (
                percentage_of_statistics_of_2023
            )
        if percentage_of_statistics_of_2024 is not UNSET:
            field_dict["percentage_of_statistics_of_2024"] = (
                percentage_of_statistics_of_2024
            )
        if percentage_of_statistics_of_2025 is not UNSET:
            field_dict["percentage_of_statistics_of_2025"] = (
                percentage_of_statistics_of_2025
            )
        if res_district is not UNSET:
            field_dict["resDistrict"] = res_district
        if sex is not UNSET:
            field_dict["sex"] = sex
        if type_of_reported_drug_abusers is not UNSET:
            field_dict["type_of_reported_drug_abusers"] = type_of_reported_drug_abusers
        if value_of_statistics_of_1986 is not UNSET:
            field_dict["value_of_statistics_of_1986"] = value_of_statistics_of_1986
        if value_of_statistics_of_1987 is not UNSET:
            field_dict["value_of_statistics_of_1987"] = value_of_statistics_of_1987
        if value_of_statistics_of_1988 is not UNSET:
            field_dict["value_of_statistics_of_1988"] = value_of_statistics_of_1988
        if value_of_statistics_of_1989 is not UNSET:
            field_dict["value_of_statistics_of_1989"] = value_of_statistics_of_1989
        if value_of_statistics_of_1990 is not UNSET:
            field_dict["value_of_statistics_of_1990"] = value_of_statistics_of_1990
        if value_of_statistics_of_1991 is not UNSET:
            field_dict["value_of_statistics_of_1991"] = value_of_statistics_of_1991
        if value_of_statistics_of_1992 is not UNSET:
            field_dict["value_of_statistics_of_1992"] = value_of_statistics_of_1992
        if value_of_statistics_of_1993 is not UNSET:
            field_dict["value_of_statistics_of_1993"] = value_of_statistics_of_1993
        if value_of_statistics_of_1994 is not UNSET:
            field_dict["value_of_statistics_of_1994"] = value_of_statistics_of_1994
        if value_of_statistics_of_1995 is not UNSET:
            field_dict["value_of_statistics_of_1995"] = value_of_statistics_of_1995
        if value_of_statistics_of_1996 is not UNSET:
            field_dict["value_of_statistics_of_1996"] = value_of_statistics_of_1996
        if value_of_statistics_of_1997 is not UNSET:
            field_dict["value_of_statistics_of_1997"] = value_of_statistics_of_1997
        if value_of_statistics_of_1998 is not UNSET:
            field_dict["value_of_statistics_of_1998"] = value_of_statistics_of_1998
        if value_of_statistics_of_1999 is not UNSET:
            field_dict["value_of_statistics_of_1999"] = value_of_statistics_of_1999
        if value_of_statistics_of_2000 is not UNSET:
            field_dict["value_of_statistics_of_2000"] = value_of_statistics_of_2000
        if value_of_statistics_of_2001 is not UNSET:
            field_dict["value_of_statistics_of_2001"] = value_of_statistics_of_2001
        if value_of_statistics_of_2002 is not UNSET:
            field_dict["value_of_statistics_of_2002"] = value_of_statistics_of_2002
        if value_of_statistics_of_2003 is not UNSET:
            field_dict["value_of_statistics_of_2003"] = value_of_statistics_of_2003
        if value_of_statistics_of_2004 is not UNSET:
            field_dict["value_of_statistics_of_2004"] = value_of_statistics_of_2004
        if value_of_statistics_of_2005 is not UNSET:
            field_dict["value_of_statistics_of_2005"] = value_of_statistics_of_2005
        if value_of_statistics_of_2006 is not UNSET:
            field_dict["value_of_statistics_of_2006"] = value_of_statistics_of_2006
        if value_of_statistics_of_2007 is not UNSET:
            field_dict["value_of_statistics_of_2007"] = value_of_statistics_of_2007
        if value_of_statistics_of_2008 is not UNSET:
            field_dict["value_of_statistics_of_2008"] = value_of_statistics_of_2008
        if value_of_statistics_of_2009 is not UNSET:
            field_dict["value_of_statistics_of_2009"] = value_of_statistics_of_2009
        if value_of_statistics_of_2010 is not UNSET:
            field_dict["value_of_statistics_of_2010"] = value_of_statistics_of_2010
        if value_of_statistics_of_2011 is not UNSET:
            field_dict["value_of_statistics_of_2011"] = value_of_statistics_of_2011
        if value_of_statistics_of_2012 is not UNSET:
            field_dict["value_of_statistics_of_2012"] = value_of_statistics_of_2012
        if value_of_statistics_of_2013 is not UNSET:
            field_dict["value_of_statistics_of_2013"] = value_of_statistics_of_2013
        if value_of_statistics_of_2014 is not UNSET:
            field_dict["value_of_statistics_of_2014"] = value_of_statistics_of_2014
        if value_of_statistics_of_2015 is not UNSET:
            field_dict["value_of_statistics_of_2015"] = value_of_statistics_of_2015
        if value_of_statistics_of_2016 is not UNSET:
            field_dict["value_of_statistics_of_2016"] = value_of_statistics_of_2016
        if value_of_statistics_of_2017 is not UNSET:
            field_dict["value_of_statistics_of_2017"] = value_of_statistics_of_2017
        if value_of_statistics_of_2018 is not UNSET:
            field_dict["value_of_statistics_of_2018"] = value_of_statistics_of_2018
        if value_of_statistics_of_2019 is not UNSET:
            field_dict["value_of_statistics_of_2019"] = value_of_statistics_of_2019
        if value_of_statistics_of_2020 is not UNSET:
            field_dict["value_of_statistics_of_2020"] = value_of_statistics_of_2020
        if value_of_statistics_of_2021 is not UNSET:
            field_dict["value_of_statistics_of_2021"] = value_of_statistics_of_2021
        if value_of_statistics_of_2022 is not UNSET:
            field_dict["value_of_statistics_of_2022"] = value_of_statistics_of_2022
        if value_of_statistics_of_2023 is not UNSET:
            field_dict["value_of_statistics_of_2023"] = value_of_statistics_of_2023
        if value_of_statistics_of_2024 is not UNSET:
            field_dict["value_of_statistics_of_2024"] = value_of_statistics_of_2024
        if value_of_statistics_of_2025 is not UNSET:
            field_dict["value_of_statistics_of_2025"] = value_of_statistics_of_2025
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

        def _parse_age_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        age_group = _parse_age_group(d.pop("age_group", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("district", UNSET))

        def _parse_fid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fid = _parse_fid(d.pop("fid", UNSET))

        def _parse_percentage_of_statistics_of_1986(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_1986 = _parse_percentage_of_statistics_of_1986(
            d.pop("percentage_of_statistics_of_1986", UNSET)
        )

        def _parse_percentage_of_statistics_of_1987(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_1987 = _parse_percentage_of_statistics_of_1987(
            d.pop("percentage_of_statistics_of_1987", UNSET)
        )

        def _parse_percentage_of_statistics_of_1988(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_1988 = _parse_percentage_of_statistics_of_1988(
            d.pop("percentage_of_statistics_of_1988", UNSET)
        )

        def _parse_percentage_of_statistics_of_1989(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_1989 = _parse_percentage_of_statistics_of_1989(
            d.pop("percentage_of_statistics_of_1989", UNSET)
        )

        def _parse_percentage_of_statistics_of_1990(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_1990 = _parse_percentage_of_statistics_of_1990(
            d.pop("percentage_of_statistics_of_1990", UNSET)
        )

        def _parse_percentage_of_statistics_of_1991(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_1991 = _parse_percentage_of_statistics_of_1991(
            d.pop("percentage_of_statistics_of_1991", UNSET)
        )

        def _parse_percentage_of_statistics_of_1992(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_1992 = _parse_percentage_of_statistics_of_1992(
            d.pop("percentage_of_statistics_of_1992", UNSET)
        )

        def _parse_percentage_of_statistics_of_1993(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_1993 = _parse_percentage_of_statistics_of_1993(
            d.pop("percentage_of_statistics_of_1993", UNSET)
        )

        def _parse_percentage_of_statistics_of_1994(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_1994 = _parse_percentage_of_statistics_of_1994(
            d.pop("percentage_of_statistics_of_1994", UNSET)
        )

        def _parse_percentage_of_statistics_of_1995(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_1995 = _parse_percentage_of_statistics_of_1995(
            d.pop("percentage_of_statistics_of_1995", UNSET)
        )

        def _parse_percentage_of_statistics_of_1996(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_1996 = _parse_percentage_of_statistics_of_1996(
            d.pop("percentage_of_statistics_of_1996", UNSET)
        )

        def _parse_percentage_of_statistics_of_1997(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_1997 = _parse_percentage_of_statistics_of_1997(
            d.pop("percentage_of_statistics_of_1997", UNSET)
        )

        def _parse_percentage_of_statistics_of_1998(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_1998 = _parse_percentage_of_statistics_of_1998(
            d.pop("percentage_of_statistics_of_1998", UNSET)
        )

        def _parse_percentage_of_statistics_of_1999(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_1999 = _parse_percentage_of_statistics_of_1999(
            d.pop("percentage_of_statistics_of_1999", UNSET)
        )

        def _parse_percentage_of_statistics_of_2000(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2000 = _parse_percentage_of_statistics_of_2000(
            d.pop("percentage_of_statistics_of_2000", UNSET)
        )

        def _parse_percentage_of_statistics_of_2001(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2001 = _parse_percentage_of_statistics_of_2001(
            d.pop("percentage_of_statistics_of_2001", UNSET)
        )

        def _parse_percentage_of_statistics_of_2002(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2002 = _parse_percentage_of_statistics_of_2002(
            d.pop("percentage_of_statistics_of_2002", UNSET)
        )

        def _parse_percentage_of_statistics_of_2003(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2003 = _parse_percentage_of_statistics_of_2003(
            d.pop("percentage_of_statistics_of_2003", UNSET)
        )

        def _parse_percentage_of_statistics_of_2004(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2004 = _parse_percentage_of_statistics_of_2004(
            d.pop("percentage_of_statistics_of_2004", UNSET)
        )

        def _parse_percentage_of_statistics_of_2005(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2005 = _parse_percentage_of_statistics_of_2005(
            d.pop("percentage_of_statistics_of_2005", UNSET)
        )

        def _parse_percentage_of_statistics_of_2006(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2006 = _parse_percentage_of_statistics_of_2006(
            d.pop("percentage_of_statistics_of_2006", UNSET)
        )

        def _parse_percentage_of_statistics_of_2007(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2007 = _parse_percentage_of_statistics_of_2007(
            d.pop("percentage_of_statistics_of_2007", UNSET)
        )

        def _parse_percentage_of_statistics_of_2008(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2008 = _parse_percentage_of_statistics_of_2008(
            d.pop("percentage_of_statistics_of_2008", UNSET)
        )

        def _parse_percentage_of_statistics_of_2009(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2009 = _parse_percentage_of_statistics_of_2009(
            d.pop("percentage_of_statistics_of_2009", UNSET)
        )

        def _parse_percentage_of_statistics_of_2010(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2010 = _parse_percentage_of_statistics_of_2010(
            d.pop("percentage_of_statistics_of_2010", UNSET)
        )

        def _parse_percentage_of_statistics_of_2011(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2011 = _parse_percentage_of_statistics_of_2011(
            d.pop("percentage_of_statistics_of_2011", UNSET)
        )

        def _parse_percentage_of_statistics_of_2012(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2012 = _parse_percentage_of_statistics_of_2012(
            d.pop("percentage_of_statistics_of_2012", UNSET)
        )

        def _parse_percentage_of_statistics_of_2013(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2013 = _parse_percentage_of_statistics_of_2013(
            d.pop("percentage_of_statistics_of_2013", UNSET)
        )

        def _parse_percentage_of_statistics_of_2014(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2014 = _parse_percentage_of_statistics_of_2014(
            d.pop("percentage_of_statistics_of_2014", UNSET)
        )

        def _parse_percentage_of_statistics_of_2015(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2015 = _parse_percentage_of_statistics_of_2015(
            d.pop("percentage_of_statistics_of_2015", UNSET)
        )

        def _parse_percentage_of_statistics_of_2016(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2016 = _parse_percentage_of_statistics_of_2016(
            d.pop("percentage_of_statistics_of_2016", UNSET)
        )

        def _parse_percentage_of_statistics_of_2017(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2017 = _parse_percentage_of_statistics_of_2017(
            d.pop("percentage_of_statistics_of_2017", UNSET)
        )

        def _parse_percentage_of_statistics_of_2018(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2018 = _parse_percentage_of_statistics_of_2018(
            d.pop("percentage_of_statistics_of_2018", UNSET)
        )

        def _parse_percentage_of_statistics_of_2019(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2019 = _parse_percentage_of_statistics_of_2019(
            d.pop("percentage_of_statistics_of_2019", UNSET)
        )

        def _parse_percentage_of_statistics_of_2020(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2020 = _parse_percentage_of_statistics_of_2020(
            d.pop("percentage_of_statistics_of_2020", UNSET)
        )

        def _parse_percentage_of_statistics_of_2021(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2021 = _parse_percentage_of_statistics_of_2021(
            d.pop("percentage_of_statistics_of_2021", UNSET)
        )

        def _parse_percentage_of_statistics_of_2022(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2022 = _parse_percentage_of_statistics_of_2022(
            d.pop("percentage_of_statistics_of_2022", UNSET)
        )

        def _parse_percentage_of_statistics_of_2023(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2023 = _parse_percentage_of_statistics_of_2023(
            d.pop("percentage_of_statistics_of_2023", UNSET)
        )

        def _parse_percentage_of_statistics_of_2024(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2024 = _parse_percentage_of_statistics_of_2024(
            d.pop("percentage_of_statistics_of_2024", UNSET)
        )

        def _parse_percentage_of_statistics_of_2025(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_of_statistics_of_2025 = _parse_percentage_of_statistics_of_2025(
            d.pop("percentage_of_statistics_of_2025", UNSET)
        )

        def _parse_res_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        res_district = _parse_res_district(d.pop("resDistrict", UNSET))

        def _parse_sex(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sex = _parse_sex(d.pop("sex", UNSET))

        def _parse_type_of_reported_drug_abusers(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_reported_drug_abusers = _parse_type_of_reported_drug_abusers(
            d.pop("type_of_reported_drug_abusers", UNSET)
        )

        def _parse_value_of_statistics_of_1986(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_1986 = _parse_value_of_statistics_of_1986(
            d.pop("value_of_statistics_of_1986", UNSET)
        )

        def _parse_value_of_statistics_of_1987(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_1987 = _parse_value_of_statistics_of_1987(
            d.pop("value_of_statistics_of_1987", UNSET)
        )

        def _parse_value_of_statistics_of_1988(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_1988 = _parse_value_of_statistics_of_1988(
            d.pop("value_of_statistics_of_1988", UNSET)
        )

        def _parse_value_of_statistics_of_1989(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_1989 = _parse_value_of_statistics_of_1989(
            d.pop("value_of_statistics_of_1989", UNSET)
        )

        def _parse_value_of_statistics_of_1990(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_1990 = _parse_value_of_statistics_of_1990(
            d.pop("value_of_statistics_of_1990", UNSET)
        )

        def _parse_value_of_statistics_of_1991(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_1991 = _parse_value_of_statistics_of_1991(
            d.pop("value_of_statistics_of_1991", UNSET)
        )

        def _parse_value_of_statistics_of_1992(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_1992 = _parse_value_of_statistics_of_1992(
            d.pop("value_of_statistics_of_1992", UNSET)
        )

        def _parse_value_of_statistics_of_1993(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_1993 = _parse_value_of_statistics_of_1993(
            d.pop("value_of_statistics_of_1993", UNSET)
        )

        def _parse_value_of_statistics_of_1994(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_1994 = _parse_value_of_statistics_of_1994(
            d.pop("value_of_statistics_of_1994", UNSET)
        )

        def _parse_value_of_statistics_of_1995(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_1995 = _parse_value_of_statistics_of_1995(
            d.pop("value_of_statistics_of_1995", UNSET)
        )

        def _parse_value_of_statistics_of_1996(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_1996 = _parse_value_of_statistics_of_1996(
            d.pop("value_of_statistics_of_1996", UNSET)
        )

        def _parse_value_of_statistics_of_1997(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_1997 = _parse_value_of_statistics_of_1997(
            d.pop("value_of_statistics_of_1997", UNSET)
        )

        def _parse_value_of_statistics_of_1998(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_1998 = _parse_value_of_statistics_of_1998(
            d.pop("value_of_statistics_of_1998", UNSET)
        )

        def _parse_value_of_statistics_of_1999(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_1999 = _parse_value_of_statistics_of_1999(
            d.pop("value_of_statistics_of_1999", UNSET)
        )

        def _parse_value_of_statistics_of_2000(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2000 = _parse_value_of_statistics_of_2000(
            d.pop("value_of_statistics_of_2000", UNSET)
        )

        def _parse_value_of_statistics_of_2001(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2001 = _parse_value_of_statistics_of_2001(
            d.pop("value_of_statistics_of_2001", UNSET)
        )

        def _parse_value_of_statistics_of_2002(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2002 = _parse_value_of_statistics_of_2002(
            d.pop("value_of_statistics_of_2002", UNSET)
        )

        def _parse_value_of_statistics_of_2003(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2003 = _parse_value_of_statistics_of_2003(
            d.pop("value_of_statistics_of_2003", UNSET)
        )

        def _parse_value_of_statistics_of_2004(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2004 = _parse_value_of_statistics_of_2004(
            d.pop("value_of_statistics_of_2004", UNSET)
        )

        def _parse_value_of_statistics_of_2005(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2005 = _parse_value_of_statistics_of_2005(
            d.pop("value_of_statistics_of_2005", UNSET)
        )

        def _parse_value_of_statistics_of_2006(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2006 = _parse_value_of_statistics_of_2006(
            d.pop("value_of_statistics_of_2006", UNSET)
        )

        def _parse_value_of_statistics_of_2007(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2007 = _parse_value_of_statistics_of_2007(
            d.pop("value_of_statistics_of_2007", UNSET)
        )

        def _parse_value_of_statistics_of_2008(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2008 = _parse_value_of_statistics_of_2008(
            d.pop("value_of_statistics_of_2008", UNSET)
        )

        def _parse_value_of_statistics_of_2009(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2009 = _parse_value_of_statistics_of_2009(
            d.pop("value_of_statistics_of_2009", UNSET)
        )

        def _parse_value_of_statistics_of_2010(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2010 = _parse_value_of_statistics_of_2010(
            d.pop("value_of_statistics_of_2010", UNSET)
        )

        def _parse_value_of_statistics_of_2011(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2011 = _parse_value_of_statistics_of_2011(
            d.pop("value_of_statistics_of_2011", UNSET)
        )

        def _parse_value_of_statistics_of_2012(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2012 = _parse_value_of_statistics_of_2012(
            d.pop("value_of_statistics_of_2012", UNSET)
        )

        def _parse_value_of_statistics_of_2013(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2013 = _parse_value_of_statistics_of_2013(
            d.pop("value_of_statistics_of_2013", UNSET)
        )

        def _parse_value_of_statistics_of_2014(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2014 = _parse_value_of_statistics_of_2014(
            d.pop("value_of_statistics_of_2014", UNSET)
        )

        def _parse_value_of_statistics_of_2015(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2015 = _parse_value_of_statistics_of_2015(
            d.pop("value_of_statistics_of_2015", UNSET)
        )

        def _parse_value_of_statistics_of_2016(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2016 = _parse_value_of_statistics_of_2016(
            d.pop("value_of_statistics_of_2016", UNSET)
        )

        def _parse_value_of_statistics_of_2017(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2017 = _parse_value_of_statistics_of_2017(
            d.pop("value_of_statistics_of_2017", UNSET)
        )

        def _parse_value_of_statistics_of_2018(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2018 = _parse_value_of_statistics_of_2018(
            d.pop("value_of_statistics_of_2018", UNSET)
        )

        def _parse_value_of_statistics_of_2019(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2019 = _parse_value_of_statistics_of_2019(
            d.pop("value_of_statistics_of_2019", UNSET)
        )

        def _parse_value_of_statistics_of_2020(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2020 = _parse_value_of_statistics_of_2020(
            d.pop("value_of_statistics_of_2020", UNSET)
        )

        def _parse_value_of_statistics_of_2021(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2021 = _parse_value_of_statistics_of_2021(
            d.pop("value_of_statistics_of_2021", UNSET)
        )

        def _parse_value_of_statistics_of_2022(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2022 = _parse_value_of_statistics_of_2022(
            d.pop("value_of_statistics_of_2022", UNSET)
        )

        def _parse_value_of_statistics_of_2023(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2023 = _parse_value_of_statistics_of_2023(
            d.pop("value_of_statistics_of_2023", UNSET)
        )

        def _parse_value_of_statistics_of_2024(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2024 = _parse_value_of_statistics_of_2024(
            d.pop("value_of_statistics_of_2024", UNSET)
        )

        def _parse_value_of_statistics_of_2025(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value_of_statistics_of_2025 = _parse_value_of_statistics_of_2025(
            d.pop("value_of_statistics_of_2025", UNSET)
        )

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
            age_group=age_group,
            district=district,
            fid=fid,
            percentage_of_statistics_of_1986=percentage_of_statistics_of_1986,
            percentage_of_statistics_of_1987=percentage_of_statistics_of_1987,
            percentage_of_statistics_of_1988=percentage_of_statistics_of_1988,
            percentage_of_statistics_of_1989=percentage_of_statistics_of_1989,
            percentage_of_statistics_of_1990=percentage_of_statistics_of_1990,
            percentage_of_statistics_of_1991=percentage_of_statistics_of_1991,
            percentage_of_statistics_of_1992=percentage_of_statistics_of_1992,
            percentage_of_statistics_of_1993=percentage_of_statistics_of_1993,
            percentage_of_statistics_of_1994=percentage_of_statistics_of_1994,
            percentage_of_statistics_of_1995=percentage_of_statistics_of_1995,
            percentage_of_statistics_of_1996=percentage_of_statistics_of_1996,
            percentage_of_statistics_of_1997=percentage_of_statistics_of_1997,
            percentage_of_statistics_of_1998=percentage_of_statistics_of_1998,
            percentage_of_statistics_of_1999=percentage_of_statistics_of_1999,
            percentage_of_statistics_of_2000=percentage_of_statistics_of_2000,
            percentage_of_statistics_of_2001=percentage_of_statistics_of_2001,
            percentage_of_statistics_of_2002=percentage_of_statistics_of_2002,
            percentage_of_statistics_of_2003=percentage_of_statistics_of_2003,
            percentage_of_statistics_of_2004=percentage_of_statistics_of_2004,
            percentage_of_statistics_of_2005=percentage_of_statistics_of_2005,
            percentage_of_statistics_of_2006=percentage_of_statistics_of_2006,
            percentage_of_statistics_of_2007=percentage_of_statistics_of_2007,
            percentage_of_statistics_of_2008=percentage_of_statistics_of_2008,
            percentage_of_statistics_of_2009=percentage_of_statistics_of_2009,
            percentage_of_statistics_of_2010=percentage_of_statistics_of_2010,
            percentage_of_statistics_of_2011=percentage_of_statistics_of_2011,
            percentage_of_statistics_of_2012=percentage_of_statistics_of_2012,
            percentage_of_statistics_of_2013=percentage_of_statistics_of_2013,
            percentage_of_statistics_of_2014=percentage_of_statistics_of_2014,
            percentage_of_statistics_of_2015=percentage_of_statistics_of_2015,
            percentage_of_statistics_of_2016=percentage_of_statistics_of_2016,
            percentage_of_statistics_of_2017=percentage_of_statistics_of_2017,
            percentage_of_statistics_of_2018=percentage_of_statistics_of_2018,
            percentage_of_statistics_of_2019=percentage_of_statistics_of_2019,
            percentage_of_statistics_of_2020=percentage_of_statistics_of_2020,
            percentage_of_statistics_of_2021=percentage_of_statistics_of_2021,
            percentage_of_statistics_of_2022=percentage_of_statistics_of_2022,
            percentage_of_statistics_of_2023=percentage_of_statistics_of_2023,
            percentage_of_statistics_of_2024=percentage_of_statistics_of_2024,
            percentage_of_statistics_of_2025=percentage_of_statistics_of_2025,
            res_district=res_district,
            sex=sex,
            type_of_reported_drug_abusers=type_of_reported_drug_abusers,
            value_of_statistics_of_1986=value_of_statistics_of_1986,
            value_of_statistics_of_1987=value_of_statistics_of_1987,
            value_of_statistics_of_1988=value_of_statistics_of_1988,
            value_of_statistics_of_1989=value_of_statistics_of_1989,
            value_of_statistics_of_1990=value_of_statistics_of_1990,
            value_of_statistics_of_1991=value_of_statistics_of_1991,
            value_of_statistics_of_1992=value_of_statistics_of_1992,
            value_of_statistics_of_1993=value_of_statistics_of_1993,
            value_of_statistics_of_1994=value_of_statistics_of_1994,
            value_of_statistics_of_1995=value_of_statistics_of_1995,
            value_of_statistics_of_1996=value_of_statistics_of_1996,
            value_of_statistics_of_1997=value_of_statistics_of_1997,
            value_of_statistics_of_1998=value_of_statistics_of_1998,
            value_of_statistics_of_1999=value_of_statistics_of_1999,
            value_of_statistics_of_2000=value_of_statistics_of_2000,
            value_of_statistics_of_2001=value_of_statistics_of_2001,
            value_of_statistics_of_2002=value_of_statistics_of_2002,
            value_of_statistics_of_2003=value_of_statistics_of_2003,
            value_of_statistics_of_2004=value_of_statistics_of_2004,
            value_of_statistics_of_2005=value_of_statistics_of_2005,
            value_of_statistics_of_2006=value_of_statistics_of_2006,
            value_of_statistics_of_2007=value_of_statistics_of_2007,
            value_of_statistics_of_2008=value_of_statistics_of_2008,
            value_of_statistics_of_2009=value_of_statistics_of_2009,
            value_of_statistics_of_2010=value_of_statistics_of_2010,
            value_of_statistics_of_2011=value_of_statistics_of_2011,
            value_of_statistics_of_2012=value_of_statistics_of_2012,
            value_of_statistics_of_2013=value_of_statistics_of_2013,
            value_of_statistics_of_2014=value_of_statistics_of_2014,
            value_of_statistics_of_2015=value_of_statistics_of_2015,
            value_of_statistics_of_2016=value_of_statistics_of_2016,
            value_of_statistics_of_2017=value_of_statistics_of_2017,
            value_of_statistics_of_2018=value_of_statistics_of_2018,
            value_of_statistics_of_2019=value_of_statistics_of_2019,
            value_of_statistics_of_2020=value_of_statistics_of_2020,
            value_of_statistics_of_2021=value_of_statistics_of_2021,
            value_of_statistics_of_2022=value_of_statistics_of_2022,
            value_of_statistics_of_2023=value_of_statistics_of_2023,
            value_of_statistics_of_2024=value_of_statistics_of_2024,
            value_of_statistics_of_2025=value_of_statistics_of_2025,
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
