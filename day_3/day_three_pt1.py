from typing import List

from scripts.reader_script import data_reader

def common_item_finder(item_list: List[str]):
    item_halves = [[whole_item[:len(whole_item)//2], whole_item[len(whole_item)//2:]] for whole_item in item_list]
    item_priority = 0
    for items in item_halves:
        common_item = set.intersection(*map(set,items)).pop()
        item_priority += ord(common_item) - 96 if  common_item.islower() else ord(common_item) - 38
    return item_priority

data = data_reader("day_3/input_data.txt")
print(common_item_finder(data))