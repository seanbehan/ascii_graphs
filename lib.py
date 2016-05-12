
def barchart(lst):
    graph = ""
    for row in range(max(lst), 0, -1):
        for elem in lst:
            if elem >= row:
                graph += '|##|'
            else:
                graph += '----'
        graph += "\n"
    return graph
