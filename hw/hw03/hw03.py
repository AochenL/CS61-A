HW_SOURCE_FILE=__file__
import math
from ucb import trace


def composer(func=lambda x: x):
    """
    Returns two functions -
    one holding the composed function so far, and another
    that can create further composed problems.
    >>> add_one = lambda x: x + 1
    >>> mul_two = lambda x: x * 2
    >>> f, func_adder = composer()
    >>> f1, func_adder = func_adder(add_one)
    >>> f1(3)
    4
    >>> f2, func_adder = func_adder(mul_two)
    >>> f2(3) # should be 1 + (2*3) = 7
    7
    >>> f3, func_adder = func_adder(add_one)
    >>> f3(3) # should be 1 + (2 * (3 + 1)) = 9
    9
    """
    # reference https://github.com/PKUFlyingPig/CS61A/blob/master/hws/hw03/hw03.py
    def func_adder(g):
        "*** YOUR CODE HERE ***"
        h = lambda x: func(g(x))
        return composer(h)
    return func, func_adder


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)


def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> # ban recursion
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***" 
    
        #g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)
        # g(4) = g(3) + 2*g(2) + 3*g(1) 
        # g(5) = g(4) + 2*g(3) + 3*g(2)

    #summary: while recursion goes backwards, iteration moves forwards.
    g_1, g_2, g_3 = 1, 2, 3
    g_n = n
    while (n - 3) > 0:
        g_n = g_3 + 2 * g_2 + 3 * g_1
        g_3, g_2, g_1 = g_n, g_3, g_2
        n -= 1
    return g_n


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 9:
        return 0
    else:
        last_digit = n % 10
        last_two_digit = (n // 10) % 10
        missing_nums = last_digit - last_two_digit - 1
        if missing_nums < 0:
            missing_nums = 0
        return missing_nums + missing_digits(n // 10)


def count_change(total):
    """Return the number of ways to make change for total.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_change', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    
    # determine whether x is a power of 2
    def is_power_of_two(x):
        return (math.ceil(math.log(x, 2)) == math.floor(math.log(x, 2)))

    # find the maximum number that is not greater than x 
    # and is a power of 2
    def max_power_of_two(x):
        if is_power_of_two(x):
            return x
        else:
            return max_power_of_two(x - 1)

    # return the ways of partitioning n using parts up to m
    # while m is a power of 2
    def count_helper(n, m):
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif m <= 0:
            return 0
        else:
            with_m = count_helper(n - m, m)
            without_m = count_helper(n, m // 2)
            return with_m + without_m
    
    return count_helper(total, max_power_of_two(total))    


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2 
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3 
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    # reference: https://www.mathsisfun.com/games/towerofhanoi.html

    # The strategy used in Towers of Hanoi is 
    # to move all but the bottom disc to the second peg, 
    # then moving the bottom disc to the third peg, 
    # then moving all but the second disc from the second to the third peg.

    if n == 1:
        print_move(start, end)
        return 
    mid = 6 - start - end
    move_stack(n - 1, start, mid)
    print_move(start, end)
    move_stack(n - 1, mid, end)
   

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return lambda n: 1 if n == 1 else lambda 

