

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

        self._data = data
        self._less, self._greater = self._generate_cumulative_sum(data)

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

    def _generate_cumulative_sum(self, data) -> List:
        """
        Generate two lists representing the cumulative sum of elements in the input data for calculations
        of 'less than' and 'greater than' statistics. 

        The method iterates through the input list 'data' once. For each element at index 'n', it updates
        the cumulative sum for elements 'less than' the current index and 'greater than' the corresponding
        reverse index (values-n-1).

        This approach allows for efficient calculation of cumulative sums in a single pass through the data,
        ensuring linear complexity both in terms of time and space.

        Args:
            data: The input data, a list of integers.

        Returns:
            tuple: A tuple containing two lists - the first list ('cum_less') contains the cumulative sum
            of elements less than each index, and the second list ('cum_greater') contains the cumulative
            sum of elements greater than each reverse index.
        """
        values = len(data)

        cum_less = [0] * values
        cum_greater = [0] * values

        total_less = 0
        total_greater = 0

        for n in range(0, values):
            cum_less[n] = total_less
            cum_greater[values-n-1] = total_greater
            total_less += data[n]
            total_greater += data[values-n-1]

        return cum_less, cum_greater
