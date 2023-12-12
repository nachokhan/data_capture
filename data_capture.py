from data_statistics import DataStatistics


class DataCapture():

    def __init__(self) -> None:
        self.numbers = [0] * 1000

    def add(self, number: int) -> None:
        if not isinstance(number, int):
            raise TypeError("Value is not integer")

        if number < 0 or number >= 1000:
            raise ValueError("Value must be positive and less than 1000")

        self.numbers[number] += 1

    def build_stats(self):
        return DataStatistics(self.numbers)
