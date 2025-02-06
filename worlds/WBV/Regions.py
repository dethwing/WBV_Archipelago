from BaseClasses import MultiWorld, Region

def link_wbv_areas(world: MultiWorld, player: int):
    for (exit, region) in mandatory_connections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))


# (Region name, list of exits)
wbv_regions = [
    ("Menu", ["Lillypad_Dungeon Entrance", "Underwater Entrance", "Desert Entrance", "Ice Castle Entrance", "Nightmare Castle Entrance"]),
    ("Lillypad_Dungeon", []),
    ("Underwater", ["Poseidon Entrance"]),    
    ("Poseidon", []),
    ("Ice Castle", []),
    ("Desert", ["Pyramid Entrance"]),
    ("Pyramid", ["Begonia Entrance"]),
    ("Begonia", ["Nightmare Castle"]),
    ("Nightmare Castle", [])
]

# (Entrance, region pointed to)
mandatory_connections = [
    ("Lillypad_Dungeon Entrance", "Lillypad_Dungeon"),
    ("Underwater Entrance", "Underwater"),
    ("Desert Entrance", "Desert"),
    ("Ice Castle Entrance", "Ice Castle"),
    ("Nightmare Castle Entrance", "Nightmare Castle"),
    ("Poseidon Entrance", "Poseidon"),
    ("Pyramid Entrance", "Pyramid"),
    ("Begonia Entrance", "Begonia"),    
]
