class AgentConfig:
    def __init__(self, description: str, instructions: list[str], mdstrings: list[str]):
        self.description = description
        self.inst = instructions
        self.mdstrings = mdstrings

