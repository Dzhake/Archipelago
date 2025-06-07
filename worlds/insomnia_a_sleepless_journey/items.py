from itertools import groupby
from typing import Dict, List, NamedTuple, Set
from BaseClasses import ItemClassification, Item
from .names import ItemNames as iname
IClass = ItemClassification  # just to make the lines shorter


class InsomniaItem(Item):
    game: str = "Insomnia a sleepless journey"


class InsomniaItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int  # put 0 for things not in the pool by default
    item_group: str = ""

def fix_item_table(item_table: Dict[iname, InsomniaItemData]) -> Dict[str, InsomniaItemData]:
    return {str(key): value for key, value in item_table.items()}

item_table: Dict[str, InsomniaItemData] = fix_item_table({
    iname.boots: InsomniaItemData(IClass.progression | IClass.useful, 1, "Equipment"),
    iname.helmet: InsomniaItemData(IClass.progression | IClass.useful, 1, "Equipment"),
    iname.key: InsomniaItemData(IClass.progression | IClass.useful, 1, "Equipment"),
    iname.tennis: InsomniaItemData(IClass.progression | IClass.useful, 1, "Equipment"),
    iname.lubricant: InsomniaItemData(IClass.progression | IClass.useful, 1, "Equipment"),
    iname.rocket: InsomniaItemData(IClass.progression | IClass.useful, 1, "Equipment"),
    iname.rocket_upg: InsomniaItemData(IClass.progression | IClass.useful, 1, "Equipment"),
    iname.hamburger: InsomniaItemData(IClass.progression | IClass.useful, 1, "Equipment"),
    iname.glove: InsomniaItemData(IClass.progression | IClass.useful, 1, "Equipment"),
    iname.heart: InsomniaItemData(IClass.useful, 1, "Equipment"),
    iname.mushroom: InsomniaItemData(IClass.progression | IClass.useful, 1, "Equipment"),
    iname.map: InsomniaItemData(IClass.useful, 1, "Equipment"),
    iname.brain: InsomniaItemData(IClass.useful, 1, "Equipment"),
    iname.fans: InsomniaItemData(IClass.progression | IClass.useful, 1, "FansSwitch"),
    iname.star: InsomniaItemData(IClass.progression, 99, "Star"),
    iname.kill: InsomniaItemData(IClass.progression, 99, "Kill"),
})

item_name_to_id: Dict[str, int] = {key: idx + 1 for idx, key in enumerate(item_table)}

filler_items: List[str] = [iname.star, iname.kill]


def get_item_group(item_name: str) -> str:
    return item_table[item_name].item_group


item_name_groups: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group) if group != ""
}