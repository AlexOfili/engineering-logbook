def theoretical_wait(lam, mu):
    """M/M/1 average time in system (minutes)."""
    if lam >= mu:
        return float('inf')  # unstable, queue grows forever
    return 1 / (mu - lam) # implements average wait time formula: W = 1/(lambda - mu)


if __name__ == "__main__":
    print(theoretical_wait(1.6, 2))   # should print 2.5
    print(theoretical_wait(1.9, 2))   # should print 10.0 
    print(theoretical_wait(2.0, 2))   # should print inf — unstable




import random

def simulate(lam, mu, customers=10000):
    t = 0.0           # current shopper's arrival time 
    till_free = 0.0    # when the till becomes free next
    total = 0.0        # running total of time in system, across all shoppers

    for _ in range(customers):
        t += random.expovariate(lam)         # next arrival
        start = max(t, till_free)            # can't start before arriving OR before till is free
        till_free = start + random.expovariate(mu)  # till is busy until service ends
        total += till_free - t               # time in system = finish - arrival

    return total / customers

if __name__ == "__main__":
    print(f"{'arrival rate':>14} {'theoretical wait':>17} {'simulated wait':>15}")  # right-aligning text
    for lam in [1.0, 1.4, 1.6, 1.8, 1.9]:
        theory = round(theoretical_wait(lam, 2), 2)
        sim = round(simulate(lam, 2), 2)       # results aren't exactly the same because of randomness (noise)
        print(f"{lam:>14} {theory:>17} {sim:>15}")      