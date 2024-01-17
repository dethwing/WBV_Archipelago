from BaseClasses import MultiWorld, Region

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
    ("Curtain", ["Longbeach Upper Entrance"]),
    ("Skysand", []),
    ("Darkgrotto", ["Longbeach Middle Entrance"]),
    ("Farfall", ["Strangecastle Entrance", "Bottom Entrance"]),
    ("Strangecastle", []),
    ("Bottom", []),
    ("Blancland", []),
    ("Deepdive2", ["Longbeach Lower Entrance"]),
    ("Longbeach", ["Blackcastle Entrance"]),
    ("Blackcastle", []),
]

# (Entrance, region pointed to)
mandatory_connections = [
    ("Nightclimb Entrance", "Nightclimb"),
    ("Deepdive Entrance", "Deepdive"),
    ("Mountside Entrance", "Mountside"),
    ("Skysand Entrance", "Skysand"),
    ("Farfall Entrance", "Farfall"),
    ("Firecage Entrance", "Firecage"),
    ("Blancland Entrance", "Blancland"),
    ("Deepdive2 Entrance", "Deepdive2"),
    ("Curtain Entrance", "Curtain"),
    ("Darkgrotto Entrance", "Darkgrotto"),
    ("Strangecastle Entrance", "Strangecastle"),
    ("Bottom Entrance", "Bottom"),
    ("Longbeach Upper Entrance", "Longbeach"),
    ("Longbeach Middle Entrance", "Longbeach"),
    ("Longbeach Lower Entrance", "Longbeach"),
    ("Blackcastle Entrance", "Blackcastle"),
]
