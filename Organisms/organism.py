"""Generalizeable information about organisms goes here"""

import random


class Organism:
    """An over-arching class for handling organisms.
    Specifics to be handled in child classes
    """

    def __init__(self, trait_dict: dict, alive: bool = True):
        self.alive = alive
        self.trait_dict = trait_dict

    def mutate(self, target_trait, mutation_rate: float = 0.01):
        """Mutate a trait so that it's different in subsequent generations."""
        mutating_trait = self.trait_dict[target_trait]
        if isinstance(mutating_trait, float):
            increase_decrease = random.choice(["increase", "decrease"])
            if increase_decrease == "increase":
                mutating_trait = mutating_trait + (mutation_rate * mutating_trait)
            elif increase_decrease == "decrease":
                mutating_trait = mutating_trait - (mutation_rate * mutating_trait)
        elif isinstance(mutating_trait, bool):
            should_flip = mutation_rate > random.random()
            if should_flip:
                mutating_trait = not mutating_trait

        self.trait_dict[target_trait] = mutating_trait

    def mutate_all_traits(self, mutation_rate: float = 0.01):
        """Mutate all of the traits in the trait dictionary"""
        trait_list = list(self.trait_dict.keys)
        for trait in trait_list:
            self.mutate(target_trait=trait, mutation_rate=mutation_rate)

    def sexual_reproduction(self):
        """Create an offspring of the organism in question"""

    def asexual_reproduction(self):
        """Create a copy of the organism in question"""
