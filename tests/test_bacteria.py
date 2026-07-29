"""
Unit tests for the Bacteria class.

These tests verify that bacterial objects are created correctly
and that their initial state matches the expected values.
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



@pytest.mark.parametrize("species", ["", " ", "   ", "\t", "\n"])
def test_bacteria_raises_error_for_invalid_species(species):
    with pytest.raises(ValueError):
        make_bacteria(species=species)