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
      queue=[]
      visited=[]
      queue.append(start)
      visited.append(start)
      l=len(queue)
      while l >0:
         ele=queue.pop(0)
         if ele in self.graph:
            x=self.graph[ele]
            for i in x:
               if i==start:
                  return True
               if i not in visited:
                  visited.append(i)
                  queue.append(i)
         l=len(queue)
      return False
      
   
   def is_cyclic(self):
      for i in self.graph:
         cycle=self.cycle_from(i)
         if cycle:
            return True
      return False

      

   def shortest_path(self, start, end):
            
            queue=[]
            visited=[]
            thisdict={}
            queue.append(start)
            visited.append(start)
            l=len(queue)
            while l >0:
               ele=queue.pop(0)
               if ele in self.graph:
                  list=[]
                  x=self.graph[ele]
                  for i in x:
                     if i not in visited:
                        visited.append(i)
                        queue.append(i)
                        list.append(i)
                        thisdict[ele]=list
               l=len(queue)
            create=[]
            create.append(end)
            def get_key_for_value_in_list(val):
               for key, value_list in thisdict.items():
                  if val in value_list:
                     return key
            l=len(create)
            while start not in create:
               v=create[l-1]
               key=get_key_for_value_in_list(v)
               create.append(key)
               l=len(create)
            create.reverse()
            return create
      
   
   def is_cyclic(self):
      for i in self.graph:
         cycle=self.cycle_from(i)
         if cycle:
            return True
      return False



      
      
      

   
   def depth_first_search(self, s,end):
      visited=[]
      queue=[]
      thisdict={}
      visited.append(s)
      queue.append(s)
      l=len(queue)
      
      while l>0:
         list=[]
         if queue[l-1] in self.graph:
             x=self.graph[queue[l-1]]
      

             for i in x:
               if(i in visited)!=1:
                  queue.append(i)
                  visited.append(i)
                  list.append(i)
                  thisdict[queue[l-1]]=list
                  break
            
             if l==len(queue):
                queue.pop(l-1)
            

             l=len(queue)
      # for i in visited:
      #    print(i,end=" ") 
      # # print(thisdict)
   
      create=[]
      create.append(end)
      def get_key_for_value_in_list(val):
         for key, value_list in thisdict.items():
            if val in value_list:
               return key
      l=len(create)
      while s not in create:
         v=create[l-1]
         key=get_key_for_value_in_list(v)
         create.append(key)
         l=len(create)
      create.reverse()
      return create
   
      
      
# dfs code is valid only for undirected graph rest 2 are for directed as well as undirected.
   
if __name__ == '__main__':
   # Create a graph given in the above diagram
   g = Graph()
   g.add_edge(0,1)
   g.add_edge(1,0)

   g.add_edge(0,2)
   g.add_edge(2,0)
   g.add_edge(2,3)
   g.add_edge(3,2)
   g.add_edge(1,3)
   g.add_edge(3,1)
   g.add_edge(3,4)
   g.add_edge(4,3)
   g.add_edge(4,1)
   g.add_edge(1,4)


print(g.depth_first_search(0,4))
print(g.shortest_path(0 ,4))
print(g.is_cyclic())
