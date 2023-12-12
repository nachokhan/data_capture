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


def test_greater_method_1():
    capture = DataCapture()
    capture.add(3)
    capture.add(2)
    capture.add(1)
    stats = capture.build_stats()

    assert stats.greater(1) == 2


def test_greater_method_2():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()

    assert stats.greater(4) == 2


def test_between_method_1():
    capture = DataCapture()
    capture.add(1)
    capture.add(2)
    capture.add(3)
    capture.add(4)
    capture.add(5)
    stats = capture.build_stats()

    assert stats.between(2, 4) == 3


def test_between_method_2():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()

    assert stats.between(3, 6) == 4


def test_invalid_input_gteq_1000():
    capture = DataCapture()
    with pytest.raises(ValueError):
        capture.add(1000)


def test_invalid_input_negative():
    capture = DataCapture()
    with pytest.raises(ValueError):
        capture.add(-1)


def test_invalid_input_string():
    capture = DataCapture()
    with pytest.raises(TypeError):
        capture.add("hello world")


def test_invalid_input_float():
    capture = DataCapture()
    with pytest.raises(TypeError):
        capture.add(4.56)
