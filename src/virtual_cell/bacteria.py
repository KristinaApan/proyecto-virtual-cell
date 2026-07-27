class Bacteria:
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

        # Spatial information:

        self.position = position

       # Physical properties:

        self.size = size                   # µm
        self.dry_mass = dry_mass           # pg (picograms)
    

       # Biological state:

        self.age = age                    # seconds
        self.atp = atp                    # ATP pool
        self.stress_level = stress_level            
        self.alive = alive