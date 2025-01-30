"""Any qualities that will apply universally to Energy are to be included in this module."""


class Energy:
    """
    Base class to handle the amount of energy
    Quantity is going to be Watts (Joules/sec) per meter^2 for solar
    and joules/gram for biochemical.
    """

    def __init__(self, quantity: int, quality: int):
        self.quantity = quantity
        self.quality = quality
        # Quality describes what percentage is making it to the organism that needs it.
        # We want this to be variable. Is it cloudy? Is the geothermal energy moving through
        # air or water etc.
        # What's the bioavailability of a consumed energy?

    def define_quantity(self):
        """Return the definitions to be used for
        quantity so they can be found easily elsewhere"""
        return """
        The quantity is the amount of energy that is present for use in whatever form. Sometimes this will be 
        solar energy. For the classes inheriting for solar you'll want how much energy is available per unit time per
        area of coverage. For biochemical energy this will be the energy content per unit weight of the organism that's being
        consumed. I think consistency in units of the subclasses will be more important than consisntency in units here. So energy per
        unit weight being used to describe biochemical energy irrespective of the creature is more important than some broad definition at
        this level.
        """

    def define_quality(self):
        """Return the definitions to be used for
        quality so they can be found easily elsewhere"""
        return """
        The quality describes the percentage of energy that's available for use. This needs to stand apart because energy is going to be used for
        a few things other than its presence down the line.
        """
