from BaseClasses import MultiWorld

def link_aus_areas(world: MultiWorld, player: int):
    for (exit, region) in mandatory_connections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))


# (Region name, list of exits)
aus_regions = [
    ("Menu", ["Nightclimb Entrance", "Deepdive Entrance", "Mountside Entrance", "Skysand Entrance", "Farfall Entrance"]),
    ("Nightclimb", []),
    ("Deepdive", ["Firecage Entrance", "Blancland Entrance", "Deepdive2 Entrance"]),
    ("Firecage", []),
    ("Mountside", ["Curtain Entrance", "Darkgrotto Entrance"]),
    ("Curtain", []),
    ("Skysand", []),
    ("Darkgrotto", []),
    ("Farfall", ["Strangecastle Entrance", "Bottom Entrance"]),
    ("Strangecastle", []),
    ("Bottom", []),
    ("Blancland", []),
    ("Deepdive2", ["Longbeach Entrance"]),
    ("Longbeach", ["Blackcastle Entrance"]),
    ("Blackcastle", []),
]

# (Entrance, region pointed to)
mandatory_connections = [

]
