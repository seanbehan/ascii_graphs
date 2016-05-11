# -*- coding: utf-8 -*-

def barchart(lst=[], empty_space=' ', marker='#'):
    graph = ""
    for row in range(max(lst), 0, -1):
        for elem in lst:
            if elem >= row:
                graph += marker
            else:
                graph += empty_space
        graph += "\n"
    return graph
