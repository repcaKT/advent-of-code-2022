from typing import Dict, List
from abc import ABC, abstractmethod
import dataclasses

class Shape(ABC):
    @property
    @abstractmethod
    def score(self):
        pass
    
    @property
    @abstractmethod
    def class_affinity(self):
        pass

    def fight(self, oponent_name: str):
        return self.class_affinity[oponent_name]

class Rock(Shape):
    score = 1
    class_affinity = {"Paper":"Lose", "Rock": "Draw", "Scissors": "Win"}

class Paper(Shape):
    score = 2
    class_affinity = {"Paper":"Draw", "Rock": "Win", "Scissors": "Lose"}

class Scissors(Shape):
    score = 3
    class_affinity = {"Paper":"Win", "Rock": "Lose", "Scissors": "Draw"}


RPS_DICT = {"A": "Rock", "X": Rock, "B":"Paper", "Y":Paper, "C":"Scissors", "Z":Scissors}
MATCH_SCORE = {"Win": 6, "Draw": 3, "Lose": 0}

def read_rps_matches(file_name: str):
     with open(file_name) as f:
        match_file_list = f.readlines()
        match_list = [match.replace("\n", "").split(" ") for match in match_file_list]
        return match_list

def count_score(match_list: List[List[str]]):
    score = 0
    for match in match_list:
        oponent_figure = RPS_DICT[match[0]]
        fighting_figure = RPS_DICT[match[1]]()
        score = score + MATCH_SCORE[fighting_figure.fight(oponent_figure)] + fighting_figure.score
    return score

current_matches = read_rps_matches("day-two/input_data.txt")
obtaiened_score = count_score(current_matches)
print(obtaiened_score)