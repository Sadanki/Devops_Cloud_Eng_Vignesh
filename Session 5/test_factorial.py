import pytest

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_positive():
    assert factorial(5) == 120

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_invalid_input():
    with pytest.raises(TypeError):
        factorial("not a number")
    with pytest.raises(TypeError):
        factorial(4.2)

def test_factorial_user_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')
    assert factorial(int(input("Enter a non-negative integer: "))) == 120

if __name__ == "__main__":
    pytest.main()
