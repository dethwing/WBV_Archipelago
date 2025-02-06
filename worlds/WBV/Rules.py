from typing import Dict, TYPE_CHECKING
from worlds.AutoWorld import LogicMixin
from worlds.generic.Rules import CollectionRule, set_rule, add_rule, add_item_rule
from BaseClasses import MultiWorld, CollectionState
from . import Options

if TYPE_CHECKING:
    from . import WBVWorld


class WBVRules:
    player: int
    world: "WBVWorld"
    region_rules: Dict[str, CollectionRule]
    location_rules: Dict[str, CollectionRule]
    boss_drop_values: Dict[str, int]
    maximum_price: int
    required_seals: int 


    def __init__(self, world: "WBVWorld") -> None:
        self.player = world.player
        self.world = world

        self.region_rules = {
            "Lillypad_Dungeon": lambda state: self.Has_Lamp(state),
            "Underwater": lambda state: self.Has_Trident(state),
            "Poseidon": lambda state: self.Has_Trident(state) and self.Has_Amulet(state),
            "Ice Castle": lambda state: self.Has_Bracelet(state),
            "Desert": lambda state: self.Has_Oasis(state),
            "Pyramid": lambda state: self.Has_Oasis(state) and self.Has_Sun(state),
            "Begonia": lambda state: self.Has_Oasis(state) and self.Has_Star(state),
            "Nightmare Castle": lambda state: self.Has_Legend(state) and self.Has_Urn(state) and self.Has_Gems(state)
        }

        self.location_rules = {
            "Hard_Shield": lambda state: self.Has_Lamp(state),
            "Elixers": lambda state: self.Has_Lamp(state),
            "Trident": lambda state: self.Has_Lamp(state),

            "Money": lambda state: self.Has_Trident(state),
            "Pygmy_Armor": lambda state: self.Has_Trident(state),
            "Pygmy_Sword": lambda state: self.Has_Trident(state),
            "Amulet": lambda state: self.Has_Trident(state),
            "Thunder": lambda state: self.Has_Trident(state),
            
            "Oasis_Boots": lambda state: self.Has_Trident(state) and self.Has_Amulet(state),
            "Return": lambda state: self.Has_Trident(state) and self.Has_Amulet(state),
            
            "Shield_Magic_Chest": lambda state: self.Has_Oasis(state),
            "Sun_Key": lambda state: self.Has_Oasis(state) and self.Has_Trident(state),
            
            "Pygmy_Boots": lambda state: self.Has_Bracelet(state),
            "Blue_Gem": lambda state: self.Has_Bracelet(state),
            "Gold_Gem": lambda state: self.Has_Bracelet(state),
            "Old_Axe": lambda state: self.Has_Bracelet(state) and self.Has_Gems(state),
            
            "Moon_Key": lambda state: self.Has_Oasis(state) and self.Has_Sun(state),
            "Secret_Chest_1": lambda state: self.Has_Oasis(state) and self.Has_Sun(state),
            "Secret_Chest_2": lambda state: self.Has_Oasis(state) and self.Has_Sun(state),
            "Secret_Chest_3": lambda state: self.Has_Oasis(state) and self.Has_Sun(state),
            "Secret_Chest_4": lambda state: self.Has_Oasis(state) and self.Has_Sun(state),
            "Secret_Chest_5": lambda state: self.Has_Oasis(state) and self.Has_Sun(state),
            "Star_Key": lambda state: self.Has_Oasis(state) and self.Has_Sun(state),
            "Pygmy_Shield": lambda state: self.Has_Oasis(state) and self.Has_Moon(state),
            
            "Power": lambda state: self.Has_Oasis(state) and self.Has_Star(state),
            "Fire_Urn": lambda state: self.Has_Oasis(state) and self.Has_Star(state) and self.Has_Pygmy(state)
                        and self.Has_Bracelet(state) and self.Has_Gems(state),
            "Charmstone_Chest": lambda state: self.Has_Oasis(state) and self.Has_Star(state) and self.Has_Pygmy(state),
            
            "Victory": LocData(None, "Nightmare Castle")                
        }        

    def Has_Lamp(self, state: CollectionState) -> bool:
        return state.has("Lamp", self.player)

    def Has_Trident(self, state: CollectionState) -> bool:
        return state.has("Trident", self.player)

    def Has_Oasis(self, state: CollectionState) -> bool:
        return state.has("Oasis Boots", self.player)

    def Has_Bracelet(self, state: CollectionState) -> bool:
        return state.has("Bracelet", self.player)
    
    def Has_Sun(self, state: CollectionState) -> bool:
        return state.has("Sun-Key", self.player, 2)

    def Has_Moon(self, state: CollectionState) -> bool:
        return state.has("Moon-Key", self.player)
    
    def Has_Star(self, state: CollectionState) -> bool:
        return state.has("Star-Key", self.player)
    
    def Has_Amulet(self, state: CollectionState) -> bool:
        return state.has("Amulet", self.player, 2)
    
    def Has_Gems(self, state: CollectionState) -> bool:
        return state.has("Blue-Gem", self.player) and state.has("Gold-Gem", self.player)
    
    def Has_Pygmy(self, state: CollectionState) -> bool:
        return state.has("Pygmy Sword", self.player) and state.has("Pygmy Armor", self.player) and state.has("Pygmy Shield", self.player) and state.has("Pygmy Boots", self.player)
    
    def true(self, state: CollectionState) -> bool:
        """Hi Messenger!"""
        return True


    def set_wbv_rules(self) -> None:
        multiworld = self.world.multiworld

        for region in multiworld.get_regions(self.player):
            if region.name in self.region_rules:
                for entrance in region.entrances:
                    entrance.access_rule = self.region_rules[region.name]
            for loc in region.locations:
                if loc.name in self.location_rules:
                    loc.access_rule = self.location_rules[loc.name]

        multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
