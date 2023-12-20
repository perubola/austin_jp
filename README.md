# austin_jp
Code for junior paper under supervision of Bob Austin

## Cell Growth Simulation
Simulates the growth of cells through their cell cycle via a sigmoid probability function. 
<p align="center">
    <img width="768" height="380" src="assets\100cells_lognormal.png"
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
## TODO
1. Make sim more realistic (add carrying capacity, cell death)
2. Fit the lognormal
3. Assuming the lognormal fits, test for what range of k it fits
