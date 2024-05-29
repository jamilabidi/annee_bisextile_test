from leap_year import leap
import pytest

def test_year_by400():
    assert leap(2000) == "LEAP"

@pytest.mark.parametrize(
    "year",[1700,1800,1900,2100]
)
def test_year_by100_NotBy400(year):
    assert leap(year) == "NOPE"


def test_year_by4_NotBy100():
    assert leap(2008) == "LEAP"
    assert leap(2012) == "LEAP"
    assert leap(2016) == "LEAP"

def test_year_Notby4():
    assert leap(2017) == "NOPE"
    assert leap(2018) == "NOPE"
    assert leap(2019) == "NOPE"