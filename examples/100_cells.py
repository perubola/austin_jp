from culture import culture

test_100 = culture(num_cells = 100, m_crit = 10, gr = 0.5, k=0.2)
# 0.2 gives log-normal
test_100.viz_distr()

test_100.sigmoid_grow(2, 20)
test_100.viz_distr()