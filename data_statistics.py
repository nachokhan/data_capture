

from typing import List


class DataStatistics():

    def __init__(self, data: List) -> None:
        self._greater: List = []
        self._less: List = []

        self._update_stats(data)

    def less(self, number) -> int:
        return self._less[number]

    def greater(self, number) -> int:
        return self._greater[number]

    def _update_stats(self, data: List) -> None:
        self._less = self._generate_cumulative_sum(data)
        self._greater = self._generate_cumulative_sum(data[::-1])[::-1]

    def _generate_cumulative_sum(self, data) -> List:
        cum_sum_data = []
        cum_sum_data.append(0)
        for n in range(1, len(data)):
            cum_sum_data.append(cum_sum_data[n-1] + data[n-1])
        return cum_sum_data
