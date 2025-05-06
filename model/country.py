class Country:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __hash__(self):
        return hash(self.code)

    def __eq__(self, other):
        return self.code == other.code


