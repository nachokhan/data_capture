

from typing import List


class DataStatistics():
    """
    DataStatistics class calculates statistics for a given list of data.
    It provides methods to find the number of elements less than, greater than,
    or between given numbers within the data.

    Attributes:
        _greater (List): A list to store the cumulative count of elements greater than each index.
        _less (List): A list to store the cumulative count of elements less than each index.
        _data (List): The input data for which statistics are calculated.
    """

    def __init__(self, data: List) -> None:
        """
        Initialize a DataStatistics object with the input data.

        Args:
            data (List): The list of data for which statistics will be calculated.
        """

        self._greater: List = []
        self._less: List = []
        self._data = data

        self._update_stats(data)

    def less(self, number) -> int:
        """
        Calculate the number of elements less than the given number.

        Args:
            number: The target number.

        Returns:
            int: The count of elements less than the target number.
        """
        self._check_number(number)
        return self._less[number]

    def greater(self, number) -> int:
        """
        Calculate the number of elements greater than the given number.

        Args:
            number: The target number.

        Returns:
            int: The count of elements greater than the target number.
        """

        self._check_number(number)
        return self._greater[number]

    def between(self, n1, n2) -> int:
        """
        Calculate the number of elements between two given numbers.

        Args:
            n1: The lower bound.
            n2: The upper bound.

        Returns:
            int: The count of elements between the lower and upper bounds.
        """

        self._check_number(n1)
        self._check_number(n2)
        out_of_range = self.greater(n2) + self.less(n1)
        return self._greater[0] - out_of_range

    def _check_number(self, number):
        """
        Check if the input number is within the valid index range.

        Args:
            number: The input number.

        Raises:
            ValueError: If the input number is out of range.
        """

        if not (0 <= number < len(self._data)):
            raise ValueError()

    def _update_stats(self, data: List) -> None:
        """
        Update the cumulative counts of elements less and greater than each index.

        Args:
            data (List): The input data for which statistics will be updated.
        """

        self._less = self._generate_cumulative_sum(data)
        self._greater = self._generate_cumulative_sum(data[::-1])[::-1]

    def _generate_cumulative_sum(self, data) -> List:
        """
        Generate the cumulative sum of elements in the input data.

        Args:
            data: The input data.

        Returns:
            List: A list of cumulative sums.
        """

        cum_sum_data = []
        cum_sum_data.append(0)
        for n in range(1, len(data)):
            cum_sum_data.append(cum_sum_data[n-1] + data[n-1])
        return cum_sum_data
