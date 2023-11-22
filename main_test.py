import pytest
from main import (in_meters_per_second, reaction_distance, braking_distance, stopping_distance, safety_distance_meter,
                  safety_distance_seconds)


def test_in_meters_per_second():
    assert in_meters_per_second(72) == pytest.approx(20)


def test_reaction_distance():
    assert reaction_distance(20) == pytest.approx(28.8,0.01)


def test_braking_distance_dry():
    assert braking_distance(20, True) == pytest.approx(28.57, 0.01)


def test_braking_distance_wet():
    assert braking_distance(20, False) == pytest.approx(50, 0.01)


def test_stopping_distance_dry():
    assert stopping_distance(72, True) == pytest.approx(57.37, 0.01)


def test_stopping_distance_wet():
    assert stopping_distance(72, False) == pytest.approx(78.8, 0.01)


def test_safety_distance_meter():
    assert safety_distance_meter(72, True) == pytest.approx(57.14,0.01)


def test_safety_distance_seconds():
    assert safety_distance_seconds(72, True) == pytest.approx(2.857, 0.001)
