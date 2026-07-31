import pytest

from virtual_cell.environment import Environment


def test_environment_creation() -> None:
    environment = Environment()

    assert environment.temperature == 37.0
    assert environment.ph == 7.0
    assert environment.volume == 1.0
    assert environment.nutrients == {}


def test_environment_accepts_custom_temperature() -> None:
    environment = Environment(temperature=25.0)

    assert environment.temperature == 25.0


@pytest.mark.parametrize(
    "invalid_temperature",
    [
        "37",
        None,
        True,
        False,
        [],
        {},
        (),
    ],
)
def test_environment_rejects_invalid_temperature_type(
    invalid_temperature,
) -> None:
    with pytest.raises(TypeError):
        Environment(temperature=invalid_temperature)


def test_environment_rejects_temperature_below_absolute_zero() -> None:
    with pytest.raises(ValueError):
        Environment(temperature=-300.0)