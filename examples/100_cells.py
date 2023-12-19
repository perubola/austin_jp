from culture import culture

test_100 = culture(num_cells = 100, m_crit = 10, gr = 0.5, k=1)
test_100.visualize()

test_100.sigmoid_grow(2, 40)
test_100.visualize()