import os

class AND:
    def __init__(self, x=0.1):
        self.x = x
        self.p = self.seed()

    # Read system entropy from /dev/urandom (Unix/Linux) or os.urandom (cross-platform)
    def seed(self):
        entropy = os.urandom(4)  # Read 4 bytes of entropy for a 32-bit seed
        seed = int.from_bytes(entropy, byteorder='big') / (2**32)  # Convert to a float in [0, 1)
        return seed

    def gen(self, m=1):
        self.x = (self.p * self.x + (self.x - 1)) % m
        return self.x

if __name__ == "__main__":
    rng = AND()
    for _ in range(100):
        print(rng.gen())
