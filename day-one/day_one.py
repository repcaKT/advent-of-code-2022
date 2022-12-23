from typing import List

def find_most_calories(file_name: str, number_of_elves: int) -> List[int]:
    with open(file_name) as f:
        calorie_list = f.read()
        calorie_int_list = [sum(list(map(int, calories.split('\n')))) for calories in calorie_list.split('\n\n')]
        result_list = []
        for _ in range(number_of_elves):
            result_list.append(calorie_int_list.pop(calorie_int_list.index(max(calorie_int_list))))
        return sum(result_list)
