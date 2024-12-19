from itertools import chain

from ..base import StrSplitSolution, answer

def step_stones(s: str) -> list[str]:
    if s == "0":
        return ["1"]

    if (line := len(s)) % 2 == 0:
        cut_line = line // 2
        return [str(int(new_stone)) for new_stone in (s[:cut_line], s[cut_line:])]

    return [str(int(s) * 2024)]


class Solution(StrSplitSolution):
    separator = " "

    @answer(239714)
    def part_1(self) -> int:
        stones = self.input

        for _ in range(25):
            stones = chain.from_iterable(map(step_stones, stones))

        return (len(list(stones)))
