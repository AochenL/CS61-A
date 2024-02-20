HW_SOURCE_FILE=__file__
from ucb import trace

def pascal(row, column):
    """Returns a number corresponding to the value at that location
    in Pascal's Triangle.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 4 (1 3 3 1), 3rd entry
    3
    """
    "*** YOUR CODE HERE ***"
    if row == 0 and column == 0:
        return 1
    elif row < 0 or column < 0 or column > row:
        return 0
    else:
        return pascal(row - 1, column - 1) + pascal(row - 1, column)
    

def compose1(f, g):
    """"Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def repeated(f, n):
    """Return the function that computes the nth application of func (recursively!).

    >>> add_three = repeated(lambda x: x + 1, 3)
    >>> add_three(5)
    8
    >>> square = lambda x: x ** 2
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> repeated(square, 0)(5)
    5
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'repeated',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return lambda x: x
    elif n == 1:
        return f
    else:
        return compose1(f, repeated(f, n-1))
    

def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def check_eight(x):
        if x == 8:
            return 1
        else:
            return 0
    
    if x < 10:
        return check_eight(x)
    else:
        return check_eight(x % 10) + num_eights(x // 10)

# keep a log of counted index and pingpng value
ping_table = {}

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    # find if x is a multiple of 8 or contains the digit 8
    def contain_eight(x):
        if num_eights(x) != 0 or x % 8 == 0:
            return True
        else:
            return False

    '''
    # my version of solving the problem
    if n < 9:
        if n not in ping_table:
            ping_table[n] = n
        return n
    else:          
        if contain_eight(n - 1):
            if n not in ping_table:
                ping_table[n] = pingpong(n - 2)
            return ping_table[n] 
        else:
            if n not in ping_table:
                ping_table[n] = 2 * pingpong(n - 1) - pingpong(n - 2)
            return ping_table[n]
    '''

    # the version I developed after watching the hint video

    def pingpong_helper(value, index, direction, max):
        if index == max:
            return value

        if contain_eight(index + 1):
            return pingpong_helper(value + direction, index + 1, direction*(-1), max)
        else:
            return pingpong_helper(value + direction, index + 1, direction, max)
    
    return pingpong_helper(1, 1, 1, n)

