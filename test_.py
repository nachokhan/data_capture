import pytest
from data_capture import DataCapture
from data_statistics import DataStatistics


def test_add_and_build_stats():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()

    assert isinstance(stats, DataStatistics), "build_stats should return a DataStatistics instance"


def test_less_method_1():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()

    assert stats.less(4) == 2


def test_less_method_2():
    capture = DataCapture()
    capture.add(3)
    capture.add(2)
    capture.add(1)
    stats = capture.build_stats()

    assert stats.less(3) == 2


def test_greater_method_2():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()

    assert stats.greater(4) == 2


def test_greater_method_1():
    capture = DataCapture()
    capture.add(3)
    capture.add(2)
    capture.add(1)
    stats = capture.build_stats()

    assert stats.greater(1) == 2

