from data_statistics import DataStatistics


class DataCapture():
    """
    DataCapture class is used to capture and store integer values in a fixed-size array.
    It provides methods to add integer values and build statistics based on the stored data.

    Attributes:
        numbers (List[int]): A list to store the counts of integer values at their respective indices.
    """

    def __init__(self) -> None:
        """
        Initialize a DataCapture object with a fixed-size array to store integer values.
        The array has a size of 1000, representing values from 0 to 999.
        """
        self.numbers = [0] * 1000

    def add(self, number: int) -> None:
        """
        Add an integer value to the storage array.

        Args:
            number (int): The integer value to be added.

        Raises:
            TypeError: If the input value is not an integer.
            ValueError: If the input value is not in the range [0, 999].
        """
        if not isinstance(number, int):
            raise TypeError("Value is not integer")

        if number < 0 or number >= 1000:
            raise ValueError("Value must be positive and less than 1000")

        self.numbers[number] += 1

    def build_stats(self):
        """
        Build statistics based on the stored data and return a DataStatistics object.

        Returns:
            DataStatistics: An instance of the DataStatistics class containing statistics
            for the stored data.
        """
        return DataStatistics(self.numbers)
