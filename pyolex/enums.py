#!/usr/bin/env python

# Enums used by pyolex

from enum import Enum

class Symbol(Enum): # Should be 23 in total
    BROWNCIRCLE = "Brunsirkel"
    YELLOWDANGER = "Gulfare"
    FISHINGNET_START = "Garnstart"
    FISHINGNET_STOP = "Garnstopp"

class Color(Enum): # Can we make these without Norwegian letters ø and å?
    RED = "Rød"
    BLUE = "Blå"
    GREEN = "Grønn"
    PURPLE = "Lilla"
    BROWN = "Brun"
    BLACK = "Svart"

class RouteType(Enum):
    DEFAULT = "uten navn"
    QUICKCROSS = "Hurtigkryss"
    TOWLINE = "Slepestrek"