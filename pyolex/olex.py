import calendar

from .enumerations import RouteType, Symbol, Color
from .structures import Waypoint
from .utils import dd2dm, dm2dd

def generate_olex_route(waypoints: [Waypoint], plotset=1, color=None):
    # Initialize an empty route string
    route_string = ""

    route_string += f"Rute uten navn\n"

    if color != None:
        route_string += f"Linjefarge {color.value}\n"
    
    route_string += f"Plottsett {plotset}\n"

    # Iterate over each waypoint in the list
    for waypoint in waypoints:
        dd_lat, dd_lon, name, timestamp, symbol = waypoint

        dm_lat, dm_lon = dd2dm(dd_lat, dd_lon)
        timestamp_seconds = calendar.timegm(timestamp.utctimetuple())

        route_line = f"{dm_lat} {dm_lon} {timestamp_seconds} {symbol.value}\n"
        route_string += route_line

        if name != "":
            name_line = f"Navn {name}\n"
            route_string += name_line

    return route_string