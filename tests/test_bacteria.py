"""
Unit tests for the Bacteria class.

These tests verify object creation, input validation,
and the behavior of the update() method.
"""

import pytest

from virtual_cell.bacteria import Bacteria


def make_bacteria(**kwargs) -> Bacteria:
    """Create a valid Bacteria instance with optional overrides."""
    data = {
        "species": "E. coli",
        "position": (0.0, 0.0),
        "size": 1.0,
        "dry_mass": 0.5,
        "age": 0.0,
        "atp": 100.0,
        "stress_level": 0.0,
        "alive": True,
    }
    data.update(kwargs)
    return Bacteria(**data)


# ---------------------------------------------------------------------
# Creation
# ---------------------------------------------------------------------

def test_bacteria_creation():
    bacteria = make_bacteria()

    assert bacteria.species == "E. coli"
    assert bacteria.position == (0.0, 0.0)
    assert bacteria.size == 1.0
    assert bacteria.dry_mass == 0.5
    assert bacteria.age == 0.0
    assert bacteria.atp == 100.0
    assert bacteria.stress_level == 0.0
    assert bacteria.alive is True


# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------

@pytest.mark.parametrize("species", ["", " ", "   ", "\t", "\n"])
def test_bacteria_raises_error_for_invalid_species(species):
    with pytest.raises(ValueError):
        make_bacteria(species=species)


def test_bacteria_raises_error_when_position_is_not_tuple():
    with pytest.raises(TypeError):
        make_bacteria(position=[0.0, 0.0])


@pytest.mark.parametrize(
    "position",
    [
        (),
        (0.0,),
        (0.0, 0.0, 0.0),
    ],
)
def test_bacteria_raises_error_when_position_has_invalid_length(position):
    with pytest.raises(ValueError):
        make_bacteria(position=position)


@pytest.mark.parametrize(
    "position",
    [
        ("x", 0.0),
        (0.0, "y"),
        ("x", "y"),
    ],
)
def test_bacteria_raises_error_when_position_contains_non_numeric_values(position):
    with pytest.raises(TypeError):
        make_bacteria(position=position)


@pytest.mark.parametrize("size", [0.0, -1.0, -10.0])
def test_bacteria_raises_error_when_size_is_not_positive(size):
    with pytest.raises(ValueError):
        make_bacteria(size=size)


@pytest.mark.parametrize("dry_mass", [0.0, -0.1, -5.0])
def test_bacteria_raises_error_when_dry_mass_is_not_positive(dry_mass):
    with pytest.raises(ValueError):
        make_bacteria(dry_mass=dry_mass)


@pytest.mark.parametrize("age", [-0.1, -1.0])
def test_bacteria_raises_error_when_age_is_negative(age):
    with pytest.raises(ValueError):
        make_bacteria(age=age)


@pytest.mark.parametrize("atp", [-0.1, -10.0])
def test_bacteria_raises_error_when_atp_is_negative(atp):
    with pytest.raises(ValueError):
        make_bacteria(atp=atp)


@pytest.mark.parametrize("stress_level", [-0.1, 1.1, 2.0])
def test_bacteria_raises_error_when_stress_level_is_out_of_range(stress_level):
    with pytest.raises(ValueError):
        make_bacteria(stress_level=stress_level)


@pytest.mark.parametrize("stress_level", [0.0, 1.0])
def test_bacteria_accepts_boundary_stress_level(stress_level):
    bacteria = make_bacteria(stress_level=stress_level)
    assert bacteria.stress_level == stress_level


# ---------------------------------------------------------------------
# Update
# ---------------------------------------------------------------------

def test_update_increases_age():
    bacteria = make_bacteria(age=1.0)

    bacteria.update(2.5)

    assert bacteria.age == 3.5


def test_update_with_zero_dt_does_not_change_age():
    bacteria = make_bacteria(age=5.0)

    bacteria.update(0.0)

    assert bacteria.age == 5.0


def test_update_on_dead_bacteria_does_not_change_age():
    bacteria = make_bacteria(age=5.0, alive=False)

    bacteria.update(2.0)

    assert bacteria.age == 5.0


def test_update_raises_error_when_dt_is_negative():
    bacteria = make_bacteria()

    with pytest.raises(ValueError):
        bacteria.update(-1.0)


@pytest.mark.parametrize(
    "invalid_dt",
    [
        "1.0",
        None,
        [],
        {},
    ],
)
def test_update_raises_type_error_when_dt_is_not_numeric(invalid_dt):
    bacteria = make_bacteria()

    with pytest.raises(TypeError):
        bacteria.update(invalid_dt)