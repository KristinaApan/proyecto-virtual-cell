
from dataclasses import dataclass


@dataclass(slots=True)
class Bacteria: 
   """Represent a single bacterial cell in the simulation."""

   # Identification
   species: str

   # Spatial information
   position: tuple[float, float]

   # Physical properties
   size: float
   dry_mass: float

   # Physiological state
   age: float
   atp: float
   stress_level: float
   alive: bool = True


   def __post_init__(self) -> None:
       """Validate the initial state of the bacterial cell."""

 
       # Identification
       if not self.species.strip():
           raise ValueError("species cannot be empty")


       # Spatial information
       if not isinstance(self.position, tuple):
           raise TypeError("position must be a tuple")


       if len(self.position) != 2:
           raise ValueError("position must contain two coordinates")


       if not all(isinstance(v, (int, float)) for v in self.position):
           raise TypeError("position coordinates must be numeric")
       

       # Physical properties 
       if self.size <= 0:
           raise ValueError("size must be greater than zero")

       if self.dry_mass <= 0:
           raise ValueError("dry_mass must be greater than zero")


       # Physiological state 
       if self.age < 0:
           raise ValueError("age cannot be negative")

       if self.atp < 0: 
           raise ValueError("atp cannot be negative")


       if not 0.0 <= self.stress_level <= 1.0:
           raise ValueError("stress_level must be between 0.0 and 1.0")


   def update(self, dt: float) -> None:
       """Advance the bacterial state by dt units of simulation time."""

       if dt < 0:
           raise ValueError("dt cannot be negative")

       if not self.alive or dt == 0:
           return

       self.age += dt
    


       