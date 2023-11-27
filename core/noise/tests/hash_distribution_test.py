# Allows code to be run in root directory
import sys
sys.path[0] = sys.path[0].removesuffix('\\core\\noise\\tests')

# Actual file
from core.noise.rng import RNG

def run_hash_distribution_test(num_buckets, iterations, seed):
    # Test
    buckets = { i : 0 for i in range(num_buckets) }
    rng = RNG(seed)
    for i in range(iterations):
        buckets[rng.next() % num_buckets] += 1
    
    expected = iterations / num_buckets
    percent_diff = [int(100 * buckets[i] / expected + 0.5) - 100 for i in range(num_buckets)]

    # Display
    s = f'Buckets by difference to expected outcome:\n'

    # Title of table
    for i in range(num_buckets):
        s = f'{s}{str(i).rjust(2).center(4)}|'
    s = f'{s}\n'

    # Bar of table
    for i in range(num_buckets):
        text = '-' * 4
        s = f'{s}{text}|'
    s = f'{s}\n'

    # Percents of table
    for diff in percent_diff:
        sign = '+' if diff > 0 else ''
        text = f'{sign}{diff}%'.center(4)
        s = f'{s}{text}|'

    print(s)

# Runs the tests
run_hash_distribution_test(
    num_buckets=20,
    iterations=100000,
    seed=2,
)