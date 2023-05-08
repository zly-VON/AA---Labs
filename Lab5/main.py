import time
from floyd import floyd
from dijkstra import dijkstra
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from graphs import generate_graph, generate_complete_graph


def exec_alg(graph):
    
    start_time = time.perf_counter()
    floyd(graph)
    floyd_time.append(round(time.perf_counter() - start_time, 5))

    start_time = time.perf_counter()
    for node in graph.nodes():
        dijkstra(graph, node)
    dijkstra_time.append(round(time.perf_counter() - start_time, 5))


def exec_info(case):

    if case == 0: 
        print('\n100-node Graph')
        table = PrettyTable(['Name/Edges', '4950', '3712', '2475', '1237', '618'])
    elif case == 1: 
        print('\n300-node Graph')
        table = PrettyTable(['Name/Edges', '44850', '33637', '22425', '11212', '5606'])
    table.add_row(['Floyd', floyd_time[0], floyd_time[1], floyd_time[2], floyd_time[3], floyd_time[4]])
    table.add_row(['Dijkstra', dijkstra_time[0], dijkstra_time[1], dijkstra_time[2], dijkstra_time[3], dijkstra_time[4]])
    print(table)

    plt.plot(edges_count, floyd_time, label='Floyd')
    plt.plot(edges_count, dijkstra_time, label='Dijkstra')
    plt.xlabel('n Edges')
    plt.ylabel('Time (s)')
    if case == 0: plt.title('100-node Graph')
    elif case == 1: plt.title('300-node Graph')
    plt.legend()
    plt.show()


floyd_time = []
dijkstra_time = []

g_max = generate_complete_graph(100)
g_1 = generate_graph(100, 3712)
g_2 = generate_graph(100, 2475)
g_3 = generate_graph(100, 1237)
g_4 = generate_graph(100, 618)

edges_count = [4950, 3712, 2475, 1237, 618]

exec_alg(g_max)
exec_alg(g_1)
exec_alg(g_2)
exec_alg(g_3)
exec_alg(g_4)
exec_info(0)

floyd_time.clear()
dijkstra_time.clear()

g_max = generate_complete_graph(300)
g_1 = generate_graph(300, 33637)
g_2 = generate_graph(300, 22425)
g_3 = generate_graph(300, 11212)
g_4 = generate_graph(300, 5606)

edges_count = [44850, 33637, 22425, 11212, 5606]

exec_alg(g_max)
exec_alg(g_1)
exec_alg(g_2)
exec_alg(g_3)
exec_alg(g_4)
exec_info(1)