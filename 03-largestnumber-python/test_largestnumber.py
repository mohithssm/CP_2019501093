import pytest
from largestnumber import fun_largestnumber
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('a, result', [
    ("we have 32 dogs 3 cats", 32), ("we have dogs cats", 0),
    ("I saw 3 dogs, 17 cats, and 14 cows!", 17), ("wehave15dogs2cats", 15)
])
def test_fun_largestnumber(a, result):
    assert fun_largestnumber(a) == result