import time
import numpy as np 
from dfs import dfs
from bfs import bfs
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from tree import balanced_tree, unbalanced_tree


def exec(tree, nodes, case):
    dfs_time = []
    bfs_time = []

    for node in nodes:
        start_time = time.perf_counter()
        dfs(tree, 1, node)
        dfs_time.append(round(time.perf_counter() - start_time, 7))
        start_time = time.perf_counter()
        bfs(tree, 1, node)
        bfs_time.append(round(time.perf_counter() - start_time, 7))

    if case == 0: 
        print('\nBalanced Tree')
        table = PrettyTable(['Name/Node', '3', '7', '11', '16', '20'])
    elif case == 1: 
        print('\nUnbalanced Tree')
        table = PrettyTable(['Name/Node', '3', '8', '10', '17', '19'])
    table.add_row(['DFS', dfs_time[0], dfs_time[1], dfs_time[2], dfs_time[3], dfs_time[4]])
    table.add_row(['BFS', bfs_time[0], bfs_time[1], bfs_time[2], bfs_time[3], bfs_time[4]])
    print(table)

    x_axis = np.arange(len(nodes))
    plt.bar(x_axis - 0.2, dfs_time, 0.4, label='DFS')
    plt.bar(x_axis + 0.2, bfs_time, 0.4, label='BFS')
    plt.xticks(x_axis, nodes)
    plt.xlabel('Node')
    plt.ylabel('Time, s')
    if case == 0: plt.title('Balanced Tree')
    elif case == 1: plt.title('Unbalanced Tree')
    plt.legend()
    plt.show()


bal_nodes = [3, 7, 11, 16, 20]
unbal_nodes = [3, 8, 10, 17, 19]
exec(balanced_tree(), bal_nodes, 0)
exec(unbalanced_tree(), unbal_nodes, 1)
