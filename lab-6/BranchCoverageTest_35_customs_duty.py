import pytest

from customs_duty import clearance_channel, duty_rate, total_duty


@pytest.mark.parametrize(
    ("category", "origin", "expected"),
    [
        ("weapons", "US", "prohibited"),
        ("narcotics", "US", "prohibited"),
        ("electronics", "FTA", 0.10),
        ("electronics", "US", 0.20),
        ("clothing", "FTA", 0.05),
        ("clothing", "US", 0.12),
        ("books", "US", 0),
        ("furniture", "US", 0.15),
    ],
)
def test_duty_rate_branches(category, origin, expected):
    if expected == "prohibited":
        with pytest.raises(ValueError, match="prohibited item"):
            duty_rate(category, origin)
    else:
        assert duty_rate(category, origin) == expected


@pytest.mark.parametrize(
    ("category", "value", "origin", "is_gift", "expected"),
    [
        ("books", -1, "US", False, "negative"),
        ("books", 5000, "US", True, 0),
        ("electronics", 10000, "FTA", True, 500),
        ("electronics", 6000, "FTA", True, 100),
        ("electronics", 5001, "FTA", True, 50),
        ("clothing", 1000, "US", False, 0),
        ("clothing", 1001, "FTA", False, 50.05),
        ("books", 1, "US", False, 0),
        ("electronics", 1000, "US", False, 0),
    ],
)
def test_total_duty_branches(category, value, origin, is_gift, expected):
    if expected == "negative":
        with pytest.raises(ValueError, match="negative value"):
            total_duty(category, value, origin, is_gift)
    else:
        assert total_duty(category, value, origin, is_gift) == pytest.approx(expected)


@pytest.mark.parametrize(
    ("value", "category", "has_documents", "expected"),
    [
        (1, "weapons", True, "refuse"),
        (1, "books", True, "green"),
        (100000, "books", True, "green"),
        (100001, "books", True, "inspect"),
        (20000, "books", False, "green"),
        (20001, "books", False, "inspect"),
        (20001, "books", True, "green"),
    ],
)
def test_clearance_channel_branches(value, category, has_documents, expected):
    assert clearance_channel(value, category, has_documents) == expected
