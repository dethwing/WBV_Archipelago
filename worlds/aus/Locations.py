from typing import NamedTuple
from BaseClasses import Location

class LocData(NamedTuple):
    id: int
    region: str
class AUSLocation(Location):
    game: str = "An Untitled Story"
    
    # override constructor to automatically mark event locations as such
    def __init__(self, player: int, name = "", code = None, parent = None) -> None:
        super(AUSLocation, self).__init__(player, name, code, parent)
        self.event = code is None

location_table = {
    "Nightwalk_jump_1": LocData(272001, "Menu"),
    "Coldkeep_high_branch": LocData(272002, "Menu"),
    "Stonecastle_heart_door": LocData(272003, "Menu"),
    "Skytown_shop_6": LocData(272004, "Menu"),
    "Farfall_bottom_heart_door": LocData(272005, "Farfall"),
    "Grotto_djump": LocData(272006, "Menu"),
    "Skytown_pit_right": LocData(272007, "Menu"),
    "Firecage_top_left_gate": LocData(272008, "Firecage"),
    "Nightclimb_duck": LocData(272009, "Nightclimb"),
    "Coldkeep_boss": LocData(272010, "Menu"),
    "Skysand_bot_left": LocData(272011, "Skysand"),
    # "Skytown_tp": LocData(272012, "Menu"),
    "Stonecastle_rock_boss": LocData(272013, "Menu"),
    "Deeptower_cannon_boss": LocData(272014, "Menu"),
    "Skytown_shop_7": LocData(272015, "Menu"),
    "Firecage_boss": LocData(272016, "Firecage"),
    "Nightwalk_hatch": LocData(272017, "Menu"),
    "Deepdive_shaft": LocData(272018, "Deepdive"),
    "Deepdive_left_ceiling": LocData(272019, "Deepdive"),
    "Bonus_1": LocData(272020, "Firecage"),
    "Deepdive_shaft_mid_right": LocData(272021, "Deepdive"),
    "Deeptower_top_entrance": LocData(272022, "Curtain"),
    "Mountside_right_heart_door": LocData(272023, "Mountside"),
    "Strangecastle": LocData(272024, "Strangecastle"),
    "Deeptower_heart": LocData(272101, "Menu"),
    "Coldkeep_low_branch": LocData(272102, "Menu"),
    "Nightwalk_shrine_torches": LocData(272103, "Menu"),
    "Skytown_pit_left": LocData(272104, "Menu"),
    "Nightclimb_right_heart": LocData(272105, "Nightclimb"),
    "Nightclimb_wall_heart": LocData(272106, "Nightclimb"),
    "Grotto_mural_heart": LocData(272107, "Menu"),
    "Nightclimb_top_heart": LocData(272108, "Nightclimb"),
    "Skytown_tower_heart": LocData(272109, "Nightclimb"),
    "Skytown_red_heart": LocData(272110, "Menu"),
    "Skytown_yellow_heart": LocData(272111, "Menu"),
    "Skytown_shop_1": LocData(272112, "Menu"),
    "Skytown_shop_2": LocData(272113, "Menu"),
    "Skytown_shop_3": LocData(272114, "Menu"),
    "Skytown_shop_4": LocData(272115, "Menu"),
    "Skytown_shop_5": LocData(272116, "Menu"),
    "Nightwalk_sky_heart": LocData(272117, "Menu"),
    "Farfall_kill_3": LocData(272118, "Farfall"),
    "Stonecastle_hidden_heart": LocData(272119, "Menu"),
    "Nightwalk_block_heart": LocData(272120, "Menu"),
    "Farfall_yellow_heart_door": LocData(272121, "Farfall"),
    "Farfall_bottom_heart": LocData(272122, "Farfall"),
    "Firecage_top_heart_door": LocData(272123, "Firecage"),
    "Firecage_top": LocData(272124, "Firecage"),
    "Firecage_bot_left_secret": LocData(272125, "Firecage"),
    "Nightclimb_duck_heart": LocData(272126, "Nightclimb"),
    "Firecage_mid": LocData(272127, "Firecage"),
    "Firecage_mid_heart_door": LocData(272128, "Firecage"),
    "Firecage_bot": LocData(272129, "Firecage"),
    "Farfall_3_balloons": LocData(272130, "Farfall"),
    "Bottom_heart": LocData(272131, "Bottom"),
    "Coldkeep_cannon_heart": LocData(272132, "Menu"),
    "Stonecastle_top_heart": LocData(272133, "Menu"),
    "Farfall_5_balloons": LocData(272134, "Farfall"),
    "Bonus_2": LocData(272135, "Firecage"),
    "Deepdive_shaft_top_right": LocData(272136, "Deepdive"),
    "Skysand_right_heart_door": LocData(272137, "Skysand"),
    "Skysand_left_roof": LocData(272138, "Skysand"),
    "Skysand_top": LocData(272139, "Skysand"),
    "Skysand_top_heart_door": LocData(272140, "Skysand"),
    "Cloudrun_left_under": LocData(272141, "Bottom"),
    "Cloudrun_mid_save": LocData(272142, "Bottom"),
    "Cloudrun_far_right": LocData(272143, "Bottom"),
    "Deepdive_left": LocData(272144, "Deepdive"),
    "Deepdive_shaft_top": LocData(272145, "Deepdive"),
    "Nightwalk_shrine_heart": LocData(272146, "Nightwalk"),
    "Farfall_chest": LocData(272147, "Farfall"),
    "Skysand_right_roof_chest": LocData(272148, "Skysand"),
    "Deepdive_chest": LocData(272149, "Deepdive"),
    "Nightclimb_chest": LocData(272150, "Nightclimb"),
    "Deepdive_right_path": LocData(272151, "Deepdive"),
    # "Skytown_astrocrash": LocData(272152, "Menu"), # Exclude?
    "Grotto_eye_boss": LocData(272153, "Deepdive"),
    "Darkgrotto_top_left": LocData(272154, "Darkgrotto"),
    "Darkgrotto_mid_right": LocData(272155, "Darkgrotto"),
    "Darkgrotto_boss_torch": LocData(272156, "Darkgrotto"),
    "Highlands_platform": LocData(272157, "Mountside"),
    "Nightwalk_upper_heart": LocData(272158, "Curtain"),
    "Curtain_break": LocData(272159, "Curtain"),
    "Nightwalk_chest": LocData(272160, "Curtain"),
    "Curtain_kill_4": LocData(272161, "Curtain"),
    # "Skytown_jumpbox": LocData(272162, "Menu"), # Exclude?
    # "Skytown_keep_going": LocData(272163, "Menu"), # Exclude?
    "Deepdive_exit_heart_mid": LocData(272164, "Deepdive2"),
    "Deepdive_exit_heart_top": LocData(272165, "Deepdive2"),
    "Icecastle_entrance": LocData(272166, "Curtain"),
    "Icecastle_left_outside": LocData(272167, "Curtain"),
    "Icecastle_entrance_heart_door": LocData(272168, "Curtain"),
    "Icecastle_low_mid_heartdoor": LocData(272169, "Curtain"),
    "Icecastle_high_mid_heartdoor": LocData(272170, "Curtain"),
    "Icecastle_top_left_heart_door": LocData(272171, "Curtain"),
    "Icecastle_top_right": LocData(272172, "Curtain"),
    "10_flowers": LocData(272173, "Curtain"),
    "20_flowers": LocData(272174, "Curtain"),
    "Rainbowdive_second_prize": LocData(272175, "Curtain"),
    "Rainbowdive_first_prize": LocData(272176, "Curtain"),
    "Icecastle_bottom_underhang": LocData(272177, "Curtain"),
    "Skylands_underhang": LocData(272178, "Curtain"),
    "Skylands_chest": LocData(272179, "Curtain"),
    "Skylands_duck": LocData(272180, "Curtain"),
    "Skylands_balloon_chain": LocData(272181, "Curtain"),
    "Skylands_portal": LocData(272182, "Mountside"),
    "Library_heart": LocData(272183, "Curtain"),
    "Deepdive_far_right": LocData(272184, "Deepdive2"),
    "Deepdive_shaft_bot_right": LocData(272185, "Deepdive"),
    "Blancland_top_left_kill": LocData(272186, "Blancland"),
    "Blancland_bottom_left": LocData(272187, "Blancland"),
    "Skylands_toll_gate": LocData(272188, "Curtain"),
    "Icecastle_low_mid_secret": LocData(272189, "Curtain"),
    "Blackcastle_top_mid": LocData(272190, "Blackcastle"),
    "Strangecastle_heart_door": LocData(272191, "Strangecastle"),
    "Skylands_heart_gate": LocData(272192, "Curtain"),
    "Undertomb_right_heart_door": LocData(272193, "Longbeach"),
    "Undertomb_left": LocData(272194, "Longbeach"),
    "Undertomb_left_heart_door": LocData(272195, "Longbeach"),
    "Skytown_shop_8": LocData(272201, "Menu"),
    "Farfall_blue_rock_boss": LocData(272202, "Farfall"),
    "Stonecastle_eye_boss": LocData(272203, "Menu"),
    "Skysand_boss": LocData(272204, "Skysand"),
    "Cloudrun_boss": LocData(272205, "Bottom"),
    "Deepdive_boss": LocData(272206, "Deepdive2"),
    "Darkgrotto_boss": LocData(272207, "Darkgrotto"),
    "Curtain_boss": LocData(272208, "Curtain"),
    "Icecastle_boss": LocData(272209, "Curtain"),
    "Blancland_boss": LocData(272210, "Blancland"),
    "Curtain_start_flower": LocData(272351, "Curtain"),
    "Longbeach_water_entrance_flower": LocData(272352, "Menu"),
    "Icecastle_entrance_flower": LocData(272353, "Curtain"),
    "Blancland_entrance_flower": LocData(272354, "Blancland"),
    "Stonecastle_flower": LocData(272355, "Menu"),
    "Farfall_bottom_flower": LocData(272356, "Farfall"),
    "Nightwalk_save_flower": LocData(272357, "Nightwalk"),
    "Blackcastle_end_flower": LocData(272358, "Blackcastle"),
    "Nightclimb_flower": LocData(272359, "Nightclimb"),
    "Deepdive_boss_flower": LocData(272360, "Deepdive2"),
    "Bottom_flower": LocData(272361, "Bottom"),
    "Mountside_left_flower": LocData(272362, "Mountside"),
    "Library_flower": LocData(272363, "Curtain"),
    "Darkgrotto_bot_right_flower": LocData(272364, "Darkgrotto"),
    "Nightwalk_high_flower": LocData(272365, "Curtain"),
    "Cloudrun_start_flower": LocData(272366, "Bottom"),
    "Grotto_flower": LocData(272367, "Menu"),
    "Skysand_left_outside": LocData(272368, "Skysand"),
    "Skytown_flower": LocData(272369, "Menu"),
    "Nightwalk_nest_flower": LocData(272370, "Curtain"),
    "Grotto_boss_1": LocData(272401, "Menu"),
    "Deeptower_boss_2": LocData(272402, "Menu"),
    "Coldkeep_boss_3": LocData(272403, "Menu"),
    "Nightclimb_boss_4": LocData(272404, "Nightclimb"),
    "Stonecastle_boss_5": LocData(272405, "Menu"),
    "Grotto_boss_6": LocData(272406, "Deepdive"),
    "Firecage_boss_7": LocData(272407, "Firecage"),
    "Farfall_boss_8": LocData(272408, "Farfall"),
    "Stonecastle_boss_9": LocData(272409, "Menu"),
    "Skysand_boss_10": LocData(272410, "Skysand"),
    "Cloudrun_boss_11": LocData(272411, "Bottom"),
    "Deepdive_boss_12": LocData(272412, "Deepdive2"),
    "Darkgrotto_boss_13": LocData(272413, "Darkgrotto"),
    "Curtain_boss_14": LocData(272414, "Curtain"),
    "Icecastle_boss_15": LocData(272415, "Curtain"),
    "Blancland_boss_16": LocData(272416, "Blancland"),
    "Blackcastle_boss_17": LocData(272417, "Blackcastle"),
    "5_flowers": LocData(272418, "Curtain"),
    "15_flowers": LocData(272419, "Curtain"),
    "Rainbowdive_300": LocData(272420, "Curtain"),
    "Rainbowdive_100": LocData(272421, "Curtain"),
    "Victory": LocData(27422, "Blackcastle")
}