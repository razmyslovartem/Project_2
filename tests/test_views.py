# test_processing.py
"""Тест функций модуля views"""

from src.airplanes import Aeroplane
from src.views import (filter_aeroplanes, get_aeroplanes_by_altitude, get_top_aeroplanes, load_aeroplanes_by_country,
                       sort_aeroplanes)


def test_load_aeroplanes_by_country():
    """Тест загрузки самолетов по стране с пустым аргументом"""
    # Arrange
    country = ""

    # Act
    result = load_aeroplanes_by_country(country)

    # Assert
    assert isinstance(result, list)
    assert len(result) == 0


def test_filter_aeroplanes(fix_list_aeroplanes):
    """Тест фильтрации самолетов по странам"""
    # Arrange
    countries = ["Saudi Arabia"]

    # Act
    result = filter_aeroplanes(fix_list_aeroplanes, countries)

    # Assert
    assert isinstance(result, list)
    assert len(result) == 1

    plane = result[0]
    assert isinstance(plane, Aeroplane)
    assert plane.reg_country == "Saudi Arabia"
    assert plane.callsign == "FAD437"


def test_get_aeroplanes_by_altitude(fix_list_aeroplanes):
    """Тест получения самолетов по высоте с пустым аргументом"""
    # Arrange
    altitude_filter = ""

    # Act
    result = get_aeroplanes_by_altitude(fix_list_aeroplanes, altitude_filter)

    # Assert
    assert isinstance(result, list)
    assert len(result) == 3


def test_sort_aeroplanes(fix_list_aeroplanes):
    """Тест сортировки самолетов"""
    # Arrange
    # fix_list_aeroplanes уже подготовлен фикстурой

    # Act
    result = sort_aeroplanes(fix_list_aeroplanes)

    # Assert
    assert isinstance(result, list)
    assert len(result) == 3
    assert result[0].reg_country == "Bahrain"


def test_get_top_aeroplanes(fix_list_aeroplanes):
    """Тест получения топ N самолетов"""
    # Arrange
    limit = 2

    # Act
    result = get_top_aeroplanes(fix_list_aeroplanes, limit)

    # Assert
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0].reg_country == "United Arab Emirates"
