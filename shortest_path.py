from GRAPHS import *

class TreeMap:
   

    def __init__(self, roads, solulus):
        """
        This is init for TreeMap for when a TreeMap is initialised.
        When initialised, i make vertices then create two graphs(one with normal edges, one with flipped edges)
        
        Written by: Choong Yu Xin

        Precondition: roads > 0
        Postcondition: after all attributes are initialized, terminate

        Input: the roads as tuples(u,v,w), where u is vertex id, v is another vertex id of next edge, w is weight of edge
        Example: (2,5,4), i have edge from vertex 2 to vertex 5, with weight 4, 
        and the solulus as tuples(x,y,z), where x is the solulu tree id, y is the time the claw at solulu tree,
        and z is the tree that will be transported to. Ex: solulu tree (2,6,7), at solulu tree 2, i take 6 minutes to destroy 
        the solulu tree, and i will then be transported to tree 7.

        Return: nothing
        Time complexity: 
            Best time analysis: O(R + T), where R is the number of roads, and T is number of trees, 
            because i call reverse_edges function which has O(R+T) best time complexity
            Worst time complexity: O(R+T), where R is the number of roads, and T is number of trees, 
            because i call reverse_edges function which has O(R+T) best time complexity

        Space complexity:
            Input space analysis: O(R+S), where R is the number of roads, and S is number of solulus,
            because i save the roads and solulus as self.roads and self.solulus
            Aux space analysis: O(R+T+S), where R is the number of roads, and S is number of solulus,
            and T is number of trees, because i store R as list of tuples in self.roads, S as list of tuples
            in self.solulus, and i create graph with max vertex which is T, then i call add_edges function which
            has aux space of R roads which gives me O(2T+S+R), which has big O of O(R+T+S)
        
        """

        self.roads = roads
        self.solulus = solulus
        max_vertex = -1
        for road in self.roads:
            first_vertex = road[0]
            second_vertex = road[1]
            max_value = max(first_vertex, second_vertex)
            if max_value > max_vertex:
                max_vertex = max_value

        self.first_graph = Graph(max_vertex)
        self.first_graph.add_edges(roads)
        self.second_graph = Graph(max_vertex)
        self.second_graph.add_edges(roads)
        self.second_graph.reverse_edges()
        


    def escape(self, start, exits):
        """
        This is the function to escape from the treemap.
        Written by: Choong Yu Xin

        Approach description(for main function of q2): First i reset both of my graphs(graph one with normal edges, 
        and graph two where i flip the edges).This is for when i call .escape multiple times on same treemap, previous
        calls will not effect the 2 graphs when i call it again. Then i call dijkstra on the first graph(to get all my 
        distances to all trees). Then, in my second graph, i add a dummy vertex with outgoing edges to all of my exit trees
        and call dijkstra on the second graph. This is so i can get the distance from my teleport trees to the exits.
        Then, i loop through all my solulu trees, getting the shortest distance from start to the solulu trees in my first
        graph. I initialize shortest distance to inf first, then for each loop, i get the total distance from start to any exit trees 
        plus the time needed to destroy the solulu tree. If distance is smaller than the current shortest distance, 
        i set the shortest distance to this distance, then save the solulu tree that i want to break. When i exit the loop,
        i check if shortest distance is inf(means that no possible routes) then return none, if not i backtrack both graphs using the 
        solulu tree that i want to break, add both graphs together and return the (shortest_distance, route) in a tuple.

        Precondition: len(exits)> 0, start is not None
        Postcondition: shortest distance and route taken is returned

        Input: start(param start) which is a id of the tree that you start at, and exits(param exits) which is a list of 
        all exit trees id.
        Return: (shortest distance, route taken) which is a tuple, if there are no routes, return None

        Time complexity:
            Best time analysis: O(RlogT), because i call reset graph function which is O(T) then djikstra, which
            is O(RlogT), then i loop through exits to add edge from dummy vertex to exit trees, which is O(T), in 
            the end will simplify to O(RlogT).
            Worst time analysis: O(RlogT), because i call reset graph function which is O(T) then djikstra, which
            is O(RlogT), then i loop through exits to add edge from dummy vertex to exit trees, which is O(T), in 
            the end will simplify to O(RlogT).

        Space complexity:
            Input space analysis: O(E), where E is list of exits, because there is space required to store the list of exit trees.
            Aux space analysis: O(T), where T is number of trees, since i call dijkstra twice which has total aux space of O(2T),
            then i call backtracking which also has aux space of O(T), which i end up with O(3T) which then simplfies to O(T).
        
        """
        self.first_graph.reset_graph()
        self.second_graph.reset_graph()
        self.first_graph.dijkstra(start)
        dummy_vertex = Vertex(len(self.second_graph.vertices) )
        self.second_graph.vertices.append(dummy_vertex)
        for exit in exits:
           
            self.second_graph.vertices[dummy_vertex.id].add_edge(Edge(dummy_vertex.id, exit, 0))
           
        self.second_graph.dijkstra(dummy_vertex.id)
        
        inf = float('inf')
        shortest_distance = inf
        solulu_to_break = None
        
        for solulu in self.solulus:
            if self.first_graph.vertices[solulu[0]].visited is True and self.second_graph.vertices[solulu[2]].visited is True:
            
                distance = self.first_graph.vertices[solulu[0]].distance +  solulu[1] + self.second_graph.vertices[solulu[2]].distance
               
                if distance < shortest_distance:
                    shortest_distance = distance
                    solulu_to_break = solulu
        
        if shortest_distance == inf:
            return None

        first_route = self.first_graph.backtracking(solulu_to_break[0])
        first_route.reverse()
        second_route = self.second_graph.backtracking(solulu_to_break[2])
        second_route.pop()
          
        for id in second_route:
            if id != first_route[len(first_route)-1]:
                first_route.append(id)

        dummy_vertex = self.second_graph.vertices.pop()
        return (shortest_distance, first_route)
    

    








        

        

        

        















