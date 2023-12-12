import pytest
from data_capture import DataCapture
from data_statistics import DataStatistics

def test_build_stats():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    assert isinstance(stats, DataStatistics), "build_stats should return a DataStatistics instance"

def test_less_method():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    assert stats.less(4) == 2

def test_greater_method():
    capture = DataCapture()
    capture.add(3)
    capture.add(2)
    capture.add(1)
    stats = capture.build_stats()
    assert stats.greater(1) == 2

def test_between_method():
    capture = DataCapture()
    capture.add(1)
    capture.add(2)
    capture.add(3)
    capture.add(4)
    capture.add(5)
    stats = capture.build_stats()
    assert stats.between(2, 4) == 3

def test_max_value():
    capture = DataCapture()
    capture.add(999)
    stats = capture.build_stats()

    with pytest.raises(ValueError):
        assert stats.less(1000) == 1

    assert stats.greater(998) == 1
    assert stats.between(999, 999) == 1

def test_min_value():
    capture = DataCapture()
    capture.add(1)
    stats = capture.build_stats()
    assert stats.less(2) == 1
    assert stats.greater(0) == 1
    assert stats.between(1, 1) == 1

def test_random_values():
    capture = DataCapture()
    values = [10, 20, 30, 40, 50]
    for value in values:
        capture.add(value)
    stats = capture.build_stats()
    assert stats.less(15) == 1
    assert stats.greater(45) == 1
    assert stats.between(20, 40) == 3
