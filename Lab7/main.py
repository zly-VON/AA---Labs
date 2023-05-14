import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable

from Prim import prim
from Kruskal import kruskal
from graph import generate_complete_graph


def minimum_spanning_tree(nodes_count):
    prim_time = []
    kruskal_time = []

    for nodes in nodes_count:
        graph = generate_complete_graph(nodes)

        start_time = time.perf_counter()
        prim(graph)
        prim_time.append(round(time.perf_counter() - start_time, 5))

        start_time = time.perf_counter()
        kruskal(graph)
        kruskal_time.append(round(time.perf_counter() - start_time, 5))

    table = PrettyTable(['Name/Nodes', '100', '300', '500', '700', '900', '1100', '1300', '1500'])
    table.add_row(['Prim', prim_time[0], prim_time[1], prim_time[2], prim_time[3], prim_time[4], prim_time[5], prim_time[6], prim_time[7]])
    table.add_row(['Kruskal', kruskal_time[0], kruskal_time[1], kruskal_time[2], kruskal_time[3], kruskal_time[4], kruskal_time[5], kruskal_time[6], kruskal_time[7]])
    print(table)
    
    plt.plot(nodes_count, prim_time, label='Prim')
    plt.plot(nodes_count, kruskal_time, label='Kruskal')
    plt.xlabel('n-th Digit')
    plt.ylabel('Time (s)')
    plt.title('Minimum Spanning Tree')
    plt.legend()
    plt.show()


nodes = [100, 300, 500, 700, 900, 1100, 1300, 1500]
minimum_spanning_tree(nodes)
