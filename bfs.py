
visited = [] # visited nodes
queue = []   # queue

def bredth_first_search(start, end, neighbor_function):
  """

  :param start:
  :param end:
  :param neighbor_function:
  :return: bfs from start to end
  """
  visited.append(start)
  queue.append(start)
  current = start
  while queue and current != end:
    current = queue.pop(0)

    for neighbor in neighbor_function(current):
      if neighbor not in visited:
        visited.append(neighbor)
        queue.append(neighbor)
  if (current == end):
    return queue
  else:
    print("no path")
