class Bacteria:
    """Represent a single bacterial cell in the simulation."""
    def __init__(
            self,
            species: str,
            position: tuple[float, float],
            size: float,
            dry_mass: float,
            age: float,
            atp: float,
            stress_level: float,
            alive: bool = True,

    ):

        self.species = species

        # Spatial information
        self.position = position

       # Physical properties
        self.size = size                  # µm
        self.dry_mass = dry_mass          # pg (picograms)

       # Biological state
        self.age = age                    # seconds
        self.atp = atp                    # ATP pool
        self.stress_level = stress_level  # 0.0 - 1.0          
        self.alive = alive                



    def update(self, dt: float):
        """Update the bacterium state.

        Parameters
        ----------
        dt : float
        Time step in seconds.
        """
        if not self.alive:
            return
 
        self.age += dt   