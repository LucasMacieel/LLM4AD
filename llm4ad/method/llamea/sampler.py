class LLaMEASampler:
    def __init__(self, llm):
        self.llm = llm
        self.draw_samples = self.llm.query
