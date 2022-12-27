from typing import List, Tuple

from scripts.reader_script import data_reader

def create_str_cleaning_range(ranges: List[str]):
    range_list = [([clean_ranges[0][0], clean_ranges[0][1]], [clean_ranges[1][0], clean_ranges[1][1]]) for clean_ranges in separate_ranges(ranges)]
    return range_list

def separate_ranges(ranges: List[str]):
    for range in ranges:
        group_lists = range.split(",")
        yield ([*map(int,group_lists[0].split("-"))], [*map(int,group_lists[1].split("-"))])

def check_for_same_ranges(range_list: List[Tuple[str]]):
    repeat_counter = 0
    for elf_duet in range_list:
        if (elf_duet[0][1] >= elf_duet[1][0] and elf_duet[0][1] <= elf_duet[1][1]) or (elf_duet[1][1] >= elf_duet[0][0] and elf_duet[1][1] <= elf_duet[0][1]):
            repeat_counter += 1
    return repeat_counter

data = data_reader("day_4/input_data.txt")
cleaning_ranges = create_str_cleaning_range(data)
print(check_for_same_ranges(cleaning_ranges))