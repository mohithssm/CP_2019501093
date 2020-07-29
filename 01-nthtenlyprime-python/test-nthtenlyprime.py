import os,sys
sys.path.append(os.getcwd())
from nthtenlyprime import fun_nthtenlyprime
import pytest


@pytest.mark.parametrize('a, result',[
    (0,19),(1, 37),(4, 127), (10, 523), (15, 1009),  (20, 1423),  (25, 2053)
])
def test_fun_nthtenlyprime(a, result):
    assert fun_nthtenlyprime(a) == result
