import pytest

def test_m1():
    a = 2
    b = 3
    assert a+1  == b
    assert a != b
@pytest.mark.login
def test_m2():
    assert True

def test_m3():
    st1 = "python"
    assert st1.upper() == "PYTHON"
@pytest.mark.login
def test_login():
    assert "admin" == "admin"