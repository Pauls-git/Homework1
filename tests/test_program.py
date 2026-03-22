from program import (
    savings,
    self_consumption,
    yearly_pv_generation,
)


def test_yearly_pv_generation() -> None:
    assert yearly_pv_generation(5, 1000) == 5000


def test_self_consumption() -> None:
    assert self_consumption(5000, 0.4) == 2000


def test_savings() -> None:
    assert savings(2000, 0.30) == 600
