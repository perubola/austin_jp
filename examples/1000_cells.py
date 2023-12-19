from culture import culture

test_1000 = culture(num_cells = 1000, m_crit = 10, gr = 0.5, k=1)
test_1000.visualize()

test_1000.sigmoid_grow(2, 40)
test_1000.visualize()