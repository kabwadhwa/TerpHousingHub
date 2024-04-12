import pytest
import TerpHousingHub
from TerpHousingHub import Property

def test_property():
    apt = Property("5721 63rd ave College Park, MD, 20740", False, "email 123rentals@gmail.com for applications")
    assert isinstance(apt, Property)

def test_add_rating():
    apt = Property("5721 63rd ave College Park, MD, 20740", False, "email 123rentals@gmail.com for applications")
    apt.add_rating(5)
    assert (apt.ratings[0] == 5)

def test_avg_rating():
    apt = Property("5721 63rd ave College Park, MD, 20740", False, "email 123rentals@gmail.com for applications")
    apt.add_rating(5)
    apt.add_rating(3)
    assert (apt.avg_rating == 4)

def test_find_listing():
    apt = Property("5721 63rd ave College Park, MD, 20740", False, "email 123rentals@gmail.com for applications")
    assert(find_listing("5721 63rd ave College Park, MD, 20740") == apt)

def test_add_listing():
    list_housing = [Property("5721 63rd ave College Park, MD, 20740", False, "email 123rentals@gmail.com for applications")]
    add_listing("8520 Regents Drive College Park, MD 20740", True, "apply on umd.housing.com")
    assert (len(terpHousing.Housing) == 2)

