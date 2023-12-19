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

    def grow(self, steps: int):
        for _ in tqdm(range(steps)):
            self.mass_array += self.gr + np.random.randn(1)

            div_cells = self.mass_array >= self.m_crit
            for j in np.where(div_cells)[0]:
                self.mass_array[j] /= 2
                self.mass_array = np.append(self.mass_array, self.mass_array[j])

            self.area_array = np.power(self.mass_array, (2/3))
            self.num_cells = len(self.mass_array)

    def sigmoid_grow(self, noise_strength, steps):
        """More sophisticated growth function
        noise_strength: controls spread of the noise
        steps: time steps"""
        def sigmoid(x):
            return 1 / (1 + np.exp(-self.k * (x - self.m_crit)))
        for _ in tqdm(range(steps)):
            noisy_gr = self.gr + np.random.normal(0, noise_strength, self.mass_array.shape)
            # NOTE: I have no clue if making this an abs is valid 
            self.mass_array = np.abs(self.mass_array + noisy_gr)

            div_prob = sigmoid(self.mass_array)
            for j, prob in enumerate(div_prob):
                if np.random.rand() < prob:
                    self.mass_array[j] /= 2
                    self.mass_array = np.append(self.mass_array, self.mass_array[j])

            
        self.area_array = np.power(self.mass_array, (2/3))
        self.num_cells = len(self.mass_array)
        print(self.num_cells)
                

    def visualize(self):
        """
        Plots histograms of the mass and area of the cell in normal and log distributions
        """
        
        mass_bins = int(np.sqrt(len(self.mass_array))) 
        area_bins = int(np.sqrt(len(self.area_array)))
        plt.subplot(2,2,1)
        plt.hist(self.mass_array, bins = mass_bins)
        plt.axvline(x=self.m_crit,color='r', linestyle='dotted')
        plt.title('Mass Distribution')
        
        plt.subplot(2,2,2)
        plt.hist(np.log(self.mass_array), bins = mass_bins)
        plt.axvline(x=np.log(self.m_crit), color='r', linestyle='dotted')
        plt.xlim(0, np.max(np.log(self.mass_array)))
        # plt.xscale('log')
        plt.title('log-mass Distribution')

        plt.subplot(2,2,3)
        plt.hist(self.area_array, bins = area_bins)
        plt.title('Area Distribution')

        plt.subplot(2,2,4)
        plt.title('log-area Distribution')
        # plt.xscale('log')
        plt.hist(np.log(self.area_array), bins = area_bins)
        plt.xlim(0, np.max(np.log(self.area_array)))

        plt.suptitle(f"Num Cells: {self.num_cells}, $M_c$: {self.m_crit}, $\kappa$: {self.k}")
        plt.show()






