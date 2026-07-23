def theoretical_wait(lam, mu):
    """M/M/1 average time in system (minutes)."""
    if lam >= mu:
        return float('inf')  # unstable, queue grows forever
    return 1 / (mu - lam) # implements average wait time formula: W = 1/(lambda - mu)


if __name__ == "__main__":
    print(theoretical_wait(1.6, 2))   # should print 2.5
    print(theoretical_wait(1.9, 2))   # should print 10.0 
    print(theoretical_wait(2.0, 2))   # should print inf — unstable