import pygal

world_map = pygal.maps.world.World()

world_map.title = "Populations of Countries in North America"
world_map.add("North America", {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

world_map.render_to_file("output/na_populations.svg")
