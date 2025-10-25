import random
import math


def exponential_generator(l):
    u = random.uniform(0, 1)
    return -math.log(u) / l


sample_size = 300
l = 0.0144
samples = [exponential_generator(l) for _ in range(sample_size)]