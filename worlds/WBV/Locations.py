from typing import NamedTuple
from BaseClasses import Location

class LocData(NamedTuple):
    id: hex
    region: str
class WBVLocation(Location):
    game: str = "An Untitled Story"
    
    # override constructor to automatically mark event locations as such
    def __init__(self, player: int, name = "", code = None, parent = None) -> None:
        super(WBVLocation, self).__init__(player, name, code, parent)
        self.event = code is None

location_table = {
    "Firestorm": LocData(0xA752, "Menu"),
    "Bat_Drop": LocData(0x2CA09, "Menu"),
    "Quake": LocData(0xA738, "Menu"),
    
    "Hard_Shield": LocData(0xA74E, "Lillypad_Dungeon"),
    "Elixers": LocData(0xA74C, "Lillypad_Dungeon"),
    "Trident": LocData(0xA756, "Lillypad_Dungeon"),

    "Money": LocData(0xA75E, "Underwater"),
    "Pygmy_Armor": LocData(0xA2A, "Underwater"),
    "Pygmy_Sword": LocData(0xA728, "Underwater"),
    "Amulet": LocData(0xA754, "Underwater"),
    "Thunder": LocData(0xA734, "Underwater"),
    
    "Oasis_Boots": LocData(0xA754, "Poseidon"),
    "Return": LocData(0xA734, "Poseidon"),
    
    "Shield_Magic_Chest": LocData(0xA730, "Desert"),
    "Sun_Key": LocData(0xA730, "Desert"),
    
    "Pygmy_Boots": LocData(0xA72E, "Ice Castle"),
    "Blue_Gem": LocData(0xA744, "Ice Castle"),
    "Gold_Gem": LocData(0xA746, "Ice Castle"),
    "Old_Axe": LocData(0xA758, "Ice Castle"),
    
    "Moon_Key": LocData(0xA73A, "Pyramid"),
    "Secret_Chest_1": LocData(0xA76A, "Pyramid"),
    "Secret_Chest_2": LocData(0xA76C, "Pyramid"),
    "Secret_Chest_3": LocData(0xA76E, "Pyramid"),
    "Secret_Chest_4": LocData(0xA770, "Pyramid"),
    "Secret_Chest_5": LocData(0xA772, "Pyramid"),
    "Star_Key": LocData(0xA73E, "Pyramid"),
    "Pygmy_Shield": LocData(0xA72C, "Pyramid"),
    
    "Power": LocData(0xA750, "Begonia"),
    "Fire_Urn": LocData(0xA75A, "Begonia"),
    "Charmstone_Chest": LocData(0xA740, "Begonia"),
    
    "Victory": LocData(None, "Nightmare Castle")
    
}
