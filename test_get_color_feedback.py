import pytest
from utilities import get_color_feedback

#! TEST CASES
test_cases = [
    (['crane', 'crane'], 'GGGGG'),
    (['blimp', 'crane'], 'BBBBB'),
    (['crane', 'trace'], 'YGGBG'),
    (['eerie', 'elite'], 'GBBYG'),
    (['apple', 'alley'], 'GBBYY'),
    (['level', 'lever'], 'GGGGB'),
    (['abbey', 'babes'], 'YYGGB'),
    (['llama', 'allot'], 'YGYBB'),
    (['tatty', 'taste'], 'GGBGB'),
    (['banal', 'canal'], 'BGGGG'),
    (['train', 'roast'], 'YYGBB'),
    (['green', 'gears'], 'GYYBB'),
    (['eerie', 'alley'], 'YBBBB'),
    (['teeth', 'tweet'], 'GYGYB'),
    (['sssss', 'sissy'], 'GBGGB'),
    (['tally', 'allot'], 'YYGYB'),
    (['eerie', 'cycle'], 'BBBBG'),
]

@pytest.mark.parametrize("inputs, expected", test_cases)
def test_get_color_feedback(inputs, expected):
    result = get_color_feedback(inputs[0], inputs[1])

    assert result == expected