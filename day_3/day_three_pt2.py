from typing import List

from scripts.reader_script import data_reader

def common_item_finder(item_list: List[str]):
    badge_value = 0
    group_list = []
    for items in item_list:
        group_list.append(items)
        if len(group_list) == 3:
            common_item = set.intersection(*map(set,group_list)).pop()
            badge_value += ord(common_item) - 96 if  common_item.islower() else ord(common_item) - 38
            group_list = []
    return badge_value

data = data_reader("day_3/input_data.txt")
print(common_item_finder(data))