class TreeNode:
    def __init__(self, node):
        self.node = node
        self.neighbors = []


def bfs(graph):

  visited = {graph.node}
  queue = collections.deque()
  queue.append(graph.neighbors)

  while queue:

    # remove first element
    node = queue.popleft()
    if node not in visited:
      visited.add(node.node)
      queue.append(node.neighbors)
    
  return visited

def dfs(graph):

  visited = {graph.node}
  queue = collections.deque()
  queue.append(graph.neighbors)

  while queue:

    # remove last element
    node = queue.pop()
    if node not in visited:
      visited.add(node.node)
      queue.append(node.neighbors)
    
  return visited
    
  
