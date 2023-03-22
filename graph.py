# Python3 Program to print breadth_first_search traversal
# from a given source vertex. breadth_first_search(int s)
# traverses vertices reachable from s.

# This class represents a directed graph
# using adjacency list representation


class Graph:

   # Constructor
   def __init__(self):

      # default dictionary to store graph
      self.graph = {}

   # function to add an edge to graph
   def add_edge(self, u, v):
      if not u in self.graph:
         self.graph[u] = [v]
      else:
         self.graph[u].append(v)

   def get_num_nodes(self):
      unique_nodes = {}
      for u in self.graph:
         unique_nodes[u] = 1
         for v in self.graph[u]:
            unique_nodes[v] = 1
      return max(self.graph)+1

   def cycle_from(self, start):
      num_nodes = self.get_num_nodes()

      visited = [False] * (num_nodes)
      stack = []
      stack.append(start)
      visited[start] = True
      while stack:
         node = stack.pop()
         adjacency = self.graph[node]
         for n in adjacency:
            if n == start:
               return True
            if not visited[n]:
               stack.append(n)
               visited[n] = True
      return False
   
   def is_cyclic(self):
      for start in self.graph:
         cycle = self.cycle_from(start)
         if cycle:
            return True
      return False

   def shortest_path(self, start, end):
      prev = {}
      visited = [False] * (max(self.graph) + 1)
      queue = []
      queue.append(start)
      visited[start] = True

      while queue:
         parent = queue.pop(0)
         neighbores = self.graph[parent]
         for node in neighbores:
            if not visited[node]:
               visited[node] = True
               prev[node] = parent
               queue.append(node)

      path = []
      node = end
      path.append(node)
      while not start in path:
         path.append(prev[node])
         node = prev[node]

      path.reverse()
      return path

   def breadth_first_search(self, s):
      '''
      Function to print a breadth_first_search of graph
      '''
      # Mark all the vertices as not visited
      visited = [False] * (max(self.graph) + 1)

      # Create a queue for breadth_first_search
      queue = []

      # Mark the source node as
      # visited and enqueue it
      queue.append(s)
      visited[s] = True

      while queue:

         # Dequeue a vertex from
         # queue and print it
         s = queue.pop(0)
         print(s, end=" ")

         # Get all adjacent vertices of the
         # dequeued vertex s. If a adjacent
         # has not been visited, then mark it
         # visited and enqueue it
         for i in self.graph[s]:
            if visited[i] == False:
               queue.append(i)
               visited[i] = True


if __name__ == '__main__':
   # Create a graph given in the above diagram
   g = Graph()
   g.add_edge(0,1)
   g.add_edge(0,2)
   g.add_edge(2,3)
   g.add_edge(1,3)
   g.add_edge(3,4)
   g.add_edge(4,1)

print(g.is_cyclic())
