from BaseClasses import Item, ItemClassification
from typing import Dict, NamedTuple

class WBVItemData(NamedTuple):
    code: int
    classification: ItemClassification

class AUSItem(Item):
    game: str = "An Untitled Story"

item_table = {
    "Legend Sword": WBVItemData(128, ItemClassification.progression),
    "Trident": WBVItemData(133, ItemClassification.progression),
    "Pygmy Sword": WBVItemData(135, ItemClassification.progression),
    "Legend Armor": WBVItemData(136, ItemClassification.useful),
    "Pygmy Armor": WBVItemData(143, ItemClassification.progression),
    
    "Legend Shield": WBVItemData(144, ItemClassification.useful),
    "Pygmy Shield": WBVItemData(151, ItemClassification.progression),
    "Legend Boots": WBVItemData(152, ItemClassification.useful),    
    "Oasis Boots": WBVItemData(154, ItemClassification.progression),   
    "Pygmy Boots": WBVItemData(159, ItemClassification.progression),

    "Firestorm": WBVItemData(160, ItemClassification.useful),
    "Quake": WBVItemData(161, ItemClassification.useful),
    "Thunder": WBVItemData(162, ItemClassification.useful),
    "Power": WBVItemData(163, ItemClassification.useful),
    "Shield": WBVItemData(164, ItemClassification.filler),
    
    "Return": WBVItemData(165, ItemClassification.useful),
    "Charmstone": WBVItemData(169, ItemClassification.useful),
    "Elixer": WBVItemData(170, ItemClassification.useful),
    "Holywater": WBVItemData(173, ItemClassification.useful),
    "Charmstone": WBVItemData(174, ItemClassification.filler),
    
    "Lamp": WBVItemData(177, ItemClassification.progression),
    "Amulet": WBVItemData(178, ItemClassification.progression),    
    "Sun-Key": WBVItemData(179, ItemClassification.progression),
    "Moon-Key": WBVItemData(180, ItemClassification.progression),
    "Star-Key": WBVItemData(181, ItemClassification.progression),
    
    "Gold-Gem": WBVItemData(182, ItemClassification.progression),
    "Blue-Gem": WBVItemData(183, ItemClassification.progression),
    "Fire-Urn": WBVItemData(185, ItemClassification.progression),
    "Bracelet": WBVItemData(186, ItemClassification.progression),    
    "Heart": WBVItemData(192, ItemClassification.filler),
    
    "Victory": WBVItemData(None, ItemClassification.progression)
}

item_pool: Dict[str, int] = {
    
}
