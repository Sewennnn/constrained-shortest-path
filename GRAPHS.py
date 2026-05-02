
class Minheap:

    def __init__(self, maximum_length):
        """
        This is init for minheap for when a minheap is initialised(taken from FIT1008 and modified to minheap)
        Written by: Choong Yu Xin

        Precondition: have maximum length > 0
        Postcondition: if maximum_length > 0, create the array 

        Input: the maximum number of vertices(param maximum_length)
        Return: nothing

        Time complexity:
            Best case analysis: O(N), where N is param maximum_length(maximum number of vertices), because i initialise array with total size (N+1)
            Worst case analysis: O(N), where N is maximum_length(maximum number of vertices), because i initialise array with total size (N+1)

        Space complexity:
            Input space analysis: O(1), because param maximum length is an int
            Aux space analysis: O(N), where N is param maximum_length(maximum number of vertices), because i initialise array with total size (N+1)

        """
        self.maximum_length = maximum_length
        self.length = 0
        self.array_index = [None] * (maximum_length + 1)
        self.the_array = [None] * (maximum_length +1)

  

    def is_full(self):
        """
        This is to check if the minheap is full
        Written by: Choong Yu Xin

        Precondition: self.the_array and self.length > 0
        Postcondition: return true if minheap is full, false if minheap is not full

        Input: no input
        Return: nothing
        Time complexity:
            Best time analysis: O(1), because i compare the length 
            Worst time analysis: O(1), because i compare the length

        Space complexity:
            Input space analysis: O(1), because im just checking length
            Aux space analysis: O(1), because no aux space created

        """
        return self.length + 1 == len(self.the_array)

    def rise(self, k) -> None:
        """
        This function is to rise element at index k in the minheap until the element is at correct position to maintain the minheap structure
        Written by: Choong Yu Xin
    
        Precondition: 1 <= k <= self.length
        Postcondition: updates the minheap

        Input: k, where k is index of element in minheap
        Return: nothing
        Time complexity: 
            Best time analysis: O(1), when my element is already at correct position, no need to swap
            Worst time analysis:O(logN), where N is number of vertices, swap elements until reach parent node

        Space complexity:
            Input space analysis: O(1), since k is to access index in minheap
            Aux space analysis: O(1), since no aux space is created

        """
        item = self.the_array[k]
        
        while k > 1 and item < self.the_array[k // 2]:
            self.the_array[k] = self.the_array[k // 2]
            self.array_index[self.the_array[k//2][1].id] = k

            k = k // 2
        self.the_array[k] = item
        self.array_index[item[1].id] = k
        

    def add(self, vertex) -> bool:
        """
        This function adds an element to minheap and rises to correct position in minheap
        Written by: Choong Yu Xin

        Precondition: self.is_full returns True
        Postcondition: the added element is at its correct position in minheap

        Input: param vertex, which is an element of type vertex in this context (i want to code djikstra which requires a min heap so all elements in minheap are vertices)
        Return: nothing

        Time complexity:
            Best time analysis: O(1), when self.is_full returns True, dont enter the if condition
            Worst time analysis: O(logN), where N is number of vertices in minheap, because of my rise method, element rises and swaps to the parent node

        Space complexity:
            Input space analysis: O(1), because input is a Vertex object
            Aux space analysis: O(1), because im appending my vertex param into array[index], not adding new space to the array

        """
        if self.is_full() == False:
            self.length += 1
            self.the_array[self.length] = vertex
            self.rise(self.length)

    def smallest_child(self, k):
        """
        This element returns the index of k's child with greatest value.
        Written by: Choong Yu Xin

        Precondition: 1 <= k <= self.length // 2
        Postcondition: The index of smallest child of parent index k in minheap is returned

        Input: param k, which is index k in minheap
        Return: index of smallest child of parent index k

        Time complexity: 
            Best time analysis: O(1), since we are just comparing the child nodes
            Worst time analysis: O(1), since we are just comparing the child nodes

        Space complexity:
            Input space analysis: O(1), since k is index for accessing the array
            Aux space analysis: O(1), since im just checking for the smallest child, im not creating new space for memory

        """
        if 2 * k == self.length or \
            self.the_array[2 * k] < self.the_array[2 * k + 1]:
            return 2 * k
        else:
            return 2 * k + 1

    
        

    def sink(self, k: int) -> None:
        """ 
        This function makes the element at index k sink to the correct position.
        Written by: Choong Yu Xin

        Precondition: 1 <= k <= self.length
        Postcondition: The element at index k gets swapped to the correct position in minheap

        Input: param k, which is the index of element in minheap
        Return: nothing

        Time complexity:
            Best time analysis: O(1), when element at index k is already at correct position in minheap
            Worst time analysis: O(logN), where N is number of elements in minheap, because the element at index k sinks to bottom of minheap

        Space complexity:
            Input space analysis: O(1), since k is index for accessing the array
            Aux space analysis: O(1), since no additional space is created, i am only comparing and swapping elements until they are at correct position

        """
        item = self.the_array[k]

        while 2 * k <= self.length:
            max_child = self.smallest_child(k)
            if self.the_array[max_child] < item:
                break
            self.the_array[k] = self.the_array[max_child]
            self.array_index[self.the_array[max_child][1].id] = k
            k = max_child

        self.the_array[k] = item
        self.array_index[item[1].id] = k


    def get_min(self):
        """ 
        This function removes and returns the smallest element from the heap. 
        Written by: Choong Yu Xin

        Precondition: self.length > 0
        Postcondition: the smallest element in the minheap is removed from minheap and returned

        Input: nothing
        Return: the smallest element in the minheap

        Time complexity:
            Best time analysis: O(1), when the sink function for index 1 is already in its correct position
            Worst time analysis: O(logN), where N is number of elements in minheap, because when calling sink function, the element sinks to bottom of heap

        Space complexity:
            Input space analysis: O(1), because the function does not take any additional input that scales with the size of the data structure.
            Aux space analysis: O(1) , since no additional space is created, i am only comparing and swapping elements until they are at correct position

        """
        if self.length == 0:
            raise IndexError("Heap is empty")

        min_elm = self.the_array[1]  

        self.the_array[1] = self.the_array[self.length]
        self.length -= 1

        self.sink(1)

        return min_elm
    
    def update(self, vertex, new_distance):
        """
        This function updates the particular information(param new_distance) stored in a particular element(param vertex) in minheap.
        Written by: Choong Yu Xin

        Precondition: self.array_index[vertex.id] is not None
        Postcondition: the particular element(param vertex) is updated with new information(param new_distance) in minheap

        Input: vertex, which is a vertex object stored in minheap, and new_distance, which is an int to update the new distance of vertex element
        Return: nothing

        Time complexity:
            Best time analysis: O(1), because when calling rise or sink function, vertex element is already at correct position
            Worst time analysis: O(logN), where N is number of vertices, because when calling rise or sink function, 
            vertex element rises to top, or vertex element sinks to bottom

        Space complexity:
            Input space analysis: O(1), because the function does not take any additional input that scales with the size of the data structure
            Aux space analysis: O(1), since no additional space is created, i am only comparing and swapping elements until they are at correct position

        """
        if self.array_index[vertex.id] == None:
            raise ValueError("Vertex not found in the heap")
        
        index = self.array_index[vertex.id]
        self.array_index[vertex.id] = None
       
        if new_distance < self.the_array[index][0]:
            
            self.the_array[index] = (new_distance, vertex)
            self.rise(index)  # Adjust the min heap upwards from the index
        else:
            self.the_array[index] = (new_distance, vertex)
            self.sink(index)  # Adjust the min heap downwards from the index

        


class Graph:

    def __init__(self, V):
        """
        This is init function for creating a graph.
        Written by: Choong Yu Xin

        Precondition: V > 0
        Postcondition: if V > 0, create array of size (V+1)

        Input: V, which is number of vertices
        Return: nothing

        Time complexity: 
            Best time analysis: O(V), where V(param V) is number of vertices, because i create array of size (V+1)
            Worst time analysis: O(V), where V(param V) is number of vertices, because i create array of size (V+1)

        Space complexity:
            Input space analysis: O(1), because V(param V) is integer
            Aux space analysis: O(V), where where V(param V) is number of vertices, because i create array of size (V+1)

        """
        self.vertices = [None] * (V + 1)
        for i in range(V+1):
            self.vertices[i] = Vertex(i)
        self.all_edges = []
        
    
    def add_edges(self, argv_edges):
        """
        This function is adding the edges that connects from a vertex to another vertex.
        Each edge consists of tuple (u,v,w), where u is current vertex id, v is next vertex id, and w is weight that links them together
        Ex: edge(2,1,3), means that i have directed edge from vertex 2 to vertex 1 with weight 3.
        Written by: Choong Yu Xin

        Precondition: argv_edges(param) is not empty, and is a list of tuples consisting of (u,v,w)
        Postcondition: all directed edges are added to graph

        Input: argv_edges, where it is a list of tuples consisting of (u,v,w)
        Return: nothing

        Time complexity: 
            Best time analysis: O(len(argv_edges)), because you loop for all edge in argv_adges
            Worst time analysis: O(len(argv_edges)), because you loop for all edge in argv_adges

        Space complexity:
            Input space analysis: O(len(argv_edges)) , because i take in a list of tuples and loop through them
            Aux space analysis: O(len(argv_edges)), because i loop through the list of tuples, get each tuple(edge) and append to my new_add_edges
            so my new_add_edges increases linearly to len(argv_edges)

        """
        for edge in argv_edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            current_edge = Edge(u,v,w)
            current_vertex = self.vertices[u]
            current_vertex.add_edge(current_edge)
            self.all_edges.append((u,v,w))
        

    def flip_edges(self):
        """
        This function flips the edges of the whole graph
        Written by: Choong Yu Xin
        
        Precondition: self.all_edges is not empty
        Postcondition: all edges are flipped

        Input: nothing
        Return: nothing

        Time complexity: 
            Best time analysis: O(len(self.all_edges)), where self.all_edges are all the edges of my graph, 
            because i loop for (len(self.all_edges)) times.
            Worst time analysis: O(len(self.all_edges)), where self.all_edges are all the edges of my graph, 
            because i loop for (len(self.all_edges)) times.

        Space complexity:
            Input space analysis: O(1), because the function does not take any additional input that scales with the size of the data structure
            Aux space analysis: O(len(self.all_edges)), where self.all_edges are all the edges of my graph, because i loop for (len(self.all_edges)),
            and every loop i append to new_all_edges, which is creating new spaces.
        
        """
        new_all_edges = []
        for i in range(len(self.all_edges)):
            edge = self.all_edges[i]
            first_vertex = edge[0]
            second_vertex = edge[1]
            weight = edge[2]
            new_all_edges.append((second_vertex, first_vertex, weight))

        self.all_edges = []
        self.add_edges(new_all_edges)
            

    def clear_all_edges(self):
        """
        This function clears all the edges in my graph.
        Written by: Choong Yu Xin

        Precondition: self.vertices is not empty
        Postcondition: all edges are cleared.

        Input: nothing
        Return: nothing

        Time complexity: 
            Best time analysis: O(len(self.vertices)), where self.vertices are all the vertices in my graph, 
            because i loop through all vertices to clear the edges.
            Worst time analysis: O(len(self.vertices)), where self.vertices are all the vertices in my graph, 
            because i loop through all vertices to clear the edges.

        Space complexity:
            Input space analysis: O(1), because the function does not take any additional input that scales with the size of the data structure
            Aux space analysis: O(1), because im assigning empty lists to all of my vertex edges.


        """
        for vertex in self.vertices:
            vertex.edges = []

    def reverse_edges(self):
        """
        This function reverses all the edges of the graph.
        Written by: Choong Yu Xin

        Precondition: self.clear_all_edges and self.flip_edges is not empty
        Postcondition: all edges of vertices are reversed

        Input: nothing
        Return: nothing

        Time complexity:
            Best time analysis: O(len(self.vertices) + len(self.all_edges)), 
            because when i call the functions below, i loop through self.vertices and self.all_edges
            Worst time analysis:  O(len(self.vertices) + len(self.all_edges)), 
            because when i call the functions below, i loop through self.vertices and self.all_edges

        Space complexity:
            Input space analysis: O(1), because the function does not take any additional input that scales with the size of the data structure
            Aux space analysis: O(1), because i dont create any extra space for memory in this function.
        """
        self.clear_all_edges()
        self.flip_edges()

    def reset_graph(self):
        """
        This function resets all the vertices in graph.
        Written by: Choong Yu Xin

        Precondition: self.vertices is not empty
        Postcondition: All my vertices in my graph is reset to undiscovered, unvisited, distance is 0, previous is None

        Input: nothing
        Return: nothing

        Time complexity:
            Best time analysis: O(len(self.vertices)), where self.vertices are all vertices in graph, because i loop through self.vertices
            Wost time analysis: O(len(self.vertices)), where self.vertices are all vertices in graph, because i loop through self.vertices

        Space complexity:
            Input space analysis: O(1), because the function does not take any additional input that scales with the size of the data structure
            Aux space analysis: O(1), because i dont create any extra space for memory in this function.

        """
        for vertex in self.vertices:
            vertex.discovered = False
            vertex.visited = False
            vertex.distance = 0
            vertex.previous = None

    def backtracking(self, id):
        """
        This function backtracks and finds all the previous vertices until the source.
        Written by: Choong Yu Xin

        Precondition: vertex.previous is not None
        Postcondition: Gets all the lists of previous vertices

        Input: id(param id), which is the id of the vertex
        Return: a list of all previous vertices all the way to the source.
        Time complexity:
            Best time analysis: O(1), where there is no previous vertex.
            Worst time analysis: O(len(self.vertices)), where self.vertices are the number of vertices, 
            when all my vertices are travelled to.

        Space complexity:
            Input space analysis: O(1), because id is the id used to find the vertex in O(1)time.
            Aux space analysis: O(V), where V is all my previously visited vertices, because i backtrack to find all previously visited vertices.

        """
     
        vertex = self.vertices[id]

        previous_vertices = []
 
        previous_vertices.append(id)
    
        while vertex.previous is not None:
           
            if self.vertices[vertex.previous.id] is not None:
                previous_vertices.append(vertex.previous.id)
                vertex = vertex.previous
            

      
        return previous_vertices

       

    def dijkstra (self, source):
        """
        This is function for dijkstra which gets shortest distance to all vertices in the graph.
        Dijkstra uses a minheap which is a priority queue to get the shortest distance of all vertices.
        In my implementation, i start from the source, then put all my vertices into my minheap. I pop out the shortest 
        distance, set vertex.visited to True, find all the edges and add that to discovered minheap, update the distance of the neighbouring 
        vertices, and continue the loop until all vertices in minheap is popped out and all are visited.

        Written by: Choong Yu Xin
        Precondition: self.vertices is not empty, source is not None and is a valid vertex id
        Postcondition: Get the shortest distance to all the vertices in the graph

        Input: source(param source), which is the id of the vertex to start from
        Return: nothing

        Time complexity:
            Best time analysis: O(ElogV), where E is total number of edges, V is total number of vertices,
            because i loop through all edges in a vertex and call add and update function, which is logV
            Worst time analysis: O(ElogV), where E is total number of edges, V is total number of vertices,
            because i loop through all edges in a vertex and call add and update function, which is logV

        Space complexity:
            Input space complexity: O(1), where source is id of the vertex you want to start from, use if to access the vertex
            Aux space complexity: O(V), where V is total number of vertices, because i creat a minheap of size V.

        """
        source = self.vertices[source]
        source.distance = 0
        
        discovered = Minheap(len(self.vertices))
            
        discovered.add((source.distance, source))     
        while discovered.length > 0:
           
            u = discovered.get_min()[1]
            u.visited = True
            u.discovered = True
           
            for edge in u.edges:
                v = edge.v                
                v = self.vertices[v]
                if v.discovered == False:
                    v. discovered = True
                    v.distance = u.distance + edge.w
                    
                    v.previous = u
                        
                    discovered.add((v.distance, v) )
                    
                else:
                    if v.visited == False:  
                        
                        if v.distance > (u.distance + edge.w):    
                            v.distance = u.distance + edge.w   
                            v. previous = u     
                            discovered.update(v, v.distance)        
                           
        
class Vertex:
    
    def __init__(self,id) -> None:
        """
        This is init function for creating a vertex.
        Written by: Choong Yu Xin

        Precondition: id is valid integer, not None
        Postcondition: Initializes all the conditions for a vertex(list of edges, id, discovered is False, visited is False, distance is 0, previous is None)

        Input: id(param id), where id is the id of vertex
        Return: nothing

        Time complexity:
            Best time analysis: O(1), where all initialization of vertices is constant
            Worst time analysis: O(1), where all initialization of vertices is constant

        Space complexity:
            Input space complexity: O(1), because the id is just for initialising the vertex id.
            Aux space complexity:O(1), because init initialises constant number of attributes.
        """
        self.id = id
        self.edges= []
        self.discovered = False
        self.visited = False
        self.distance = 0
        self.previous = None

    def __lt__(self, other):
        """
        This is magic method that compares the distances of two vertices.
        Written by: Choong Yu Xin

        Precondition: distance of two vertices are not None
        Postcondition: returns True or False statement 

        Input: other vertex(param other), where it is the other vertex you want to compare
        Return: True or False

        Time complexity:
            Best time analysis: O(1), because is int comparison
            Worst time analysis: O(1), because it is int comparison

        Space complexity:
            Input space complexity: O(1), because the input (param other) is just to get the distance of that other vertex which is constant.
            Aux space complexity: O(1), because no extra space is created in memory.

        """
        # Define comparison logic based on distance
        return self.distance < other.distance


    def add_edge(self,edge):
        """
        This is function to add edge to this vertex.
        Written by: Choong Yu Xin

        Precondition: edge is Edge object tuple in form of (u,v,w) where u is vertex id, v is other vertex id, and w is weight of edge.
        Postcondition: edge is added to vertex

        Input: edge(param edge), where edge is is tuple (u,v,w)
        Return: nothing

        Time complexity: 
            Best time analysis: O(1), since always append edge to self.edges, is constant
            Worst time analysis: O(1), since always append edge to self.edges, is constant

        Space complexity:
            input space complexity: O(1), where i append the input to my self.edges, which is constant.
            Aux space complexity: O(1), where i append a edge in form of (u,v,w) to self.edges, which is constant.

        """
        self.edges.append(edge)




class Edge:
    
    def __init__(self, u, v, w):
        """
        This is init function for creating a edge.
        Written by: Choong Yu Xin

        Precondition: u,v,w are valid integers.
        Postcondition: Initializes the u, v,w of params as attribute(u is first vertex id, v is 2nd vertex id, w is weight of edge)
        eg. i have a edge(2,5,1), which means i have directed edge from vertex 2 to vertex 5 with weight of 5.

        Input: u,v,w , (u is first vertex id, v is 2nd vertex id, w is weight of edge), see example above
        Return: nothing

        Time complexity:
            Best time analysis: O(1), where all initialization of edge is constant
            Worst time analysis: O(1), where all initialization of edge is constant

        Space complexity:
            Input space complexity: O(1), because init initialises constant number of attributes.
            Aux space complexity: O(1), because init initialises constant number of attributes.
        """
        self.u = u
        self.v = v
        self.w = w
       

        
    

if __name__ == "__main__":

    '''
    Min Heap Test Case without Update
    '''
    # sort_me = [4,2,2,51,52,5,6,7,9,6]

    # minheap = Minheap(len(sort_me))

    # # Minheap.heapify(sort_me, 10)

    # print (minheap)
    
    # for i in range(len(sort_me)):
    #     minheap.add(sort_me[i])

    # print(minheap)

    # print (minheap.get_min())
    # print(minheap.smallest_child(1))


    '''
    Djikstra Test Case All Implemented taking input of vertices and edges
    so full implementation of the code above
    '''

    total_vertices = 5
    edges = []
    edges.append((3,1,5))       # u = 3, v = 1, w = 5
    edges.append((1,2,1))
    edges.append((3,2,5))
    edges.append((2,3,7))
    my_graph = Graph(total_vertices )
    
    

    my_graph.add_edges(edges)
    my_graph.flip_edges()
    my_graph.dijkstra(1)
    for v in my_graph.vertices :
     print(f'vertex {v.id} distance : {v.distance}')

    

    # =======================================
    # edges = []

    # total_vertices = [0,1,5,3,4,6,2]

    # edges.append((0,1,18))
    # edges.append((0,2,3))
    # edges.append((1,3,14))
    # edges.append((2,4,15))
    # edges.append((2,5,5))
    # edges.append((5,4,5))
    # edges.append((4,3,6))
    # edges.append((4,1,3))
    # edges.append((4,6,5))
    # edges.append((5,6,11))
    # my_graph = Graph(6)
    # my_graph.add_edges(edges)
    # my_graph.reverse_edges()

    # my_graph.dijkstra(0)

    # for v in my_graph.vertices :
    #  print(f'vertex {v.id} distance : {v.distance}')

    # ============================================


    # edges = []

    # total_vertices = [0,1,2,3,4] # s=0 a=1 b=2 c=3 d=4

    # #s pointer
    # edges.append((0,1,10))
    # edges.append((0,3,5))
    # #a pointer
    # edges.append((1,3,2))
    # edges.append((1,2,1))
    # #bpointer
    # edges.append((2,4,4))

    # #cpointer
    # edges.append((3,4,2))
    # edges.append((3,1,3))
    # edges.append((3,2,9))
    # #d pointer
    # edges.append((4,2,6))
    # edges.append((4,0,7))
    # my_graph = Graph(total_vertices, edges)
    # my_graph.add_edges(edges)

    # my_graph.dijkstra(0,4)

    # for v in my_graph.vertices :
    #  print(f'vertex {v.id} distance : {v.distance}')


    

    
