class cell:
    def __init__(
            self,
            gr: float,
            size: float,
            p_split: float, # should be between 0 and 1
            nuc_area: float,
            m_crit: float,
    ):
        self.gr = gr
        self.size = size
        self.p_split = p_split
        self.nuc_area = nuc_area
        self.m_crit = m_crit