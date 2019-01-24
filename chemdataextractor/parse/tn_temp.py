# -*- coding: utf-8 -*-
"""
Temporary test solution for the sort of parser that would be generated automatically by code for Tc.

:codeauthor: Taketomo Isazawa (ti250@cam.ac.uk)
"""

from .auto import BaseAutoParser, AutoTableParser, construct_unit_element, match_dimensions_of, value_element, value_element_plain, cem, chemical_label, lenient_chemical_label
from ..utils import first
from ..model.model import NeelTemperature, Compound
from .elements import W, I, R, T, Optional, Any, OneOrMore, Not, ZeroOrMore, Group
from .common import lbrct, rbrct


class NeelTemperatureParser(BaseAutoParser):
    model = NeelTemperature
    value_phrase_tag = 'neeltemperature'
    root_phrase_tag = 'neeltemperaturephrase'
    property_name = 'neel_temperature'


class NeelTemperatureTableParser(AutoTableParser):
    model = NeelTemperature
    value_phrase_tag = 'neeltemperature'
    root_phrase_tag = 'neeltemperaturephrase'
    property_name = 'neel_temperature'
