import pytest
from freezegun import freeze_time
from test import generate_week_schedule


@pytest.mark.parametrize('days_ahead, tz, expected_len', [
    (1, 'Europe/Helsinki', 1),
    (7, 'Europe/Helsinki', 7),
    (0, 'Europe/Helsinki', 0),
    (14, 'UTC', 14),
])
def test_generate_week_schedule_positive_lengths(days_ahead, tz, expected_len):
    result = generate_week_schedule(days_ahead=days_ahead, tz=tz)
    assert len(result) == expected_len


@freeze_time('2023-10-23')
@pytest.mark.parametrize('day_idx, expected_tuple', [
    (0, ('Mo', '23/10', '00:05–22:55')),
    (5, ('Sa', '28/10', 'Closed')),
    (6, ('Su', '29/10', 'Closed')),
])
def test_generate_week_schedule_logic(day_idx, expected_tuple):
    schedule = generate_week_schedule(days_ahead=7)
    assert schedule[day_idx] == expected_tuple


@pytest.mark.parametrize('days_ahead', [
    -1,
    -100
])
def test_generate_week_schedule_negative_days(days_ahead):
    result = generate_week_schedule(days_ahead=days_ahead)
    assert result == []


@pytest.mark.parametrize('invalid_tz', [
    'Invalid/Zone',
    '',
    'GMT+99'
])
def test_generate_week_schedule_invalid_tz(invalid_tz):
    with pytest.raises(Exception):
        generate_week_schedule(tz=invalid_tz)
