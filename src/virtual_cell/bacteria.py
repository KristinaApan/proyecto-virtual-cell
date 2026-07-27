class Bacteria:
    def __init__(
            self,
            species: str,
            position: tuple[float, float],
            size: float,
            dry_mass: float,
            age: float,
            atp: float,
            health: float,
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
        self.healf = health               # 0.0 - 1.0
        self.alive = alive