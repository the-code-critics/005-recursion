"""
Some examples on how to use recursion to play with tree structured data.
In this case a phylogenetic tree - or more accurately a cladogram
https://evolution.berkeley.edu/evolibrary/article/phylogenetics_02
"""

tree = [[[['Human', 'Chimpanzee'], 'Gorilla'], 'Orangutan'], 'Gibbon']


def print_tree(tree, level=0):
    if isinstance(tree, list):
        for subtree in tree:
            print_tree(subtree, level + 1)
    else:
        indent = ' ' * (level - 1) * 3
        print(indent + tree)


def print_clades(tree):
    if isinstance(tree, list):
        for subtree in tree:
            print_clades(subtree)
        print(tree)


def print_species(tree):
    if isinstance(tree, list):
        for subtree in tree:
            print_species(subtree)
    else:
        print(tree)


def depth(species, tree, level=0):
    if species == tree:
        return level
    if isinstance(tree, list):
        return max(depth(species, t, level + 1) for t in tree)
    return -1


def distance(species1, species2, tree):
    return abs(depth(species1, tree) - depth(species2, tree))


print_clades(tree)
print_species(tree)
print_tree(tree)
print(depth('Gibbon', tree))
print(distance('Human', 'Gorilla', tree))
