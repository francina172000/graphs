import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Graph {

    /*
     * Complete the 'bfs' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER m
     *  3. 2D_INTEGER_ARRAY edges
     */

    public static void bfs(int n, int m, List<List<Integer>> edges) {
    // Write your code here

    }

    public static void main(String[] args) throws IOException {
         BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

         try {
             String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

             int n = Integer.parseInt(firstMultipleInput[0]);
             int m = Integer.parseInt(firstMultipleInput[1]);

             List<List<Integer>> edges = new ArrayList<>();

             IntStream.range(0, m).forEach(i -> {
                 try {
                     edges.add(
                         Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                             .map(Integer::parseInt)
                             .collect(toList())
                     );
                 } catch (IOException ex) {
                     throw new RuntimeException(ex);
                 }
             });


             Graph.bfs(n, m, edges);

          } 
          catch (IOException ex) {
             throw new RuntimeException(ex);
        }
        bufferedReader.close();
    }
}

