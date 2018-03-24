# -*- coding: utf-8 -*-

"""Графы заданы списками смежности"""

class Graph(dict):
    def __init__(self, nodes, edges):
        for n in nodes:
            self[n] = set() # Множества для неповторяющихся элементов
        if edges == None: # Если все вершины в графе не имеют связей
            pass
        else:
            for e in edges:
                self.add_edge(e)

    def add_edge(self, edge):
        # edge содержит два node,
        # поэтому к вершине A
        # добавим вершину B и наоборот
        self[edge[0]].add(edge[1])
        self[edge[1]].add(edge[0])

    def add_node(self, node):
        self[node] = set()

    def __str__(self):
        string = ''
        for key in self.keys():
            string += str(key)
            for item in self[key]:
                 string += '->' + str(item)
            string += '\n'
        return string

    def BFS(self, s):
        # Начинаем обход с вершины s
        visited = [False for _ in range(len(self.items()))]
        queue = [s]
        visited[s] = True

        while queue:
            # Пока очередь не пуста продолжаем обход

            s = queue.pop(0) # Извлекаем вершину
            print(s)

            for w in self[s]:
                # Проанализируем каждую вершину
                if visited[w] == False:
                    queue.append(w)
                    visited[w] = True

    def DFS(self, s):
        # Начинаем обход с вершины s
        visited = [False for _ in range(len(self.items()))]
        stack = [s]
        visited[s] = True

        while stack:
            # Пока стэк не пуст продолжаем обход

            s = stack.pop()
            print(s)

            for w in self[s]:
                # Проанализируем каждую вершину
                if visited[w] == False:
                    stack.append(w)
                    visited[w] = True
