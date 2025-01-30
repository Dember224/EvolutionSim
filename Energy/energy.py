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
