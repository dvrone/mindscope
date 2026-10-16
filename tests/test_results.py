from bot.handlers.results import format_date


def test_format_date_converts_utc_to_tashkent():
    # Toshkent UTC+5
    assert format_date("2026-10-16 09:30:00") == "16.10.2026 14:30"


def test_format_date_crosses_midnight():
    assert format_date("2026-10-16 20:15:00") == "17.10.2026 01:15"
