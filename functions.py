
# Author: Taylor C. Powell



# ++ ---------------------------- MATH FUNCTIONS ----------------------------- ++


# FUNCTION: factorial(int x)
#
# Calculates the factorial of x
# 
# INPUT: an integer value x
# OUTPUT: the factorial of x
#
# FORMULA: x! = x * (x - 1) * (x - 2) * ... * 3 * 2 * 1
#
def factorial(x):
    if (x == 0):
        return 1
    else:
        output = 1
        for i in range(1, x + 1):
            output *= i
        return output



# ++ ------------------------ PROBABILITY FUNCTIONS ------------------------- ++


## FUNCTION: combination(int n, int r) 
#
# Calculates the number of combinations of n items taken r at a time
#
# INPUT: two integer values n and r
# OUTPUT: the number of combinations of n items taken r at a time
#
# FORMULA: C(n, r) = n! / (r! * (n - r)!)
#
def combination(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


## FUNCTION: binomial_pmf(float p_of_success, int n_trials, int x_val)
#
# Calculates the probability mass function (PMF) of a binomial distribution
#
# INPUT: three values: p_of_success (float), n_trials (int), and x_val (int)
# OUTPUT: the PMF of the binomial distribution
#
# FORMULA: PMF(x) = C(n, x) * p^x * (1 - p)^(n - x)
#   where C(n, x) is the number of combinations of n items taken x at a time,
#   p is the probability of success, and n is the number of trials
#
def binomial_pmf(p_of_success, n_trials, x_val):
    if not (0 <= p_of_success <= 1):
        raise ValueError("p_of_success must be between 0 and 1.")
    return combination(n_trials, x_val) * (p_of_success ** x_val) * ((1 - p_of_success) ** (n_trials - x_val))


## FUNCTION: dist_binomial_cdf(float p_of_success, int n_trials, int x_val)
#
# Calculates the cumulative distribution function (CDF) of a binomial distribution
#
# INPUT: three values: p_of_success (float), n_trials (int), and x_val (int)
# OUTPUT: the CDF of the binomial distribution
#
# FORMULA: CDF(x) = sum from i=0 to x of C(n, i) * p^i * (1 - p)^(n - i)
#   where C(n, i) is the number of combinations of n items taken i at a time,
def binomial_cdf(p_of_success, n_trials, x_val):
    if x_val < 0:
        raise ValueError("x_val must be non-negative")
    output = 0
    for i in range(0, x_val + 1):
        output += binomial_pmf(p_of_success, n_trials, i)
    return output


def hypergeometric_pdf(N1, N2, n, x):
    """
    Calculates the probability of drawing x successes in a hypergeometric distribution.

    Parameters:
    N1 (int): Number of successes in the population.
    N2 (int): Number of failures in the population.
    n (int): Number of draws.
    x (int): Number of successes in the draws.

    Returns:
    float: Probability of drawing x successes.
    """
    if not all(isinstance(i, int) and i >= 0 for i in [N1, N2, n, x]):
        raise ValueError("All inputs must be non-negative integers.")
    if x > n:
        raise ValueError("x must be less than or equal to n.")
    if n > N1 + N2:
        raise ValueError("n must be less than or equal to N1 + N2.")
    
    return (combination(N1, x) * combination(N2, n - x)) / combination(N1 + N2, n)



# ++ ------------ SANDBOX ------------ ++


# Replace 'None' as needed
to_console = (binomial_cdf(0.5, 3, 2) * binomial_cdf(0.5, 5, 5)) + (binomial_cdf(0.5, 3, 3) * binomial_cdf(0.5, 5, 4))

print(
    to_console
)
