import numpy as np

class culture:
    """
    holds n cells and evolves them over time 
    """
    def __init__(
            self,
            num_cells: int,
            m_crit: float, 
            gr: float, # growth rate from 0 to 1
            k: float = 3, # steepness of the sigmoid, try around 3 for now
    ):
        self.num_cells = num_cells
        self.m_crit = m_crit
        # assume mean mass of 5 units 
        self.mass_array = 10*np.abs(np.random.randn(num_cells))  # stores cell mass 
        # area is proportional to m ^ (2/3)
        self.area_array = np.power(self.mass_array, (2/3))/10  # array storing cell area
        # p = 1/(1+exp[-k(m-mc)])
        self.prob_array = 1/(1+np.exp(-k*(self.mass_array - m_crit)))




