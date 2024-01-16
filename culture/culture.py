import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
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

    def sigmoid_grow(self, steps):
        """More sophisticated growth function
        noise_strength: controls spread of the noise
        steps: time steps"""
        def sigmoid(x):
            return 1 / (1 + np.exp(-self.k * (x - self.m_crit)))

        mu = self.gr
        std = np.sqrt(self.gr)
        for _ in tqdm(range(steps)):
            noise = np.abs(np.random.normal(mu, std, size=self.mass_array.size))
            noisy_gr = 1 + self.gr + noise 
            self.mass_array = self.mass_array*(noisy_gr) 

            div_prob = sigmoid(self.mass_array)
            for j, prob in enumerate(div_prob):
                if np.random.rand() < prob:
                    self.mass_array[j] /= 2
                    self.mass_array = np.append(self.mass_array, self.mass_array[j])

            
        self.area_array = np.power(self.mass_array, (2/3))
        self.num_cells = len(self.mass_array)
                

    def viz_distr(self):
        """
        Plots histograms of the mass and area of the cell in normal and log distributions
        """
        mass_bins = int(np.sqrt(len(self.mass_array)))
        area_bins = int(np.sqrt(len(self.area_array)))
        plt.subplot(2,2,1)
        plt.hist(self.mass_array, bins = mass_bins)
        plt.axvline(x=self.m_crit,color='r', linestyle='dotted')
        plt.title(f"Mass Distribution, $\mu$: {np.mean(self.mass_array):.3f}")
        
        plt.subplot(2,2,2)
        plt.hist(np.log(self.mass_array), bins = mass_bins)
        plt.axvline(x=np.log(self.m_crit), color='r', linestyle='dotted')
        # plt.xlim(np.min(np.log(self.mass_array)), np.max(np.log(self.mass_array)))
        print(np.min(np.log(self.mass_array)))
        # plt.xscale('log')
        plt.title('log-mass Distribution')

        plt.subplot(2,2,3)
        plt.hist(self.area_array, bins = area_bins)
        plt.title('Area Distribution')

        plt.subplot(2,2,4)
        plt.title('log-area Distribution')
        # plt.xscale('log')
        plt.hist(np.log(self.area_array), bins = area_bins)
        # plt.xlim(0, np.max(np.log(self.area_array)))

        plt.suptitle(f"Num Cells: {self.num_cells}, $M_c$: {self.m_crit}, $\kappa$: {self.k}, gr: {self.gr}")
        plt.show()

    def gauss_gv(self, steps: int):
        """Grows culture for n steps. Plots initial versus final mass state. Plots gaussian for log-normal comparison"""
        m0 = self.mass_array
        self.sigmoid_grow(steps)
        mt = self.mass_array
        print(self.num_cells)

        fig, axs = plt.subplots(2,2,figsize=(10,10))
        bin0 = int(np.sqrt(len(m0)))
        bint = int(np.sqrt(len(mt)))

        def get_norm_gauss(data):
            mu = np.mean(data)
            std = np.std(data)
            x = np.linspace(mu - 3.5*std, mu + 3.5*std, 1000)


            gcurve = norm.pdf(x, mu, std)

            ddensity, _ = np.histogram(data, bins=int(np.sqrt(len(data))))
            peak_density = max(ddensity)


            return x, gcurve

        x, curve = get_norm_gauss(np.log(mt))
        plt.rcParams.update({'font.size': 14})


        axs[0, 0].hist(m0, bins=bin0, color='blue', alpha=0.7, density=True)
        axs[0, 0].set_title('Initial State - Linear')
        axs[0, 0].set_xlabel('Mass')
        axs[0, 0].set_ylabel('Density')

        axs[0, 1].hist(np.log(m0), color='blue', bins=bin0, alpha=0.7, density=True)
        axs[0, 1].set_title('Initial State - Log')
        axs[0, 1].set_xlabel('$\ln$Mass')
        axs[0, 1].set_ylabel('Density')

        # Plotting final state in the second row
        axs[1, 0].hist(mt, bins=bint, color='blue', alpha=0.7, density=True)
        axs[1, 0].set_title('Final State - Linear')
        axs[1, 0].set_xlabel('Mass')
        axs[1, 0].set_ylabel('Density')

        axs[1, 1].hist(np.log(mt), bins=bint, color='blue', alpha=0.7, density=True)
        axs[1, 1].set_title('Final State - Log')
        axs[1, 1].set_xlabel('$\ln$Mass')
        axs[1, 1].set_ylabel('Density')
        axs[1, 1].plot(x, curve, color = 'r')
        axs[1, 1].set_xlim(min(x), max(x))

        fig.suptitle(f'Simulated Growth Over {steps} Time Steps\n$M_c$ = {self.m_crit}, ' + r'$\langle \alpha \rangle$' + f' = {self.gr}, k = {self.k}')

        plt.tight_layout()

        plt.show()



if __name__ == "__main__":
    test_100 = culture(num_cells = 100, m_crit = 20, gr = 0.03, k=0.6)
    # 0.2 gives log-normal
    # test_100.viz_distr()

    # test_100.sigmoid_grow(30)
    # test_100.viz_distr()

    test_100.gauss_gv(40)


