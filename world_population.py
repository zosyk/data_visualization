import json
from pygal_maps_world.i18n import COUNTRIES
import pygal
from pygal.style import RotateStyle, LightColorizedStyle

# Load the data into a list

filename = "resources/population_data.json"

with open(filename) as f:
    pop_data = json.load(f)


def get_country_code(country_name):
    """ Return the Pygal 2-digit country code for a given country"""

    for code, name in COUNTRIES.items():
        if (name == country_name):
            return code

    return None


# Build a dictionary of population data.
cc_populations = {}

for pop_dict in pop_data:
    if pop_dict.get("Year") == '2010':
        country_name = pop_dict.get("Country Name")
        population = int(float(pop_dict.get("Value")))
        code = get_country_code(country_name)

        if code:
            cc_populations[code] = population

# Group the country into 3 population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
world_map = pygal.maps.world.World(style=wm_style)


world_map.title = "World population in 2010, by Country"
world_map.add("0-10m", cc_pops_1)
world_map.add("10m-1bn", cc_pops_2)
world_map.add(">1bn", cc_pops_3)

world_map.render_to_file("output/world_population.svg")
