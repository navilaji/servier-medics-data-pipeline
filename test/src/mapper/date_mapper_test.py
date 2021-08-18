import pytest
from src.mapper.date_mapper import date_mapper

def test_date_pattern_matching():
    assert date_mapper.match_pattern("2020-01-01","%Y-%m-%d")==True
    assert date_mapper.match_pattern("2020-01-01","%Y/%m/%d")==False
    assert date_mapper.match_pattern("01/03/2020","%d/%m/%Y")==True
    assert date_mapper.match_pattern("1 january 2002","%d %B %Y")==True
    assert date_mapper.match_pattern("13 june 1999","%d %B %Y")==True
    assert date_mapper.match_pattern("june 11 1999","%d %B %Y")==False
    assert date_mapper.match_pattern(None,"%d %B %Y")==False

def test_date_parsing():
    assert date_mapper.map_to_date("2020-01-01")=="2020-01-01"
    assert date_mapper.map_to_date("01/02/2021")=="2021-02-01"
    assert date_mapper.map_to_date("21 August 2019")=="2019-08-21"
    assert date_mapper.map_to_date(None)==None

def test_date_parsing_exception():
    with pytest.raises(Exception):
        date_mapper.map_to_date("2021/04/20")
    with pytest.raises(Exception):
        date_mapper.map_to_date("04-20-2019")

