from collections import Counter

from bot.data.eq_questions import EQ_QUESTIONS
from bot.data.iq_questions import IQ_QUESTIONS
from bot.data.mbti_questions import MBTI_QUESTIONS
from bot.data.mbti_types import MBTI_TYPES
from bot.handlers.eq import MAX_TOTAL, eq_level
from bot.handlers.iq import calculate_iq, iq_level
from bot.handlers.mbti import build_breakdown, calculate_type


def test_calculate_type():
    scores = {"E": 3, "I": 2, "S": 1, "N": 4, "T": 5, "F": 0, "J": 2, "P": 3}
    assert calculate_type(scores) == "ENTP"


def test_calculate_type_is_always_valid():
    assert calculate_type({}) in MBTI_TYPES


def test_breakdown_percentages():
    scores = {"E": 1, "I": 4, "S": 5, "N": 0, "T": 2, "F": 3, "J": 5, "P": 0}
    lines = build_breakdown(scores).split("\n")
    assert lines[0] == "E 20% — 80% I"
    assert lines[1] == "S 100% — 0% N"


def test_calculate_iq_bounds():
    assert calculate_iq(0, 20) == 70
    assert calculate_iq(20, 20) == 145


def test_iq_levels():
    assert iq_level(145) == "Juda yuqori"
    assert iq_level(120) == "Yuqori"
    assert iq_level(100) == "O'rtacha"
    assert iq_level(80) == "O'rtachadan past"


def test_eq_levels():
    assert eq_level(MAX_TOTAL) == "Juda yuqori"
    assert eq_level(0) == "Rivojlantirish kerak"


def test_mbti_questions_are_balanced():
    counts = Counter(q["dimension"] for q in MBTI_QUESTIONS)
    assert set(counts) == {"EI", "SN", "TF", "JP"}
    assert len(set(counts.values())) == 1


def test_mbti_question_letters_match_dimension():
    for q in MBTI_QUESTIONS:
        assert {q["a"]["letter"], q["b"]["letter"]} == set(q["dimension"])


def test_iq_correct_index_is_valid():
    for q in IQ_QUESTIONS:
        assert len(q["options"]) == 4
        assert 0 <= q["correct"] <= 3


def test_eq_questions_have_all_scores():
    for q in EQ_QUESTIONS:
        scores = sorted(option["score"] for option in q["options"])
        assert scores == [1, 2, 3, 4]
