import os,sys
sys.path.append(os.getcwd())
from vowelscount import vowelscount
import pytest


@pytest.mark.parametrize('n, result',[
	("mallowd", 2),
	("parametrize", 5),
	("spacecraft", 3)
])
def test_vowelscount(n, result):
    assert vowelscount(n) == result