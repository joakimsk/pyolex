from typing import NamedTuple
from datetime import datetime

from .enumerations import RouteType, Symbol, Color

class Waypoint(NamedTuple):
    lat: float
    lon: float
    name: str
    timestamp: datetime.timestamp
    symbol: Symbol
