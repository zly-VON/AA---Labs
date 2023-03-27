from tree import balanced_tree, unbalanced_tree
from graphviz import Digraph


def plot(tree, name):
    dot = Digraph()

    for node in tree:
        dot.node(str(node))
                 
    for parent, children in tree.items():
        for child in children:
            dot.edge(str(parent), str(child))

    dot.render(name, format='png')


plot(balanced_tree(), 'balanced_tree')
plot(unbalanced_tree(), 'unbalanced_tree')