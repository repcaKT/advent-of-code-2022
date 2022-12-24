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
    def strategy_shape(self):
        pass

    def fight(self, choosen_strategy: str):
        return self.strategy_shape[choosen_strategy]

class Rock(Shape):
    score = 1
    strategy_shape = {"Lose":"Scissors", "Draw":"Rock", "Win":"Paper"}

class Paper(Shape):
    score = 2
    strategy_shape = {"Draw":"Paper",  "Win":"Scissors",  "Lose":"Rock"}

class Scissors(Shape):
    score = 3
    strategy_shape = {"Win":"Rock", "Lose":"Paper","Draw":"Scissors"}


RPS_DICT = {"A": Rock, "B":Paper, "C":Scissors}
FIGURE_MAP = {"Rock": Rock, "Paper": Paper, "Scissors": Scissors}
STRATEGY_DICT = {"X":"Lose", "Y": "Draw", "Z":"Win"}
MATCH_SCORE = {"Win": 6, "Draw": 3, "Lose": 0}

def read_rps_matches(file_name: str):
     with open(file_name) as f:
        match_file_list = f.readlines()
        match_list = [match.replace("\n", "").split(" ") for match in match_file_list]
        return match_list

def count_score(match_list: List[List[str]]):
    score = 0
    for match in match_list:
        oponent_figure = RPS_DICT[match[0]]()
        match_strategy = STRATEGY_DICT[match[1]]
        my_figure = FIGURE_MAP[oponent_figure.fight(match_strategy)]
        score = score + MATCH_SCORE[match_strategy] + my_figure.score
    return score

current_matches = read_rps_matches("day-two/input_data.txt")
obtaiened_score = count_score(current_matches)
print(obtaiened_score)