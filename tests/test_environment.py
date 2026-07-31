from virtual_cell.environment import Environment


def test_environment_creation() -> None:
    environment = Environment()

    assert environment.temperature == 37.0
    assert environment.ph == 7.0
    assert environment.volume == 1.0
    assert environment.nutrients == {}
