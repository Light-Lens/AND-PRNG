import matplotlib.pyplot as plt
import random, math, os

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

my_rng, python_rng = [], []
rng = AND()
for _ in range(100):
    print(rng.gen())

    python_rng.append(random.uniform(0, 1))
    my_rng.append(rng.x)

plt.style.use('ggplot')
plt.figure(figsize=(18, 7))
plt.title("Pseudorandom numbers", fontsize=16)

plt.plot(my_rng, label="AND algorithm")
plt.plot(python_rng, label="Python's random module")

plt.xlabel("Iteration", fontsize=12)
plt.ylabel("Value", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

plt.legend(fontsize=12)
plt.show()
