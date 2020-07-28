import pytest
from longestsubpalindromes import fun_longestsubpalindromes
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('a, result', [
    ("abcba", "abcba"), ("ab-4-be!!!", "b-4-b"),
    ("abba", "abba"), ("abcbce", "cbc")
])
def test_fun_longestsubpalindromes(a, result):
    assert fun_longestsubpalindromes(a) == result