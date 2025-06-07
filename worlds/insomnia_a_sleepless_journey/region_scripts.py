from typing import TYPE_CHECKING, Dict, List, cast

from BaseClasses import Location, Region
from worlds.generic.Rules import CollectionRule
from .region_data import LType
from .names import ItemNames as iname, RegionNames as rname

if TYPE_CHECKING:
    from . import InsomniaWorld

class ILocation(Location):
    game = "Insomnia a sleepless journey"

helper_reference: Dict[str, List[str]] = {
    iname.m_jump: [iname.lubricant, iname.boots, iname.rocket_upg, iname.rocket],
    iname.h_jump: [iname.lubricant, iname.rocket_upg],
    iname.spike_kill: [iname.helmet, iname.tennis],
    iname.any_rocket: [iname.rocket, iname.rocket_upg],
}


def convert_helper_reqs(helper_name: str, reqs: List[List[str]]) -> List[List[str]]:
    new_list_storage: List[List[str]] = []
    for i, sublist in enumerate(reqs):
        for j, req in enumerate(sublist):
            if req == helper_name:
                for replacement in helper_reference[helper_name]:
                    new_list = sublist.copy()
                    new_list[j] = replacement
                    new_list_storage.append(new_list)
                # replace the starter list with one of the storage lists to keep it from skipping an entry
                reqs[i] = new_list_storage.pop()
                break

    for sublist in new_list_storage:
        reqs.append(sublist)

    return reqs


def create_insomnia_regions(world: "InsomniaWorld") -> Dict[str, Region]:
    insomnia_regions: Dict[str, Region] = {}
    for region_name in rname:
        insomnia_regions[region_name] = Region(region_name, world.player, world.multiworld)
    return insomnia_regions


# basically any(all(individual requirements))
def interpret_rule(reqs: List[List[str]], world: "InsomniaWorld") -> CollectionRule:
    # expand the helpers into individual items
    for helper_name in helper_reference.keys():
        reqs = convert_helper_reqs(helper_name, reqs)
    return lambda state: any(state.has_all(sublist, world.player) for sublist in reqs)



def create_regions_and_set_rules(world: "InsomniaWorld") -> None:
    player = world.player
    iregions = create_insomnia_regions(world)
    for origin_name, destinations in world.traversal_requirements.items():
        origin_name = cast(str, origin_name.value)
        for destination_name, data in destinations.items():
            destination_name = cast(str, destination_name.value)

            if data.type == LType.loc:
                location = ILocation(player, destination_name, world.location_name_to_id[destination_name], iregions[origin_name])
                #location.access_rule = interpret_rule(data.rules, world)
                iregions[origin_name].locations.append(location)
            elif data.type == LType.region:
                iregions[origin_name].connect(connecting_region=iregions[destination_name])
                #rule=interpret_rule(data.rules, world)


    for region in iregions.values():
        world.multiworld.regions.append(region)