from typing import Dict, List, NamedTuple, Optional, Union
from enum import IntEnum
from .names import ItemNames as iname, LocationNames as lname, RegionNames as rname


class LType(IntEnum):
    loc = 1
    region = 2


class LocType(IntEnum):
    chest = 0
    star = 1
    enemy = 2
    fans_switch = 3


class LData(NamedTuple):
    type: int  # location or region
    rules: List[List[str]] = [[]]  # how to access it
    # the rules are formatted such that [[wand], [disc, remote]] means you need wand OR you need disc + remote
    loc_type: Optional[LocType] = None

traversal_requirements: Dict[Union[lname, rname], Dict[Union[lname, rname], LData]] = {
    #rname.main is considered always accessible — don't write that there's a path to it
    rname.main: {
        lname.helmet_chest: LData(LType.loc, loc_type=LocType.chest),
        lname.lubricant_chest: LData(LType.loc, loc_type=LocType.chest),
        lname.boots_chest: LData(LType.loc, loc_type=LocType.chest),
        lname.map_chest: LData(LType.loc, loc_type=LocType.chest),

        lname.star_r6c3_57: LData(LType.loc, loc_type=LocType.star),
        lname.star_r6c4_54: LData(LType.loc, loc_type=LocType.star),
        lname.star_r6c5_47: LData(LType.loc, loc_type=LocType.star),
        lname.star_r6c6_52: LData(LType.loc, loc_type=LocType.star),
        lname.star_r6c8_50: LData(LType.loc, loc_type=LocType.star),
        lname.star_r6c9_48: LData(LType.loc, loc_type=LocType.star),
        lname.star_r6c10_58: LData(LType.loc, loc_type=LocType.star),
        lname.star_r6c11_51: LData(LType.loc, loc_type=LocType.star),
        lname.star_r5c7_38: LData(LType.loc, loc_type=LocType.star),
        lname.star_r5c7_46: LData(LType.loc, loc_type=LocType.star),
        lname.star_r5c8_41: LData(LType.loc, loc_type=LocType.star),
        lname.star_r5c9_42: LData(LType.loc, loc_type=LocType.star),
        lname.star_r4c10_30: LData(LType.loc, [[iname.m_jump]],LocType.star),
        lname.star_r7c4_59: LData(LType.loc, [[iname.fans],[iname.m_jump]], LocType.star),
        lname.star_r7c6_66: LData(LType.loc, [[iname.glove]],LocType.star),
        lname.star_r7c8_63: LData(LType.loc, loc_type=LocType.star),
        lname.star_r7c9_64: LData(LType.loc, loc_type=LocType.star),
        lname.star_r8c9_77: LData(LType.loc, loc_type=LocType.star),
        lname.star_r8c10_72: LData(LType.loc, [[iname.lubricant], [iname.fans], [iname.rocket_upg]], LocType.star),
        lname.star_r8c5_79: LData(LType.loc, loc_type=LocType.star),
        lname.star_r10c9_85: LData(LType.loc, loc_type=LocType.star),
        lname.star_r10c10_88: LData(LType.loc, loc_type=LocType.star),

        lname.turtle_r5c4: LData(LType.loc, loc_type=LocType.enemy),
        lname.turtle_r6c4: LData(LType.loc, loc_type=LocType.enemy),
        lname.turtle_r7c4: LData(LType.loc, [[iname.fans], [iname.m_jump]],LocType.enemy),
        lname.mushroom_r6c4: LData(LType.loc, loc_type=LocType.enemy),
        lname.mushroom_r7c5: LData(LType.loc, loc_type=LocType.enemy),
        lname.mushroom_r5c6: LData(LType.loc, loc_type=LocType.enemy),
        lname.plant_r5c7: LData(LType.loc, loc_type=LocType.enemy),
        lname.turtle_r6c7: LData(LType.loc, loc_type=LocType.enemy),
        lname.slime_r6c8: LData(LType.loc, loc_type=LocType.enemy),
        lname.mushroom_r6c10: LData(LType.loc, loc_type=LocType.enemy),
        lname.turtle_r6c11: LData(LType.loc, loc_type=LocType.enemy),
        lname.apple_r6c11: LData(LType.loc, loc_type=LocType.enemy),
        lname.turtle_r7c10: LData(LType.loc, loc_type=LocType.enemy),
        lname.turtle_r8c9: LData(LType.loc, loc_type=LocType.enemy),
        lname.imp_r4c7: LData(LType.loc, loc_type=LocType.enemy),
        lname.fakeblock_r10c9: LData(LType.loc, loc_type=LocType.enemy),
        lname.slime_r9c12: LData(LType.loc, loc_type=LocType.enemy),
        lname.turtle_r9c13: LData(LType.loc, loc_type=LocType.enemy),
        lname.apple_r4c8: LData(LType.loc, loc_type=LocType.enemy),
        lname.turtle_r4c9: LData(LType.loc, loc_type=LocType.enemy),
        lname.mushroom_r5c9: LData(LType.loc, loc_type=LocType.enemy),
        lname.slime_r6c5: LData(LType.loc, loc_type=LocType.enemy),

        lname.spikeslime_r7c3: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),
        lname.spikeslime_r5c8: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),
        lname.spikeslime_r6c9: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),
        lname.spiketurtle_r7c8: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),
        lname.spiketurtle_r8c10: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),
        lname.spinner_r10c10: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),

        rname.tunnel: LData(LType.region, [[iname.fans], [iname.m_jump]]),
        rname.below_basement_door_2: LData(LType.region, [[iname.m_jump]]),
        rname.after_lubricant: LData(LType.region, [[iname.lubricant]]),
        rname.up_mid_r: LData(LType.region, [[iname.m_jump]]),
        rname.up_mid: LData(LType.region, [[iname.any_rocket], [iname.lubricant, iname.boots]]),
        rname.up_mid_l: LData(LType.region, [[iname.lubricant], [iname.any_rocket]]),
        rname.glove_chest: LData(LType.region, [[iname.lubricant], [iname.glove, iname.rocket_upg], [iname.glove, iname.rocket, iname.helmet]]),
        rname.mushroom: LData(LType.region, [[iname.tennis]]),
        rname.down_l_r: LData(LType.region, [[iname.glove]]),
        rname.r_pack: LData(LType.region, [[iname.rocket_upg], [iname.fans]]),
        rname.near_switch: LData(LType.region, [[iname.m_jump]]),
        rname.basement: LData(LType.region, [[iname.helmet]]),
        rname.heart_chest: LData(LType.region, [[iname.fans], [iname.rocket_upg]]),
        rname.tennis_chest: LData(LType.region, [[iname.lubricant]]),
    },

    rname.below_basement_door_2: {
        lname.star_r5c10_44: LData(LType.loc, loc_type=LocType.star),
        rname.basement: LData(LType.region, [[iname.h_jump]]),
    },

    rname.basement: {
        lname.star_r10c11_91: LData(LType.loc, loc_type=LocType.star),
        lname.spiketurtle_r10c11: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),
        rname.basement_door: LData(LType.region, [[iname.glove, iname.rocket_upg], [iname.glove, iname.fans]]),
    },

    rname.basement_door: {
        lname.brain_chest: LData(LType.loc, loc_type=LocType.chest),

        lname.star_r10c12_86: LData(LType.loc, loc_type=LocType.star),
        lname.star_r1c13_2: LData(LType.loc, loc_type=LocType.star),

        lname.fakeblock_r10c12: LData(LType.loc, loc_type=LocType.enemy),
        lname.plant_r1c13: LData(LType.loc, loc_type=LocType.enemy),
        lname.eye_r1c14: LData(LType.loc, loc_type=LocType.enemy),

        rname.basement: LData(LType.region), #you can access b.d. only after accessing basement, so blocks are definitly broken
    },

    rname.after_lubricant: {
        lname.fakeblock_r4c10: LData(LType.loc, loc_type=LocType.enemy),
        lname.star_r4c11_34: LData(LType.loc, loc_type=LocType.star),
    },

    rname.tunnel: {
        lname.key_chest: LData(LType.loc, loc_type=LocType.chest),

        lname.star_r6c12_55: LData(LType.loc, loc_type=LocType.star),
        lname.star_r5c12_45: LData(LType.loc, loc_type=LocType.star),
        lname.star_r5c11_40: LData(LType.loc, [[iname.m_jump]], LocType.star),
        lname.star_r4c2_35: LData(LType.loc, loc_type=LocType.star),
        lname.star_r4c3_31: LData(LType.loc, loc_type=LocType.star),
        lname.star_r7c7_62: LData(LType.loc, loc_type=LocType.star),
        lname.star_r9c1_80: LData(LType.loc, loc_type=LocType.star),
        lname.star_r3c13_27: LData(LType.loc, [[iname.fans], [iname.h_jump]], LocType.star),

        lname.imp_r6c12: LData(LType.loc, loc_type=LocType.enemy),
        lname.imp_r5c12: LData(LType.loc, loc_type=LocType.enemy),
        lname.apple_r4c12: LData(LType.loc, loc_type=LocType.enemy),
        lname.turtle_r4c12: LData(LType.loc, loc_type=LocType.enemy),
        lname.apple_r4c2: LData(LType.loc, loc_type=LocType.enemy),
        lname.plant_r4c2: LData(LType.loc, loc_type=LocType.enemy),
        lname.eye_r4c3: LData(LType.loc, loc_type=LocType.enemy),
        lname.slime_r7c7: LData(LType.loc, loc_type=LocType.enemy),

        lname.spinner_r5c12: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),

        rname.tunnel_door: LData(LType.region, [[iname.tennis]]),
        rname.after_lubricant: LData(LType.region, [[iname.rocket_upg]]),
        rname.up_r: LData(LType.region, [[iname.rocket, iname.fans], [iname.h_jump]]),
        rname.up_left: LData(LType.region, [[iname.rocket_upg]]),
    },

    rname.tunnel_door: {
        lname.star_r10c1_92: LData(LType.loc, loc_type=LocType.star),
        lname.star_r3c14_21: LData(LType.loc, loc_type=LocType.star),

        lname.plant_r3c14: LData(LType.loc, loc_type=LocType.enemy),
        lname.faceleft_r10c1: LData(LType.loc, loc_type=LocType.enemy),
        lname.spikeseal_r10c1: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),

        rname.tunnel: LData(LType.region),
    },

    rname.up_left: {
        lname.star_r3c2_22: LData(LType.loc, loc_type=LocType.star),
        lname.star_r3c2_28: LData(LType.loc, loc_type=LocType.star),
        lname.star_r2c3_9: LData(LType.loc, loc_type=LocType.star),
        lname.star_r1c3_0: LData(LType.loc, loc_type=LocType.star),
        lname.star_r1c10_4: LData(LType.loc, loc_type=LocType.star),
        lname.star_r2c10_11: LData(LType.loc, loc_type=LocType.star),
        lname.star_r3c10_23: LData(LType.loc, loc_type=LocType.star),

        lname.imp_r3c3: LData(LType.loc, loc_type=LocType.enemy),
        lname.eye_r2c3: LData(LType.loc, loc_type=LocType.enemy),
        lname.turtle_r1c2: LData(LType.loc, loc_type=LocType.enemy),
        lname.faceleft_r1c10: LData(LType.loc, loc_type=LocType.enemy),
        lname.seal_r3c10: LData(LType.loc, loc_type=LocType.enemy),

        lname.spikeseal_r2c10: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),

        rname.tunnel: LData(LType.region),
    },

    rname.r_pack: {
        lname.rocket_chest: LData(LType.loc, loc_type=LocType.chest),

        lname.star_r8c11_73: LData(LType.loc, [[iname.m_jump]], LocType.star),
        lname.star_r8c12_74: LData(LType.loc, [[iname.any_rocket]], LocType.star),

        lname.spikeseal_r8c11: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),
    },

    rname.near_switch: {
        lname.star_r7c11_65: LData(LType.loc, loc_type=LocType.star),
        lname.turtle_r7c12: LData(LType.loc, loc_type=LocType.enemy),
        rname.switch: LData(LType.region, [[iname.lubricant]]),
    },

    rname.switch: {
        lname.star_r7c13_60: LData(LType.loc, [[iname.h_jump], [iname.fans]], LocType.star),
        lname.star_r5c13_39: LData(LType.loc, [[iname.rocket_upg], [iname.fans]], LocType.star),
        lname.imp_r7c13: LData(LType.loc, [[iname.h_jump], [iname.fans]], loc_type=LocType.enemy),
        lname.fans_switch: LData(LType.loc, loc_type=LocType.fans_switch),

        rname.near_switch: LData(LType.region, [[iname.lubricant]]),
        rname.after_switch: LData(LType.region, [[iname.fans], [iname.rocket_upg]]),
    },

    rname.after_switch: {
        lname.star_r6c13_49: LData(LType.loc, loc_type=LocType.star),
        lname.faceright_r6c13: LData(LType.loc, loc_type=LocType.enemy),

        rname.switch: LData(LType.region),
        rname.before_well: LData(LType.region, [[iname.glove]]),
    },

    rname.before_well: {
        lname.star_r6c14_53: LData(LType.loc, loc_type=LocType.star),
        lname.fakeblock_r6c14: LData(LType.loc, loc_type=LocType.enemy),

        rname.after_switch: LData(LType.region),
        rname.well: LData(LType.region, [[iname.helmet]])
    },

    rname.well: {
        lname.star_r8c14_70: LData(LType.loc, [[iname.rocket_upg]], LocType.star), #techically nothing is required but you need to rerun to there again without using helmet or use helmet very carefully.. annoying
        lname.star_r8c13_69: LData(LType.loc, loc_type=LocType.star),

        lname.fakeblock_r8c13: LData(LType.loc, loc_type=LocType.enemy),
        lname.seal_r8c5: LData(LType.loc, loc_type=LocType.enemy),
        lname.spikeslime_r8c14: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),

        rname.in_well: LData(LType.region, [[iname.hamburger]]),
    },

    rname.in_well: {
        lname.star_r10c14_98: LData(LType.loc, loc_type=LocType.star),
        lname.star_r10c13_89: LData(LType.loc, loc_type=LocType.star),

        lname.fish_r10c14: LData(LType.loc, loc_type=LocType.enemy),
        lname.fish_r9c14: LData(LType.loc, loc_type=LocType.enemy),
        lname.spinner_r10c13: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),

        rname.well: LData(LType.region),
    },

    rname.heart_chest: {
        lname.heart_chest: LData(LType.loc, loc_type=LocType.chest),
        lname.star_r2c13_13: LData(LType.loc, [[iname.m_jump]], LocType.star),
        lname.seal_r2c14: LData(LType.loc, loc_type=LocType.enemy),
    },

    rname.up_r: {
        lname.star_r3c12_26: LData(LType.loc, loc_type=LocType.star),
        lname.turtle_r2c12: LData(LType.loc, loc_type=LocType.enemy),
        rname.tunnel: LData(LType.region),
        rname.up_r_top: LData(LType.region, [[iname.h_jump]])
    },

    rname.up_r_top: {
        lname.star_r2c12_12: LData(LType.loc, loc_type=LocType.star),
        lname.star_r1c12_6: LData(LType.loc, loc_type=LocType.star),
        lname.star_r10c4_96: LData(LType.loc, [[iname.mushroom, iname.helmet]], LocType.star),
        
        lname.fakeblock_r1c12: LData(LType.loc, loc_type=LocType.enemy),
        lname.seal_r10c4: LData(LType.loc, [[iname.mushroom]], LocType.enemy),
        rname.up_r: LData(LType.region),
    },

    rname.up_mid: {
        lname.star_r4c6_32: LData(LType.loc, loc_type=LocType.star),
        lname.spiketurtle_r4c6: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),

        rname.the_door: LData(LType.region, [[iname.rocket_upg]]),
    },

    rname.up_mid_r: {
        lname.star_r4c8_29: LData(LType.loc, loc_type=LocType.star),
        lname.star_r3c9_20: LData(LType.loc, loc_type=LocType.star),
        lname.star_r2c11_16: LData(LType.loc, loc_type=LocType.star),
        lname.star_r1c11_1: LData(LType.loc, [[iname.fans], [iname.h_jump]], LocType.star),

        lname.eye_r3c9: LData(LType.loc, loc_type=LocType.enemy),
        lname.spikeslime_r4c9: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),
        lname.faceright_r1c11: LData(LType.loc, [[iname.fans], [iname.h_jump]], LocType.enemy),
        lname.mushroom_r2c11: LData(LType.loc, [[iname.fans], [iname.h_jump]], LocType.enemy),

        rname.the_door: LData(LType.region, [[iname.any_rocket]]),
    },

    rname.the_door: {
        lname.rocket_upg_chest: LData(LType.loc, loc_type=LocType.chest),

        lname.star_r3c8_19: LData(LType.loc, loc_type=LocType.star),
        lname.star_r3c7_18: LData(LType.loc, loc_type=LocType.star),
        lname.star_r2c6_14: LData(LType.loc, loc_type=LocType.star),
        lname.star_r2c9_10: LData(LType.loc, loc_type=LocType.star),
        lname.star_r3c11_17: LData(LType.loc, [[iname.m_jump]], LocType.star),

        lname.mushroom_r3c6: LData(LType.loc, loc_type=LocType.enemy),
        lname.fakeblock_r2c6: LData(LType.loc, loc_type=LocType.enemy),
        lname.eye_r2c7: LData(LType.loc, loc_type=LocType.enemy),
        lname.slime_r2c8: LData(LType.loc, loc_type=LocType.enemy),
        lname.plant_r2c9: LData(LType.loc, loc_type=LocType.enemy),

        rname.up_mid: LData(LType.region),
        rname.up_mid_r: LData(LType.region),
    },

    rname.up_mid_l: {
        lname.star_r5c5_37: LData(LType.loc, loc_type=LocType.star),
        lname.star_r4c5_33: LData(LType.loc, loc_type=LocType.star),
        lname.spinner_r4c5: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),

        rname.tunnel: LData(LType.region, [[iname.any_rocket]]),
        rname.up_mid_l_top: LData(LType.region, [[iname.h_jump]]),
    },

    rname.up_mid_l_top: {
        lname.star_r3c4_25: LData(LType.loc, loc_type=LocType.star),
        lname.star_r2c4_15: LData(LType.loc, loc_type=LocType.star),
        lname.star_r1c4_7: LData(LType.loc, loc_type=LocType.star),
        lname.star_r1c5_3: LData(LType.loc, loc_type=LocType.star),
        lname.star_r1c1_5: LData(LType.loc, loc_type=LocType.star),

        lname.fish_r1c1: LData(LType.loc, loc_type=LocType.enemy),
        lname.faceleft_r1c5: LData(LType.loc, loc_type=LocType.enemy),
        lname.eye_r2c4: LData(LType.loc, loc_type=LocType.enemy),
        lname.turtle_r3c4: LData(LType.loc, loc_type=LocType.enemy),
        lname.spiketurtle_r2c4: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),

        rname.up_mid_l: LData(LType.region),
    },

    rname.glove_chest: {
        lname.glove_chest: LData(LType.loc, loc_type=LocType.chest),
        lname.spiketurtle_r6c2: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),
    },

    rname.mushroom: {
        lname.mushroom_chest: LData(LType.loc, loc_type=LocType.chest),

        lname.star_r7c2_61: LData(LType.loc, [[iname.h_jump], [iname.fans]], LocType.star),
        lname.star_r7c1_67: LData(LType.loc, loc_type=LocType.star),
        lname.star_r6c1_56: LData(LType.loc, loc_type=LocType.star),
        lname.star_r5c1_36: LData(LType.loc, [[iname.mushroom]], loc_type=LocType.star),

        lname.fakeblock_r7c2: LData(LType.loc, loc_type=LocType.enemy),
        lname.plant_r7c1: LData(LType.loc, loc_type=LocType.enemy),
        lname.seal_r7c1: LData(LType.loc, loc_type=LocType.enemy),
        lname.faceright_r6c1: LData(LType.loc, loc_type=LocType.enemy),
        lname.imp_r5c1: LData(LType.loc, [[iname.mushroom]], LocType.enemy),

        rname.down_l: LData(LType.region, [[iname.helmet]])
    },

    rname.down_l_r: {
        lname.star_r8c4_75: LData(LType.loc, loc_type=LocType.star),
        lname.star_r9c4_84: LData(LType.loc, loc_type=LocType.star),
        lname.spikeseal_r8c4: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),
        rname.down_l_r_d: LData(LType.region, [[iname.h_jump]]),
    },

    rname.down_l_r_d: {
        lname.star_r9c3_81: LData(LType.loc, loc_type=LocType.star),
        lname.star_r3c1_24: LData(LType.loc, [[iname.mushroom, iname.rocket_upg], [iname.mushroom, iname.fans]], LocType.star),
        lname.star_r2c1_8: LData(LType.loc, loc_type=LocType.star),

        lname.spinner_r3c1: LData(LType.loc, [[iname.spike_kill]], LocType.enemy),
        lname.faceleft_r9c3: LData(LType.loc, loc_type=LocType.enemy),
    },

    rname.down_l: {
        lname.star_r5c14_43: LData(LType.loc, loc_type=LocType.star), #you need iname.tennis to get to down_l too.
        lname.star_r8c3_78: LData(LType.loc, loc_type=LocType.star),
        lname.star_r8c1_68: LData(LType.loc, [[iname.m_jump]], LocType.star),
        lname.star_r9c2_82: LData(LType.loc, loc_type=LocType.star),

        lname.plant_r8c1: LData(LType.loc, loc_type=LocType.enemy),
        
        rname.down_l_b: LData(LType.region, [[iname.hamburger]]),
    },

    rname.down_l_b: {
        lname.star_r10c2_93: LData(LType.loc, loc_type=LocType.star),
        lname.star_r10c3_87: LData(LType.loc, loc_type=LocType.star),

        lname.fish_r10c2: LData(LType.loc, loc_type=LocType.enemy),

        rname.down_l: LData(LType.region),
    },

    rname.tennis_chest: {
        lname.tennis_chest: LData(LType.loc, loc_type=LocType.chest),
        lname.star_r8c8_76: LData(LType.loc, [[iname.m_jump]], LocType.star),
        rname.after_tennis_chest: LData(LType.region, [[iname.tennis, iname.rocket_upg], [iname.tennis, iname.helmet]]),
    },

    rname.after_tennis_chest: {
        lname.star_r9c5_83: LData(LType.loc, loc_type=LocType.star),
        lname.star_r8c6_71: LData(LType.loc, loc_type=LocType.star),
        lname.star_r10c5_97: LData(LType.loc, [[iname.hamburger]], LocType.star),
        lname.star_r10c6_95: LData(LType.loc, [[iname.hamburger]], LocType.star),
        lname.star_r10c7_94: LData(LType.loc, [[iname.hamburger]], LocType.star),

        lname.faceright_r8c6: LData(LType.loc, loc_type=LocType.enemy),
        lname.fish_r10c5: LData(LType.loc, [[iname.hamburger]], LocType.enemy),
        lname.fish_r10c7: LData(LType.loc, [[iname.hamburger]], LocType.enemy),

        #We definitly have tennis, no need to check for iname.spikekill
        lname.spinner_r10c6: LData(LType.loc, [[iname.hamburger]], LocType.enemy),

        rname.tennis_chest: LData(LType.region),
        rname.hamburger_chest: LData(LType.region, [[iname.glove]]),
    },

    rname.hamburger_chest: {
        lname.hamburger_chest: LData(LType.loc, loc_type=LocType.chest),

        lname.star_r10c8_90: LData(LType.loc, [[iname.hamburger]], LocType.star),
        lname.spinner_r10c8: LData(LType.loc, [[iname.hamburger]], LocType.enemy),
        lname.fish_r9c8: LData(LType.loc, [[iname.hamburger]], LocType.enemy),
        rname.after_tennis_chest: LData(LType.region),
    }
}