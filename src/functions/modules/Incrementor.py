class Incrementor:
    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter += 1
            
    def get(self):
        return self.counter 