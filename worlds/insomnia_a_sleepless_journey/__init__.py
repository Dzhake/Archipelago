from copy import deepcopy
from typing import Dict, List, Union
from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from .names import LocationNames, RegionNames
from .region_data import LData
from .region_scripts import create_regions_and_set_rules
from .items import item_name_to_id, item_table, item_name_groups, filler_items, InsomniaItem
from .region_data import traversal_requirements

# All the files are pretty much copypasta from https://github.com/ScipioWright/Archipelago-SW/blob/animal-well/worlds/animal_well/__init__.py

class InsomniaWebWorld(WebWorld):
    theme = "ocean"
    tutorials = [
        Tutorial(
            tutorial_name="Multiworld Setup Guide",
            description="A guide to setting up the Insomnia a sleepless journey Randomizer for Archipelago multiworld games.",
            language="English",
            file_name="en_setup.md",
            link="en/setup",
            authors=["Dzhake"]
        )
    ]
    bug_report_page = "github.com/Dzhake/insomnia-a-sleepless-journey/issues"

class InsomniaWorld(World):
    game = "Insomnia a sleepless journey"
    web = InsomniaWebWorld()

    item_name_groups = item_name_groups
    item_name_to_id = item_name_to_id
    location_name_to_id = {key: idx + 1 for idx, key in enumerate(LocationNames)}

    origin_region_name = "Main region"

    traversal_requirements: Dict[Union[LocationNames, RegionNames], Dict[Union[LocationNames, RegionNames], LData]]

    def create_item(self, name: str) -> InsomniaItem:
        item_data = item_table[name]
        return InsomniaItem(name, item_data.classification, self.item_name_to_id[name], self.player)
    
    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)
    
    def create_regions(self) -> None:
        self.traversal_requirements = deepcopy(traversal_requirements)
        create_regions_and_set_rules(self)
        return
    
    def create_items(self) -> None:
        insomnia_items : List[InsomniaItem] = []
        items_to_create: Dict[str, int] = {item: data.quantity_in_item_pool for item, data in item_table.items()}

        # Any rules about adding/removing items go here and change items_to_create

        for item_name, quantity in items_to_create.items():
            for _ in range(quantity):
                insomnia_items.append(self.create_item(item_name))

        # if there are more locations than items, add filler until there are enough items
        filler_count = len(self.multiworld.get_unfilled_locations(self.player)) - len(insomnia_items)
        for _ in range(filler_count):
            insomnia_items.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.itempool += insomnia_items

