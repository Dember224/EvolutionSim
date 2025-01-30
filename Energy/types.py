from typing import float, int
from energy import Energy

class Solar(Energy):
    """
    Providing life with Solar energy.
    """
    def __init__(self, quantity: float, quality: float, daytime_length: int, nighttime_length: int):
        super().__init__(quantity, quality)
        self.daytime_length = daytime_length
        self.nighttime_length = nighttime_length

    def get_energy_that_makes_it(self) -> float:
        """Energy that makes it through atmosphere to organism given conditions"""
        return self.quantity * self.quality

    def get_energy_per_day(self) -> float:
        """Daily energy per square meter"""
        return self.get_energy_that_makes_it() * (self.daytime_length * 3600)


    

class Biochemical(Energy):
    """
    Energy consumed by an organism. Carnivorous or parasitic.
    """
    def __init__(self, quantity:float, quality:float):
        super().__init__(quantity, quality)
        # Quantity is Energy per gram of organism

    def get_bioavailable_energy(self) -> float:
        """Amount of energy that does work for the organism."""
        return self.quantity * self.quality


        