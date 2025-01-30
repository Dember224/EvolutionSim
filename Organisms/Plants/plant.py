"""This module houses the plant behavior."""

from Organisms.organism import Organism


class Plant(Organism):
    """A parent class to define general plant behavior"""

    def __init__(self, alive=True):
        super().__init__(alive)
