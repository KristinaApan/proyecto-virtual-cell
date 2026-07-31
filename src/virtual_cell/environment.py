from dataclasses import dataclass, field


ABSOLUTE_ZERO_C = -273.15
MIN_PH = 0.0
MAX_PH = 14.0


@dataclass(slots=True)
class Environment:
    """Represent the physicochemical environment of the simulation.

    Attributes:
        temperature: Medium temperature in degrees Celsius (°C).
        ph: Medium pH.
        volume: Medium volume in liters (L).
        nutrients: Nutrient concentrations in millimoles per liter (mmol/L).
    """

    temperature: float = 37.0
    ph: float = 7.0
    volume: float = 1.0
    nutrients: dict[str, float] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate environment parameters."""
        if (
            not isinstance(self.temperature, (int, float))
            or isinstance(self.temperature, bool)
        ):
            raise TypeError("temperature must be a number.")

        if self.temperature < ABSOLUTE_ZERO_C:
            raise ValueError(
                "temperature cannot be below absolute zero "
                f"({ABSOLUTE_ZERO_C} °C)."
            )
        
        if (
            not isinstance(self.ph, (int, float))
            or isinstance(self.ph, bool)
        ):
            raise TypeError("ph must be a number.")

        # This simulation targets conventional microbiological culture media.
        # Therefore, pH values are restricted to the practical range
        # [0.0, 14.0]. This is a modeling decision rather than a universal
        # physical constraint.
        if not MIN_PH <= self.ph <= MAX_PH:
            raise ValueError(
                f"ph must be between {MIN_PH} and {MAX_PH}."
            )

        if (
            not isinstance(self.volume, (int, float))
            or isinstance(self.volume, bool)
        ):
            raise TypeError("volume must be a number.")

        if self.volume <= 0:
            raise ValueError("volume must be greater than zero.")

        if not isinstance(self.nutrients, dict):
            raise TypeError("nutrients must be a dictionary.")

        for name, concentration in self.nutrients.items():
            if not isinstance(name, str):
                raise TypeError("nutrient names must be strings.")

            if not name.strip():
                raise ValueError("nutrient names cannot be empty.")

            if (
                not isinstance(concentration, (int, float))
                or isinstance(concentration, bool)
            ):
                raise TypeError(
                    "nutrient concentrations must be numbers."
                )

            if concentration < 0:
                raise ValueError(
                    "nutrient concentrations cannot be negative."
                )