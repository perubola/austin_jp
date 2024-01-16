from culture import culture

test_1000 = culture(num_cells = 1000, m_crit = 10, gr = 1, k=1)
test_1000.viz_distr()

test_1000.sigmoid_grow(2, 30)
test_1000.viz_distr()