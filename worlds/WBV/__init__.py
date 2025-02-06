from .Regions import link_wbv_areas, wbv_regions
from BaseClasses import Region, Entrance, Tutorial, Item
from .Options import WBVOptions
from .Items import item_table, WBVItem, item_pool
from .Locations import location_table, WBVLocation
from .Rules import WBVRules
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, components, Type
from multiprocessing import Process

class AMonsterWorldWeb(WebWorld):
    tutorials = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the Wonder Boy in Monster World ranndomizer for Archipelago.",
            "English",
            "setup_en.md",
            "setup/en",
            ["dethwing"],
        )
    ]
class WBVWorld(World):
    """

    """
    game = "Wonder Boy in Monster World (USA, Europe)"
    options_dataclass = WBVOptions
    options: WBVOptions
    topology_present = False

    #base_id = 72000
    web = AMonsterWorldWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in location_table.items()}

    def _get_wbv_data(self):
        return {
            "world_seed": self.multiworld.per_slot_randoms[self.player].getrandbits(32),
            "seed_name": self.multiworld.seed_name,
            "player_name": self.multiworld.get_player_name(self.player),
            "player_id": self.player,
        }

    def create_items(self):
        # Fill out our pool with our items from item_pool, assuming 1 item if not present in item_pool
        pool = []
        for name, data in item_table.items():
            for amount in range(item_pool.get(name, 1)):
                if name != "Victory":
                    item = WBVItem(name, data.classification, data.code, self.player)
                    print(item, amount)
                    pool.append(item)

        self.multiworld.itempool += pool

    def create_regions(self):
        def WBVRegion(region_name: str, exits=[]):
            ret = Region(region_name, self.player, self.multiworld)
            ret.locations += [WBVLocation(self.player, loc_name, loc_data.id, ret)
                             for loc_name, loc_data in location_table.items()
                             if loc_data.region == region_name]
            for exit in exits:
                ret.exits.append(Entrance(self.player, exit, ret))
            return ret

        self.multiworld.regions += [WBVRegion(*r) for r in aus_regions]
        link_wbv_areas(self.multiworld, self.player)

        self.multiworld.get_location("Victory", self.player).place_locked_item(self.create_item("Victory"))

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = WBVItem(name, item_data.classification, item_data.code, self.player)
        return item

    def set_rules(self) -> None:
        WBVRules(self).set_aus_rules()

    def get_filler_item_name(self) -> str:
        return "A cool rock"
