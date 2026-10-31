import pytest

from customs_duty import clearance_channel, duty_rate, total_duty


def test_duty_rate_covers_prohibited_and_all_categories():
    with pytest.raises(ValueError, match="prohibited item"):
        duty_rate("weapons", "US")
    assert duty_rate("electronics", "FTA") == 0.10
    assert duty_rate("electronics", "US") == 0.20
    assert duty_rate("clothing", "FTA") == 0.05
    assert duty_rate("clothing", "US") == 0.12
    assert duty_rate("books", "US") == 0
    assert duty_rate("furniture", "US") == 0.15


def test_total_duty_covers_validation_gift_and_non_gift_paths():
    with pytest.raises(ValueError, match="negative value"):
        total_duty("books", -1, "US", False)
    assert total_duty("books", 5000, "US", True) == 0
    assert total_duty("electronics", 6000, "FTA", True) == 100
    assert total_duty("electronics", 5001, "FTA", True) == 50
    assert total_duty("clothing", 1500, "FTA", False) == 75
    assert total_duty("books", 1000, "US", False) == 0


def test_clearance_channel_covers_every_return():
    assert clearance_channel(1, "weapons", True) == "refuse"
    assert clearance_channel(100001, "books", True) == "inspect"
    assert clearance_channel(20001, "books", False) == "inspect"
    assert clearance_channel(20000, "books", False) == "green"
