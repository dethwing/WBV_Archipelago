from typing import Dict, TYPE_CHECKING
from worlds.AutoWorld import LogicMixin
from worlds.generic.Rules import CollectionRule, set_rule, add_rule, add_item_rule
from BaseClasses import MultiWorld, CollectionState
from . import Options

if TYPE_CHECKING:
    from . import AUSWorld


class AUSRules:
    player: int
    world: "AUSWorld"
    region_rules: Dict[str, CollectionRule]
    location_rules: Dict[str, CollectionRule]
    boss_drop_values: Dict[str, int]
    maximum_price: int
    required_seals: int 
    ORB_COUNT: int = 10

    def __init__(self, world: "AUSWorld") -> None:
        self.player = world.player
        self.world = world

        self.region_rules = {
            "Nightclimb": lambda state: self.jump_height_min(state, 5) and self.has_fire(state) and self.double_jump_min(state, 1),
            "Deepdive": lambda state: self.jump_height(state) + (self.can_crouch(state) and self.has_red_energy(state)) * 2 >= 8 and 
                                        self.hatched(state) and self.can_smash(state),
            "Firecage": lambda state: self.can_stick(state) and self.has_red_energy(state) and self.can_shoot(state),
            "Mountside": lambda state: self.jump_height(state) + self.can_crouch(state) * 2 >= 8 and
                                         self.has_red_energy(state) and self.hatched(state),
            "Curtain": lambda state: self.jump_height_min(state, 8) and self.can_slide(state) and 
                                        state.has_all({"Red Energy", "Yellow Energy", "Hatch", "Ice Shot"}, self.player),
            "Skysand": lambda state: self.single_jump_min(state, 2) and self.double_jump_min(state, 2) and self.can_slide(state) and
                                        state.has_all({"Red Energy", "Progressive Fire Shot", "Ice Shot"}, self.player),
            "Darkgrotto": lambda state: self.has_ice(state) and self.can_smash(state),
            "Farfall": lambda state: self.jump_height_min(state, 4) and state.has_all({"Red Energy", "Smash", "Hatch"}, self.player),
            "Strangecastle": lambda state: (self.jump_height(state) + self.can_stick(state)) >= 7,
            "Bottom": lambda state: self.jump_height_min(state, 6.5) and self.can_slide(state),
            "Blancland": lambda state: self.jump_height_min(state, 8) and state.has("Extra Air Capacity", self.player),
            "Deepdive2": lambda state: self.jump_height_min(state, 7) and (self.single_jump_min(state, 3) or self.can_slide(state)),
            "Blackcastle": lambda state: state.has("Gold Orb", self.player, self.ORB_COUNT) and self.single_jump_min(state, 3) and
                                            self.double_jump_min(state, 2) and self.can_smash(state) and self.can_slide(state),
        }

        self.location_rules = {
            # nightwalk
            "Nightwalk_save_flower": lambda state: self.jump_height_min(state, 5),
            "Nightwalk_sky_heart": lambda state: (self.can_crouch(state) and self.jump_height_min(state, 6) and (self.double_jump_min(state, 2) or self.can_slide(state))) or state.can_reach("Curtain", "Region", self.player),
            "Nightwalk_block_heart": lambda state: self.can_smash(state) and (self.jump_height_min(state, 2) or self.double_jump_min(state, 1)),
            "Nightwalk_hatch": lambda state: (self.can_crouch(state) and self.jump_height_min(state, 6) and self.double_jump_min(state, 1)) or state.can_reach("Curtain", "Region", self.player),
            "Nightwalk_shrine_heart": lambda state: self.jump_height_min(state, 2.5),
            "Nightwalk_shrine_torches": lambda state: self.jump_height_min(state, 2.5) and self.can_light_torches(state),
            # nightclimb
            "Nightclimb_duck_heart": lambda state: self.can_crouch(state) and self.hatched(state),
            "Nightclimb_right_heart": lambda state: self.jump_height_min(state, 5) and self.has_fire(state),
            "Nightclimb_chest": lambda state: self.jump_height_min(state, 5) and self.has_fire(state),
            # grotto
            "Grotto_djump": lambda state: self.jump_height_min(state, 3.5),
            "Grotto_boss_1": lambda state: self.jump_height_min(state, 3.5),
            "Grotto_flower": lambda state: (self.jump_height(state)+(self.can_crouch(state) and self.has_red_energy(state))*2 >= 8) and self.hatched(state),
            "Grotto_mural_heart": lambda state: self.jump_height_min(state, 4) and (self.double_jump_height(state)+(self.can_stick(state))>=2),
            # deeptower
            "Deeptower_cannon_boss": lambda state: self.jump_height_min(state, 4),
            "Deeptower_boss_2": lambda state: self.jump_height_min(state, 4),
            "Deeptower_heart": lambda state: self.jump_height_min(state, 4) and (self.double_jump_height(state)+self.can_slide(state)),
            # coldkeep
            "Coldkeep_cannon_heart": lambda state: self.jump_height_min(state, 5) and self.has_ice(state),
            "Coldkeep_boss": lambda state: self.jump_height_min(state, 5),
            "Coldkeep_boss_3": lambda state: self.jump_height_min(state, 5),
            "Coldkeep_high_branch": lambda state: self.jump_height_min(state, 4),
            "Coldkeep_low_branch": lambda state: self.jump_height_min(state, 4),
            # skytown
            "Skytown_yellow_heart": lambda state: self.jump_height_min(state, 4) and self.has_yellow_energy(state),
            "Skytown_red_heart": lambda state: (self.jump_height_min(state, 4) and self.has_red_energy(state)) or (state.can_reach("Nightclimb", "Region", self.player) and self.has_ice(state)),
            "Skytown_shop_1": lambda state: self.total_money(state, 100),
            "Skytown_shop_2": lambda state: self.total_money(state, 100),
            "Skytown_shop_3": lambda state: self.total_money(state, 100),
            "Skytown_shop_4": lambda state: self.total_money(state, 100),
            "Skytown_shop_5": lambda state: self.total_money(state, 500),
            "Skytown_shop_6": lambda state: self.total_money(state, 500),
            "Skytown_shop_7": lambda state: self.total_money(state, 500),
            "Skytown_shop_8": lambda state: self.total_money(state, 1000),
            # "Skytown_astrocrash": lambda state: False,
            # "Skytown_jumpbox": lambda state: False,
            # "Skytown_keep_going": lambda state: False,
            "Skytown_flower": lambda state: self.jump_height_min(state, 4),
            "Skytown_pit_left": lambda state: self.jump_height_min(state, 5) and self.has_fire(state),
            "Skytown_tp": lambda state: self.jump_height_min(state, 4),
            "Skytown_pit_right": lambda state: (self.jump_height_min(state, 3) and self.can_slide(state)) or self.double_jump_min(state, 2),
            # farfall
            "Farfall_kill_3": lambda state: self.jump_height_min(state, 5) and self.double_jump_min(state, 1),
            "Farfall_chest": lambda state: self.jump_height_min(state, 4),
            "Farfall_5_balloons": lambda state: self.jump_height_min(state, 7),
            "Farfall_bottom_heart_door": lambda state: self.jump_height_min(state, 5) and self.double_jump_min(state, 1) and self.can_smash(state) and self.has_red_energy(state),
            "Farfall_bottom_heart": lambda state: self.jump_height_min(state, 5) and self.double_jump_min(state, 1) and self.can_smash(state) and self.has_red_energy(state),
            "Farfall_bottom_flower": lambda state: self.jump_height_min(state, 5) and self.double_jump_min(state, 1) and self.can_smash(state) and self.has_red_energy(state),
            "Farfall_yellow_heart_door": lambda state: self.jump_height_min(state, 5) and self.double_jump_min(state, 1) and self.can_smash(state) and self.has_red_energy(state) and self.has_yellow_energy(state),
            # stonecastle
            "Stonecastle_flower": lambda state: self.jump_height_min(state, 5),
            "Stonecastle_top_heart": lambda state: self.jump_height_min(state, 8) and self.has_red_energy(state) and self.has_yellow_energy(state),
            "Stonecastle_heart_door": lambda state: self.jump_height_min(state, 4),
            "Stonecastle_hidden_heart": lambda state: self.jump_height_min(state, 4),
            "Stonecastle_rock_boss": lambda state: ((self.jump_height_min(state, 4) and self.double_jump_min(state, 1)) or self.jump_height_min(state, 5)) and self.can_smash(state) and self.has_red_energy(state),
            "Stonecastle_boss_5": lambda state: ((self.jump_height_min(state, 4) and self.double_jump_min(state, 1)) or self.jump_height_min(state, 5)) and self.has_red_energy(state),
            "Stonecastle_eye_boss": lambda state: self.jump_height_min(state, 8) and self.has_red_energy(state) and self.has_yellow_energy(state) and self.can_slide(state) and self.can_smash(state),
            "Stonecastle_boss_9": lambda state: self.jump_height_min(state, 8) and self.has_red_energy(state) and self.has_yellow_energy(state) and self.can_slide(state) and self.can_smash(state),
            # deepdive
            "Deepdive_left_ceiling": lambda state: self.double_jump_min(state, 3),
            "Deepdive_left": lambda state: self.double_jump_min(state, 3),
            "Deepdive_chest": lambda state: self.double_jump_min(state, 3),
            "Deepdive_shaft": lambda state: (self.has_ice(state) or self.jump_height_min(state, 8)),
            "Deepdive_shaft_top_right": lambda state: self.has_ice(state) and self.jump_height_min(state, 6.5) and state.has("Extra Air Capacity", self.player),
            "Deepdive_shaft_bot_right": lambda state: self.jump_height_min(state, 8) and state.has("Extra Air Capacity", self.player, 2),
            "Deepdive_right_path": lambda state: self.jump_height_min(state, 7),
            "Deepdive_exit_heart_mid": lambda state: self.has_ice(state),
            # firecage
            "Firecage_top_left_gate": lambda state: (self.can_slide(state) or self.has_fire(state)),
            "Firecage_top": lambda state: self.has_fire(state),
            "Firecage_mid": lambda state: self.jump_height_min(state, 6.5) and self.has_yellow_energy(state),
            "Firecage_mid_heart_door": lambda state: self.jump_height_min(state, 8) and self.has_yellow_energy(state),
            "Firecage_bot": lambda state: self.jump_height_min(state, 6.5) and self.can_slide(state) and self.has_yellow_energy(state),
            "Firecage_boss": lambda state: self.jump_height_min(state, 6.5) and self.has_yellow_energy(state),
            "Firecage_boss_7": lambda state: self.jump_height_min(state, 6.5) and self.has_yellow_energy(state),
            # skysand
            "Skysand_bot_left": lambda state: self.has_ice(state) and (self.has_red_energy(state) or self.jump_height_min(state, 8)) and self.can_stick(state),
            "Skysand_top": lambda state: self.has_yellow_energy(state) and self.double_jump_min(state, 3),
            # cloudrun
            "Cloudrun_left_under": lambda state: self.jump_height_min(state, 7),
            "Cloudrun_mid_save": lambda state: self.jump_height_min(state, 7) and self.has_fire(state),
            "Cloudrun_boss": lambda state: self.jump_height_min(state, 7) and self.has_fire(state) and self.has_ice(state),
            "Cloudrun_boss_11": lambda state: self.jump_height_min(state, 7) and self.has_fire(state) and self.has_ice(state),
            "Cloudrun_far_right": lambda state: self.jump_height_min(state, 7) and self.has_fire(state) and self.has_ice(state),
            # highlands
            "Highlands_platform": lambda state: self.has_yellow_energy(state) and (self.double_jump_min(state, 3) or (self.double_jump_min(state, 2) and self.can_slide(state))) and self.has_ice(state),
            # darkgrotto
            "Darkgrotto_top_left": lambda state: self.has_yellow_energy(state) and self.jump_height_min(state, 7),
            "Darkgrotto_boss_torch": lambda state: self.can_light_torches(state),
            # the curtain
            "Curtain_start_flower": lambda state: self.has_yellow_energy(state) and (self.double_jump_min(state, 3) or (self.can_slide(state) and self.double_jump_min(state, 2))) and self.has_ice(state),
            "Curtain_break": lambda state: self.can_smash(state),
            # longbeach
            "Longbeach_water_entrance_flower": lambda state: (state.can_reach("Deepdive2", "Region", self.player) or state.can_reach("Darkgrotto", "Region", self.player)) and self.double_jump_min(state, 3) and self.can_slide(state),
            # icecastle
            "Icecastle_bottom_underhang": lambda state: self.can_smash(state),
            "Icecastle_boss": lambda state: self.can_smash(state),
            "Icecastle_boss_15": lambda state: self.can_smash(state),
            # blackcastle
            "Blackcastle_end_flower": lambda state: self.has_fire(state),
            "Blackcastle_top_mid": lambda state: self.can_shoot(state),
            "Victory": lambda state: True,
            # staircase
            "5_flowers": lambda state: state.has("Secret Flower", self.player, 5),
            "10_flowers": lambda state: state.has("Secret Flower", self.player, 10),
            "15_flowers": lambda state: state.has("Secret Flower", self.player, 15),
            "20_flowers": lambda state: state.has("Secret Flower", self.player, 20),
            # skylands
            "Skylands_underhang": lambda state: self.can_smash(state),
            "Skylands_duck": lambda state: self.can_smash(state) and self.can_crouch(state),
            "Skylands_balloon_chain": lambda state: self.can_smash(state),
            "Skylands_heart_gate": lambda state: self.can_smash(state),
            # blancland
            "Blancland_bottom_left": lambda state: self.has_red_energy(state) and self.has_ice(state),
            "Blancland_top_left_kill": lambda state: self.has_red_energy(state) and self.has_fire(state) and self.can_slide(state),
            "Blancland_boss": lambda state: self.has_red_energy(state) and self.has_fire(state),
            "Blancland_boss_16": lambda state: self.has_red_energy(state) and self.has_fire(state),
            # mountside
            "Mountside_left_flower": lambda state: self.double_jump_min(state, 3),
            # strangecastle
            "Strangecastle": lambda state: self.jump_height_min(state, 2) and self.has_range(state),
            "Strangecastle_heart_door": lambda state: self.jump_height_min(state, 2) and self.has_range(state),
            # undertomb
            "Undertomb_right_heart_door": lambda state: self.can_smash(state),
            "Undertomb_left": lambda state: self.can_smash(state),
            "Undertomb_left_heart_door": lambda state: self.can_smash(state),
        }

        self.boss_drop_values = {
            # 10, 25 and 35 are marked as filler and thus not progression items
            "50 Crystals": 50,
            "75 Crystals": 75,
            "110 Crystals": 110,
            "65 Crystals": 65,
            "125 Crystals": 125,
            "180 Crystals": 180,
            "270 Crystals": 270,
            "150 Crystals": 150,
            "200 Crystals": 200,
            "235 Crystals": 235,
            "245 Crystals": 245,
            "400 Crystals": 400,
            "300 Crystals": 300,
            "100 Crystals": 100,
        }

    def total_money(self, state: CollectionState, amount: int) -> int:
        money: int = 0
        for key, value in self.boss_drop_values.items():
            money += state.count(key, self.player) * value
        return money >= amount

    def jump_height(self, state: CollectionState) -> int:
        count: int
        if state.count("Jump Upgrade", self.player) == 3 and state.count("Double Jump Upgrade", self.player) == 1:
            count = 6.5
        else:
            count = state.count("Jump Upgrade", self.player) + state.count("Double Jump Upgrade", self.player) + 2
        return count
    
    def jump_height_min(self, state: CollectionState, amount: int) -> bool:
        count = self.jump_height(state)
        return count >= amount

    def single_jump_min(self, state: CollectionState, amount: int) -> bool:
        return state.count("Jump Upgrade", self.player) >= amount

    def double_jump_height(self, state: CollectionState) -> int:
        return state.count("Double Jump Upgrade", self.player)

    def double_jump_min(self, state: CollectionState, amount: int) -> bool:
        return state.count("Double Jump Upgrade", self.player) >= amount

    def has_red_energy(self, state: CollectionState) -> bool:
        return state.has("Red Energy", self.player)

    def has_yellow_energy(self, state: CollectionState) -> bool:
        return state.has("Yellow Energy", self.player)

    def can_crouch(self, state: CollectionState) -> bool:
        return state.has("Duck", self.player)

    def can_stick(self, state: CollectionState) -> bool:
        return state.has("Progressive Ceiling Stick", self.player)
    
    def can_slide(self, state: CollectionState) -> bool:
        return state.has("Progressive Ceiling Stick", self.player, 2)

    def can_smash(self, state: CollectionState) -> bool:
        return state.has("Smash", self.player)
    
    def has_fire(self, state: CollectionState) -> bool:
        return state.has("Progressive Fire Shot", self.player)
    
    def has_range(self, state: CollectionState) -> bool:
        return state.has("Progressive Fire Shot", self.player, 2)
    
    def has_ice(self, state: CollectionState) -> bool:
        return state.has("Ice Shot", self.player)
    
    def can_shoot(self, state: CollectionState) -> bool:
        return self.has_fire(state) or self.has_ice(state)
    
    def can_light_torches(self, state: CollectionState) -> bool:
        return self.has_fire(state) or self.can_smash(state)
    
    def hatched(self, state: CollectionState) -> bool:
        return state.has("Hatch", self.player)    

    def true(self, state: CollectionState) -> bool:
        """Hi Messenger!"""
        return True


    def set_aus_rules(self) -> None:
        multiworld = self.world.multiworld

        for region in multiworld.get_regions(self.player):
            if region.name in self.region_rules:
                for entrance in region.entrances:
                    entrance.access_rule = self.region_rules[region.name]
            for loc in region.locations:
                if loc.name in self.location_rules:
                    loc.access_rule = self.location_rules[loc.name]

        multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)