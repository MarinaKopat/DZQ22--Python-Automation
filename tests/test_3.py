def format_price(price: str) -> str:
    try:
        price_float = float(price)
        # добавить проверку обрабатать знак отдельно
        price_str = f"{price_float:.2f}"
        integer_part, decimal_part = price_str.split(".")
        formatted_parts = []
        for i in range(len(integer_part), 0, -3):
            start = max(0, i - 3)
            formatted_parts.insert(0, integer_part[start:i])
        return " ".join(formatted_parts) + "." + decimal_part
    except (ValueError, AttributeError):   # нет TypeError
        return price
import pytest
@pytest.mark.parametrize('input_value, expected_output', [
    ('1234', '1 234.00'),
    ('1234567.8', '1 234 567.80'),
    ('99.999', '100.00'),
    ('-1234', '-1 234.00'),
])

def test_format_price_positive(input_value, expected_output):
    assert format_price(input_value) == expected_output

@pytest.mark.parametrize('input_value, expected_output', [
    ('abc', 'abc'),
    (None, None),
    ([], []),
    ('', ''),
])
def test_format_price_negative(input_value, expected_output):
    assert format_price(input_value) == expected_output
