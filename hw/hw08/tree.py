def bigs(t):
    """return the number of nodes that are greater than all their ancestors
    >>> a = Tree(1, [Tree (4, [Tree (4), Tree (5)]), Tree(3, [Tree (0, [Tree (2) ])])])
    >>> bigs(a)
    4
    """
    def f(a, x):
        if x.label > a:
            return 1 + sum([f(x.label, b) for b in x.branches])
        else:
            return sum([f(a, b) for b in x.branches])
    return f(-float("inf"), t)

class Tree:
    def __init__(self, label, branches=[]):
        for branch in branches:
            assert isinstance(branch, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

def smalls(t):
    """return the non-leaf nodes in t that are smaller than all their descendants.
    >>> a = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(6)])])])
    >>> sorted([t.label for t in smalls(a)])
    [0, 2]
    """
    result = []
    def process(t):
        """find smallest label in t & maybe add t to result"""
        nonlocal result
        if t.is_leaf():
            return t.label
        smallest_of_branches = min([process(b) for b in t.branches])
        if t.label < smallest_of_branches:
            result.append(t)
            return t.label
        else:
            return smallest_of_branches
    process(t)
    return result
        

