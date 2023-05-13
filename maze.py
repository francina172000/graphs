class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = {}
        
    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
    
    def remove_edge(self, u, v):
        if u in self.graph:
            if v in self.graph[u]:
                self.graph[u].remove(v)
                

    def has_edge(self, u, v):
        result = False
        if u in self.graph:
            if v in self.graph[u]:
                result = True
        return result

class Maze:
    def __init__(self, size):
        self.size = size
        self.nodes = []
        self.graph = Graph(size*size)

        # label the nodes from 0 to (N*N)-1
        for i in range(0, self.size):
            self.nodes.append([])
            for j in range(0, self.size):
                self.nodes[i].append(i*self.size + j)

        # each node in the graph is connected to UP, DOWN, LEFT, RIGHT (if they exist)
        for i in range(0, self.size):
            for j in range(0, self.size):
                node = self.nodes[i][j]
                if i > 0:
                    up = self.nodes[i-1][j]
                    self.graph.add_edge(node, up)
                if i < self.size-1:
                    down = self.nodes[i+1][j]
                    self.graph.add_edge(node, down)
                if j > 0:
                    left = self.nodes[i][j-1]
                    self.graph.add_edge(node, left)
                if j < self.size-1:
                    right = self.nodes[i][j+1]
                    self.graph.add_edge(node, right)
                    
    def print(self):
        result = ' '+('_ ' * (self.size-1))+'_\n'
        for i in range(self.size):
            result+='|'
            for j in range(self.size):
                node = self.nodes[i][j]
                # check the floor (bottom wall)
                if i < self.size-1 and self.graph.has_edge(node, self.nodes[i+1][j]):
                    result+='_'
                elif (i == self.size-1):
                    result+='_'
                else:
                    result+=' '

                # check the right wall
                if j < self.size-1 and self.graph.has_edge(node, self.nodes[i][j+1]):
                    result+='|'
                elif i < self.size-1 and j < self.size-1:
                    result+=' '
                elif i == self.size-1 and j < self.size-1:
                    result+='_'
            result+='|\n'
        print(result)
    

    def sptree(self,start):
      
      end=(self.size*self.size)-1
      visited=[]
      queue=[]
      thisdict={}
      visited.append(start)
      queue.append(start)
    #   l=len(queue)
      while end not in visited:

         ele=queue.pop()
         
         if ele in self.graph.graph:
            list=[]
            x=self.graph.graph[ele]
            for i in x:
               if i not in visited:
                  visited.append(i)
                  queue.append(i)
                  list.append(i)
                  thisdict[ele]=list 
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
    #   return create
      l=len(create)
      for i in create:
          inde = create.index(i)
          if inde+1 <l:
              res=self.graph.has_edge(create[inde],create[inde+1])
              if res==True:
                  self.graph.remove_edge(create[inde],create[inde+1])
    
    
    def depth_first_search(self):
        s=0
        end=(self.size*self.size)-1
        visited=[]
        queue=[]
        thisdict={}
        visited.append(s)
        queue.append(s)
        l=len(queue)
        while l>0:
            list=[]
            x=self.graph.graph[queue[l-1]]
            for i in x:
                if (i in visited)!=1:
                    queue.append(i)
                    visited.append(i)
                    list.append(i)
                    thisdict[queue[l-1]]=list
                    break
            if l==len(queue):
                queue.pop(l-1)
            l=len(queue)
        create=[]
        create.append(end)
        def get_key(val):
            for key, value_list in thisdict.items():
                if val in value_list:
                    return key
        l=len(create)
        while s not in create:
            key=get_key(create[l-1])
            create.append(key)
            l=len(create)
        create.reverse()
        l=len(create)
        for i in create:
            inde=create.index(i)
            if inde+1<l:
                res=self.graph.has_edge(create[inde],create[inde+1])
                if res==True:
                    self.graph.remove_edge(create[inde],create[inde+1])
                res=self.graph.has_edge(create[inde+1],create[inde])
                if res==True:
                    self.graph.remove_edge(create[inde+1],create[inde])



    


        


        

                    
      
              
      
      
              
                
        
maze = Maze(3)
maze.print()
maze.depth_first_search()
maze.print()
print(maze.graph.graph)
# dict=maze.sptree(0,8)
# print(dict)
# # maze.print()
# print("Welcome to 2D maze")
