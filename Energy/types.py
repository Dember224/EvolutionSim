"""
This module will handle specific types of energy. For now specifically solar and biochemical.
At some point in the future this could include geothermal and others.
"""

from energy import Energy


class Solar(Energy):
    """
    Providing life with Solar energy.
    """

    def __init__(
        self,
        quantity: float,
        quality: float,
        daytime_length: int,
        nighttime_length: int,
    ):
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

    def __init__(
        self, quantity: float, quality: float, loss_rate: float, organism_weight: float
    ):
        super().__init__(quantity, quality)
        # Quantity is Energy per gram of organism
        self.loss_rate = loss_rate # grams/second loss to decay after killed
        self.organism_weight = organism_weight # In grams


    def get_total_energy(self) -> float:
        """The total amount of energy available in that organism"""
        return self.quantity * self.organism_weight

    def get_total_bioavailable_energy(self) -> float:
        """Amount of energy that does work for the organism."""
        return self.quantity * self.quality

    def get_current_energy(self, decay_time_elapsed:int = 0) -> float:
        """Amount of energy currently available for consumption"""
        food_remaining_by_mass = self.organism_weight - (self.loss_rate * decay_time_elapsed)
        energy_remaining = food_remaining_by_mass * self.quality
        return energy_remaining
