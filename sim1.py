import numpy as np
import matplotlib.pyplot as plt 
from tqdm import tqdm 

class culture:
    """
    holds n cells and evolves them over time 
    """
    def __init__(
            self,
            num_cells: int,
            m_crit: float, 
            gr: float, # growth rate, units of mass units/sec
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
        # might not need it
        # self.prob_array = 1/(1+np.exp(-k*(self.mass_array - m_crit)))

    def grow(self, steps: int):
        for _ in tqdm(range(steps)):
            self.mass_array += self.gr + np.random.randn(1)

            div_cells = self.mass_array >= self.m_crit
            for j in np.where(div_cells)[0]:
                self.mass_array[j] /= 2
                self.mass_array = np.append(self.mass_array, self.mass_array[j])

            self.area_array = np.power(self.mass_array, (2/3))
            self.num_cells = len(self.mass_array)
                

    def visualize(self):
        """
        Plots histograms of the mass and area of the cell in normal and log distributions
        """
        mass_bins = int(np.sqrt(len(self.mass_array))) 
        area_bins = int(np.sqrt(len(self.area_array)))
        plt.subplot(2,2,1)
        plt.hist(self.mass_array, bins = mass_bins)
        plt.title('Mass Distribution')
        
        plt.subplot(2,2,2)
        plt.hist(self.mass_array, bins = mass_bins)
        plt.xscale('log')
        plt.title('log-mass Distribution')

        plt.subplot(2,2,3)
        plt.hist(self.area_array, bins = area_bins)
        plt.title('Area Distribution')

        plt.subplot(2,2,4)
        plt.title('log-area Distribution')
        plt.xscale('log')
        plt.hist(self.area_array, bins = area_bins)
        plt.show()






