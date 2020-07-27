import os,sys
sys.path.append(os.getcwd())
from vowelscount import vowelscount
import pytest


@pytest.mark.parametrize('n, result',[
	("mallowd", 2),
	("parAmetrize", 5),
	("spacecraftCalcIum", 5)
])
def test_vowelscount(n, result):
    assert vowelscount(n) == result