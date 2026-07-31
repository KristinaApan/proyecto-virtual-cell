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


def test_environment_accepts_custom_ph() -> None:
    environment = Environment(ph=6.5)

    assert environment.ph == 6.5


@pytest.mark.parametrize(
    "invalid_ph",
    [
        "7",
        None,
        True,
        False,
        [],
        {},
        (),
    ]
)
def test_environment_rejects_invalid_ph_type(
    invalid_ph,
) -> None:
    with pytest.raises(TypeError):
        Environment(ph=invalid_ph)


@pytest.mark.parametrize(
    "invalid_ph",
    [
        -1.0,
        14.1,
        20.0,
    ]
)
def test_environment_rejects_invalid_ph_value(
    invalid_ph,
) ->None:
    with pytest.raises(ValueError):
        Environment(ph=invalid_ph)


def test_environment_accepts_custom_volume() -> None:
    environment = Environment(volume=2.5)

    assert environment.volume == 2.5


@pytest.mark.parametrize(
    "invalid_volume",
    [
        "1.0",
        None,
        True,
        False,
        [],
        {},
        (),
    ],
)
def test_environment_rejects_invalid_volume_type(
    invalid_volume,
) -> None:
    with pytest.raises(TypeError):
        Environment(volume=invalid_volume)


@pytest.mark.parametrize(
    "invalid_volume",
    [
        0.0,
        -1.0,
        -10.5,
    ],
)
def test_environment_rejects_invalid_volume(
    invalid_volume,
) -> None:
    with pytest.raises(ValueError):
        Environment(volume=invalid_volume)



