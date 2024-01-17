from BaseClasses import Item, ItemClassification
from typing import Dict, NamedTuple

class AUSItemData(NamedTuple):
    code: int
    classification: ItemClassification

class AUSItem(Item):
    game: str = "An Untitled Story"

item_table = {
    "Jump Upgrade": AUSItemData(272001, ItemClassification.progression),
    "Red Energy": AUSItemData(272004, ItemClassification.progression),
    "Lucky Pots": AUSItemData(272005, ItemClassification.useful), 
    "Double Jump Upgrade": AUSItemData(272006, ItemClassification.progression),
    "Duck": AUSItemData(272009, ItemClassification.progression),
    "Progressive Ceiling Stick": AUSItemData(272010, ItemClassification.progression),
    # "Teleport": AUSItemData(272012, ItemClassification.progression), # given automatically
    "Smash": AUSItemData(272013, ItemClassification.useful),
    "Progressive Fire Shot": AUSItemData(272014, ItemClassification.progression),
    "Yellow Energy": AUSItemData(272016, ItemClassification.progression),
    "Hatch": AUSItemData(272017, ItemClassification.progression),
    "Extra Air Capacity": AUSItemData(272018, ItemClassification.progression),
    "Money Magnet": AUSItemData(272020, ItemClassification.useful),
    "Ice Shot": AUSItemData(272021, ItemClassification.progression),
    "Toughness Upgrade": AUSItemData(272022, ItemClassification.useful),
    "Heart": AUSItemData(272100, ItemClassification.useful),
    "Gold Orb": AUSItemData(272200, ItemClassification.progression),
    "Secret Flower": AUSItemData(272300, ItemClassification.progression),
    "10 Crystals": AUSItemData(272401, ItemClassification.filler),
    "25 Crystals": AUSItemData(272402, ItemClassification.filler),
    "35 Crystals": AUSItemData(272403, ItemClassification.filler),
    "50 Crystals": AUSItemData(272405, ItemClassification.progression),
    "75 Crystals": AUSItemData(272406, ItemClassification.progression),
    "110 Crystals": AUSItemData(272407, ItemClassification.progression),
    "65 Crystals": AUSItemData(272408, ItemClassification.progression),
    "125 Crystals": AUSItemData(272409, ItemClassification.progression),
    "180 Crystals": AUSItemData(272410, ItemClassification.progression),
    "270 Crystals": AUSItemData(272411, ItemClassification.progression),
    "150 Crystals": AUSItemData(272412, ItemClassification.progression),
    "200 Crystals": AUSItemData(272413, ItemClassification.progression),
    "235 Crystals": AUSItemData(272415, ItemClassification.progression),
    "245 Crystals": AUSItemData(272417, ItemClassification.progression),
    "400 Crystals": AUSItemData(272419, ItemClassification.progression),
    "300 Crystals": AUSItemData(272420, ItemClassification.progression),
    "100 Crystals": AUSItemData(272421, ItemClassification.progression),
}

item_pool: Dict[str, int] = {
    "Jump Upgrade": 3,
    "Double Jump Upgrade": 3,
    "Progressive Ceiling Stick": 2,
    "Progressive Fire Shot": 2,
    "Extra Air Capacity": 2,
    "Toughness Upgrade": 3,
    "Heart": 92,
    "Gold Orb": 10,
    "Secret Flower": 20,
    "35 Crystals": 2,
    "150 Crystals": 2,
    "200 Crystals": 3,
}