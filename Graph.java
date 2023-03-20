// Java program to print breadthFirstSearch traversal from a given source
// vertex. breadthFirstSearch(int s) traverses vertices reachable from s.
import java.io.*;
import java.util.*;
import java.util.HashMap;

// This class represents a directed graph using adjacency
// list representation
class Graph {
	private int V; // No. of vertices
	private LinkedList<Integer> adj[]; // Adjacency Lists

	// Constructor
	Graph(int v)
	{
		V = v;
		adj = new LinkedList[v];
		for (int i = 0; i < v; ++i)
			adj[i] = new LinkedList<Integer>();
	}

	// Function to add an edge into the graph
	void addEdge(int v, int w) { adj[v].add(w); }

	// prints breadthFirstSearch traversal from a given source s
	void breadthFirstSearch(int s)
	{

	}
	int[] shortestPath(int start, int end){
		HashMap<Integer, Integer> prev = new HashMap<Integer, Integer>();
		ArrayList<Integer> queue = new ArrayList<Integer>();
		boolean []visited = new boolean[V];
		queue.add(start);
		while (queue.size() > 0){
			int parent = queue.remove(0);
			ListIterator iter = adj[parent].listIterator();
			while (iter.hasNext()){
				Integer node = (Integer)iter.next();
				if (!visited[node]){
					prev.put(node, parent);
					visited[node] = true;
					queue.add(node);
				}
			}
		}

		ArrayList<Integer> path = new ArrayList<Integer>();
		path.add(end);
		int node = end;
		while (! path.contains(start)){
			path.add(prev.get(node));
			node = prev.get(node);
		}

		int []flippedPath = new int[path.size()];
		int next = 0;
		for (int i = path.size()-1; i >=0; i--){
			flippedPath[next] = path.get(i);
			next++;
		}

		return flippedPath;
	}

 	// Driver method to
	public static void main(String args[])
	{
		Graph g = new Graph(4);

		g.addEdge(0, 1);
		g.addEdge(1, 0);
		g.addEdge(0, 2);
		g.addEdge(2, 0);
		g.addEdge(1, 2);
		g.addEdge(2, 1);
		g.addEdge(2, 3);
		g.addEdge(3, 2);
		g.addEdge(1, 3);
		g.addEdge(3, 1);

		/* 
		System.out.println(
			"Following is Breadth First Traversal "
			+ "(starting from vertex 2)");

		g.breadthFirstSearch(2);
		*/
		int []path = g.shortestPath(0, 3);
		String pathString = "";
		for (int i = 0; i < path.length; i++){
			pathString+=path[i]+" ";
		}
		System.out.println(pathString);
	}
}

