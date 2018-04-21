import pygal

world_map = pygal.maps.world.World()
world_map.title = "North, Central and South America"

world_map.add("North America", ['ca', 'mx', 'us'])
world_map.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
world_map.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

world_map.render_to_file("americas.svg")
