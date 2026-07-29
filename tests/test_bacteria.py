"""
Unit tests for the Bacteria class.

These tests verify that bacterial objects are created correctly
and that their initial state matches the expected values.
"""

import pytest

from virtual_cell.bacteria import Bacteria


def test_bacteria_creation():

    # Arrange
    species = "E. coli"
    position = (0.0, 0.0)
    size = 1.5
    dry_mass = 0.35
    age = 0.0
    atp = 100.0 
    stress_level = 0.0

    # Act
    bacteria = Bacteria(
        species=species,
        position=position,
        size=size,
        dry_mass=dry_mass,
        age=age,
        atp=atp,
        stress_level=stress_level,
    )

    # Assert
    assert bacteria.species == species
    assert bacteria.position == position
    assert bacteria.size == size
    assert bacteria.dry_mass == dry_mass
    assert bacteria.age == age
    assert bacteria.atp == atp
    assert bacteria.stress_level == stress_level
    assert bacteria.alive is True 



@pytest.mark.parametrize(
    "species",
    [
        "",
        " ",
        "   ",
        "\t",
        "\n",
    ],
)
def test_bacteria_raises_error_for_invalid_species(species):
    with pytest.raises(ValueError):
        Bacteria(
            species=species,
            position=(0.0, 0.0),
            size=1.0,
            dry_mass=0.5,
            age=0.0,
            atp=100.0,
            stress_level=0.0,
            alive=True,
        )