import pytest
from hasbalancedparantheses import fun_hasbalancedparantheses
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('a, result', [
    ("( ( ( ( )3))  ", False), ("( ( ( ( )3)))  ", True),
    ("( ( ( ( ( )3)))  ", False),
    (") ) ", False), ("  ", True), (" (  )  ", True)
])
def test_fun_hasbalancedparantheses(a, result):
    assert fun_hasbalancedparantheses(a) == result
