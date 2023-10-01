import decimal, os

class AND:
    def __init__(self, x=0.1, p=-1):
        """
        Initialize the AND pseudo-random number generator.

        Args:
            x (float, optional): Initial value for the generator (default is 0.1).
            p (float, optional): Parameter for the generator; if negative, it's seeded randomly (default is -1).
        """

        self.x = x
        self.p = self.seed() if (p < 0 or p > 1) else p

    def gen(self, m=1):
        """
        Generate a pseudo-random number using the AND algorithm.

        Args:
            m (float, optional): Modulus for the random number generation (default is 1).

        Returns:
            float: A pseudo-random number in the range (0, m).
        """

        self.x = (self.p * self.x + (self.x - 1)) % m
        self.middle_square_seed()
        return self.x

    def random(self):
        """
        Generate a random number by generating 10 random numbers and selecting any from it randomly.

        Returns:
            float: A random seed in the range (0, 1).
        """

        random_numbers = []
        for _ in range(10):
            random_numbers.append(self.gen())

        return random_numbers[int(self.p*10)]

    # Read system entropy from /dev/urandom (Unix/Linux) or os.urandom (cross-platform)
    def seed(self):
        """
        Generate a random seed for the 'p' parameter using system entropy.

        Returns:
            float: A random seed in the range (0, 1).
        """

        entropy = os.urandom(4)  # Read 4 bytes of entropy for a 32-bit seed
        seed = int.from_bytes(entropy, byteorder='big') / (2**32)  # Convert to a float in [0, 1]
        return seed

    def middle_square_seed(self):
        """
        Generate a random seed for the 'p' parameter using the middle square algorithm.

        Returns:
            float: A random seed in the range (0, 1).
        """

        num_digits = -decimal.Decimal(str(self.p)).as_tuple().exponent
        seed = int(self.p * 10**num_digits)

        # Square the seed
        squared = seed * seed

        # Extract the middle digits as the next random number
        squared_str = str(squared)
        middle_start = (len(squared_str) - num_digits) // 2
        middle_end = middle_start + num_digits
        random_str = squared_str[middle_start:middle_end]

        # Convert the random string back to an integer and update the seed
        seed = int(random_str)

        # Normalize the random number to be between 0 and 1
        normalized_random = seed / 10**num_digits
        self.p = normalized_random

if __name__ == "__main__":
    rng = AND()
    print(rng.random())

    # for _ in range(10):
    #     print(rng.gen())
