import Even_or_Odd

import pytest

@pytest.mark.parametrize("a, Res", [(3, True), (6, True), (10, True), (14, True), (17, True), (18, True), (22, True)])

def test_Even_or_Odd(a, Res):

    Result = Even_or_Odd.Check_Even_or_Odd(a)

    assert Result == Res