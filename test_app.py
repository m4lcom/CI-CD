def suma(a, b):
    return a + b

def resta(a, b):
    return a - b


def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0.3, 0.7) == 1


def test_resta():
    assert resta(5, 2) == 3
    assert resta(1, 1) == 0
    assert resta(-3, 31) == -4

def test_multiplicacion():
    assert multiplicacion(2, 3) == 6
    assert multiplicacion(6, 4) == 24
    





