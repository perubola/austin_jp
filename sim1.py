import numpy as np
import matplotlib.pyplot as plt 
class culture:
    """
    holds n cells and evolves them over time 
    """
    def __init__(
            self,
            num_cells: int,
            m_crit: float, 
            gr: float, # growth rate, units of ___
            k: float = 3, # steepness of the sigmoid, try around 3 for now
    ):
        self.num_cells = num_cells
        self.m_crit = m_crit
        self.k = k
        self.gr = gr
        # assume mean mass of 5 units 
        self.mass_array = 10*np.abs(np.random.randn(num_cells))  # stores cell mass 
        # area is proportional to m ^ (2/3)
        self.area_array = np.power(self.mass_array, (2/3))  # array storing cell area
        # p = 1/(1+exp[-k(m-mc)])
        self.prob_array = 1/(1+np.exp(-k*(self.mass_array - m_crit)))

    def grow(self, g_t: float):
        # for i in linspace()

        return 
    def visualize(self):
        plt.subplot(2,2,1)
        plt.hist(self.mass_array)
        plt.title('Mass Distribution')
        
        plt.subplot(2,2,2)
        plt.hist(np.log(self.mass_array))
        plt.title('log-mass Distribution')

        plt.subplot(2,2,3)
        plt.hist(self.area_array)
        plt.title('Area Distribution')

        plt.subplot(2,2,4)
        plt.title('log-area Distribution')
        plt.hist(np.log(self.area_array))
        plt.show()






