print('Hello world!')

from worlds.generic.Rules import exclusion_rules
from BaseClasses import Region, Entrance, Tutorial, Item
from .Options import AUSOptions
from .Items import item_table, AUSItem
from .Locations import location_table, AUSLocation
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, components, Type
from multiprocessing import Process

class AnUntitledStoryWeb(WebWorld):
    tutorials = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the An Untitled Story randomizer for Archipelago.",
            "English",
            "setup_en.md",
            "setup/en",
            ["ThatOneGuy27"],
        )
    ]
class AUSWorld(World):
    """
    A freeware metroidvania game created by Maddy Thorson chronicling the travels of an adventurous egg.
    """
    game = "An Untitled Story"
    options_dataclass = AUSOptions
    options: AUSOptions
    topology_present = False

    base_id = 272000
    web = AnUntitledStoryWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in location_table.items()}

    data_version = 7

    def _get_aus_data(self):
        return {
            "world_seed": self.multiworld.per_slot_randoms[self.player].getrandbits(32),
            "seed_name": self.multiworld.seed_name,
            "player_name": self.multiworld.get_player_name(self.player),
            "player_id": self.player,
        }

    # def create_regions(self):
    #     def UndertaleRegion(region_name: str, exits=[]):
    #         ret = Region(region_name, self.player, self.multiworld)
    #         ret.locations += [UndertaleAdvancement(self.player, loc_name, loc_data.id, ret)
    #                          for loc_name, loc_data in advancement_table.items()
    #                          if loc_data.region == region_name and
    #                          (loc_name not in exclusion_table["NoStats"] or
    #                           (self.multiworld.rando_stats[self.player] and
    #                            (self.multiworld.route_required[self.player] == "genocide" or
    #                             self.multiworld.route_required[self.player] == "all_routes"))) and
    #                          (loc_name not in exclusion_table["NoLove"] or
    #                           (self.multiworld.rando_love[self.player] and
    #                            (self.multiworld.route_required[self.player] == "genocide" or
    #                             self.multiworld.route_required[self.player] == "all_routes"))) and
    #                          loc_name not in exclusion_table[self.multiworld.route_required[self.player].current_key]]
    #         for exit in exits:
    #             ret.exits.append(Entrance(self.player, exit, ret))
    #         return ret

    #     self.multiworld.regions += [UndertaleRegion(*r) for r in undertale_regions]
    #     link_undertale_areas(self.multiworld, self.player)

    # def fill_slot_data(self):
    #     slot_data = self._get_undertale_data()
    #     for option_name in undertale_options:
    #         option = getattr(self.multiworld, option_name)[self.player]
    #         if (option_name == "rando_love" or option_name == "rando_stats") and \
    #                 self.multiworld.route_required[self.player] != "genocide" and \
    #                 self.multiworld.route_required[self.player] != "all_routes":
    #             option.value = False
    #         if slot_data.get(option_name, None) is None and type(option.value) in {str, int}:
    #             slot_data[option_name] = int(option.value)
    #     return slot_data

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        item = AUSItem(name, item_data.classification, item_data.code, self.player)
        return item
