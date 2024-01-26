from BaseClasses import Item, ItemClassification
from typing import Dict, NamedTuple

class AUSItemData(NamedTuple):
    code: int
    classification: ItemClassification

class AUSItem(Item):
    game: str = "An Untitled Story"

item_table = {
    "Jump Upgrade": AUSItemData(72001, ItemClassification.progression),
    "Red Energy": AUSItemData(72004, ItemClassification.progression),
    "Lucky Pots": AUSItemData(72005, ItemClassification.useful), 
    "Double Jump Upgrade": AUSItemData(72006, ItemClassification.progression),
    "Duck": AUSItemData(72009, ItemClassification.progression),
    "Progressive Ceiling Stick": AUSItemData(72010, ItemClassification.progression),
    # "Teleport": AUSItemData(72012, ItemClassification.progression), # given automatically
    "Smash": AUSItemData(72013, ItemClassification.progression),
    "Progressive Fire Shot": AUSItemData(72014, ItemClassification.progression),
    "Yellow Energy": AUSItemData(72016, ItemClassification.progression),
    "Hatch": AUSItemData(72017, ItemClassification.progression),
    "Extra Air Capacity": AUSItemData(72018, ItemClassification.progression),
    "Money Magnet": AUSItemData(72020, ItemClassification.useful),
    "Ice Shot": AUSItemData(72021, ItemClassification.progression),
    "Toughness Upgrade": AUSItemData(72022, ItemClassification.useful),
    "Heart": AUSItemData(72100, ItemClassification.filler),
    "Gold Orb": AUSItemData(72200, ItemClassification.progression),
    "Secret Flower": AUSItemData(72300, ItemClassification.progression),
    "10 Crystals": AUSItemData(72401, ItemClassification.filler),
    "25 Crystals": AUSItemData(72402, ItemClassification.filler),
    "35 Crystals": AUSItemData(72403, ItemClassification.filler),
    "50 Crystals": AUSItemData(72405, ItemClassification.progression),
    "75 Crystals": AUSItemData(72406, ItemClassification.progression),
    "110 Crystals": AUSItemData(72407, ItemClassification.progression),
    "65 Crystals": AUSItemData(72408, ItemClassification.progression),
    "125 Crystals": AUSItemData(72409, ItemClassification.progression),
    "180 Crystals": AUSItemData(72410, ItemClassification.progression),
    "270 Crystals": AUSItemData(72411, ItemClassification.progression),
    "150 Crystals": AUSItemData(72412, ItemClassification.progression),
    "200 Crystals": AUSItemData(72414, ItemClassification.progression),
    "235 Crystals": AUSItemData(72417, ItemClassification.progression),
    "245 Crystals": AUSItemData(72418, ItemClassification.progression),
    "400 Crystals": AUSItemData(72419, ItemClassification.progression),
    "300 Crystals": AUSItemData(72420, ItemClassification.progression),
    "100 Crystals": AUSItemData(72421, ItemClassification.progression),
    "Victory": AUSItemData(None, ItemClassification.progression)
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