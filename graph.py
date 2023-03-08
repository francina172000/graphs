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

   '''
   Function to print a breadth_first_search of graph
   '''
   def breadth_first_search(self, s):
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
   g.add_edge(0, 1)
   g.add_edge(0, 2)
   g.add_edge(1, 2)
   g.add_edge(2, 0)
   g.add_edge(2, 3)
   g.add_edge(3, 3)

   print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
   g.breadth_first_search(2)
