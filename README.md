# austin_jp
Code for junior paper under supervision of Bob Austin

## Cell Growth Simulation
Simulates the growth of cells through their cell cycle via a sigmoid probability function. 
<p align="center">
    <img width="600" height="450" src="assets\100cells_lognormal.png"
</p>

## Quick example
```python
from culture import culture 

cult = culture(num_cells = 100, m_crit = 10, gr = 0.5, k=0.2)
cult.visualize()

# use sigmoid_grow for more probabilistic model
cult.sigmoid_grow(noise_strength=1, steps=20)  
cult.visualize()
```