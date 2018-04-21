import json
from pygal_maps_world.i18n import COUNTRIES

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


# Print the 2010 population for each country
for pop_dict in pop_data:
    if pop_dict.get("Year") == '2010':
        country_name = pop_dict.get("Country Name")
        population = int(float(pop_dict.get("Value")))
        code = get_country_code(country_name)

        if code:
            print(code + ":"  + str(population))
        else:
            print("ERROR - " + country_name)


