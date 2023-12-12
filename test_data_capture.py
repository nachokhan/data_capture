import pytest
from data_capture import DataCapture
from data_statistics import DataStatistics

def test_add_data():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    assert isinstance(stats, DataStatistics), "build_stats should return a DataStatistics instance"

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
        capture.add("5")

def test_invalid_input_float():
    capture = DataCapture()
    with pytest.raises(TypeError):
        capture.add(4.56)

def test_empty_capture():
    capture = DataCapture()
    stats = capture.build_stats()
    assert stats.less(1) == 0
    assert stats.greater(999) == 0
    assert stats.between(1, 999) == 0

def test_single_element_capture():
    capture = DataCapture()
    capture.add(500)
    stats = capture.build_stats()
    assert stats.less(500) == 0
    assert stats.greater(500) == 0
    assert stats.between(500, 500) == 1
